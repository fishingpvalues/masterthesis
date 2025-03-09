import pandas as pd
import numpy as np
import os
import json
import random
from typing import Union

# Further reduced constants for error injection probabilities and proportions
NA_COLUMN_PROB = 0.005  # Even lower chance to modify a column with NA values
NA_ROW_PROPORTION = 0.005  # Even lower proportion of rows to set NA per selected column

ID_MOD_PROPORTION = 0.005  # Lower proportion of rows to modify ID columns

TIMESTAMP_ERROR_PROPORTION = (
    0.005  # Lower proportion of rows to receive timestamp errors
)
TIME_NEGATIVE_PROB = 0.005  # Keep same within a timestamp error

INVALID_FLAG_PROPORTION = 0.005  # Lower random invalid marking

# Reduced probabilities for additional errors (step 6)
RANDOM_ERROR_PROPORTION = 0.01  # Lower overall proportion for additional errors
TIME_SWAP_PROB = 0.005  # Lower probability to swap start_time and end_time
FOREIGN_KEY_PROB = 0.005  # Lower probability to inject a foreign key violation
MISMATCH_PART_PROB = 0.005  # Lower probability to assign a random part_id
DUPLICATE_ROW_PROB = 0.005  # Lower probability to duplicate a row
ID_SWAP_PROB = 0.005  # Lower probability to swap any two ID columns


def generate_false_data(
    input_df: Union[pd.DataFrame, str],
    apply_na: bool = True,
    apply_id_mod: bool = True,
    apply_timestamp_err: bool = True,
    apply_mappings_replacement: bool = True,
    apply_invalid_flag: bool = True,
    apply_additional_errors: bool = True,
    additional_invalid_ratio: float = 0.0,  # New parameter, e.g., 0.5 -> 50% extra invalid rows.
    random_seed: int = None,  # New parameter to set the random seed
) -> pd.DataFrame:
    """
    Reads mapping JSONs from the 'output' folder and generates false data.
    Accepts either a pandas DataFrame or a CSV file path.

    Each error modification can be toggled via function parameters.

    The function introduces a variety of errors to simulate false/synthetic data:
      1. Random NA values.
      2. Slight modifications of ID columns (increment/decrement by 1) while ensuring
         the new values fall within the ground-truth mappings.
      3. Overlapping or inconsistent timestamps.
      4. Replacements using external mappings as ground truth.
      5. Randomly marking some rows as invalid.
      6. Additional randomized errors on selected rows:
         a. Time inconsistency (swapping start_time and end_time).
         b. Foreign key violations (assigning -999 or None to an ID column).
         c. Mismatched parts (assign a random part_id, using allowed values if available).
         d. Duplicate rows (appending a copy of the row).
         e. ID swapping: Randomly swap any two available ID columns.
         For every modification at any step the affected row's "is_valid" flag is set to 0.

      Additionally, extra invalid rows (with is_valid set to 0) will be generated,
      with a count equal to additional_invalid_ratio multiplied by the number of valid rows.

    Args:
        input_df (Union[pd.DataFrame, str]): Original DataFrame or path to a CSV file.
        apply_na (bool): Toggle NA injection.
        apply_id_mod (bool): Toggle ID modifications.
        apply_timestamp_err (bool): Toggle timestamp modifications.
        apply_mappings_replacement (bool): Toggle mapping replacements.
        apply_invalid_flag (bool): Toggle randomly marking some rows as invalid.
        apply_additional_errors (bool): Toggle additional randomized errors.
        additional_invalid_ratio (float): Ratio of additional invalid rows relative to the count of rows
                                          with is_valid = 1. (E.g., 0.5 adds 50% extra invalid rows.)
        random_seed (int): Seed for random number generators.

    Returns:
        pd.DataFrame: DataFrame with false data introduced.
    """
    # Set the random seed if provided.
    if random_seed is not None:
        import numpy as np

        np.random.seed(random_seed)
        import random

        random.seed(random_seed)

    # Load data from CSV if needed.
    if isinstance(input_df, str) and input_df.lower().endswith(".csv"):
        df = pd.read_csv(input_df, parse_dates=["start_time", "end_time"])
    elif isinstance(input_df, pd.DataFrame):
        df = input_df.copy()
    else:
        raise ValueError(
            "input_df must be a pandas DataFrame or a valid CSV file path."
        )

    # Ensure start_time and end_time are converted to datetime (if not already)
    for col in ["start_time", "end_time"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # Initialize is_valid to 1 everywhere.
    df["is_valid"] = True

    # Load all mapping JSONs from the output folder.
    mappings = {}
    output_folder = "output"
    if os.path.exists(output_folder):
        for file_name in os.listdir(output_folder):
            if file_name.endswith(".json"):
                with open(os.path.join(output_folder, file_name), "r") as f:
                    mappings[file_name] = json.load(f)

    # Build allowed mapping dict for columns using known mapping filenames.
    allowed_mapping = {}
    # part_mapping.json → part_id
    if "part_mapping.json" in mappings and "part_id" in df.columns:
        allowed_mapping["part_id"] = (
            list(mappings["part_mapping.json"].values())
            if isinstance(mappings["part_mapping.json"], dict)
            else []
        )
    # process_mapping.json → process_id
    if "process_mapping.json" in mappings and "process_id" in df.columns:
        allowed_mapping["process_id"] = (
            list(mappings["process_mapping.json"].values())
            if isinstance(mappings["process_mapping.json"], dict)
            else []
        )
    # resource_mapping.json → resource_id
    if "resource_mapping.json" in mappings and "resource_id" in df.columns:
        allowed_mapping["resource_id"] = (
            list(mappings["resource_mapping.json"].values())
            if isinstance(mappings["resource_mapping.json"], dict)
            else []
        )
    # type_mapping.json → process_type
    if "type_mapping.json" in mappings and "process_type" in df.columns:
        allowed_mapping["process_type"] = (
            list(mappings["type_mapping.json"].values())
            if isinstance(mappings["type_mapping.json"], dict)
            else []
        )

    # 1. Randomly introduce NA values.
    if apply_na:
        for col in df.columns:
            if np.random.rand() < NA_COLUMN_PROB:
                na_indices = np.random.choice(
                    df.index, size=int(len(df) * NA_ROW_PROPORTION), replace=False
                )
                df.loc[na_indices, col] = np.nan
                df.loc[na_indices, "is_valid"] = False

    # 2. Slight modifications of ID columns.
    id_columns = [
        "process_execution_id",
        "order_id",
        "part_id",
        "process_id",
        "resource_id",
    ]
    if apply_id_mod:

        def modify_value(x, allowed=None):
            delta = np.random.choice([-1, 1])
            try:
                new_val = x + delta
            except Exception:
                return x
            if allowed and len(allowed) > 0:
                return new_val if new_val in allowed else random.choice(allowed)
            return new_val

        for col in id_columns:
            if col in df.columns:
                num_samples = int(len(df) * ID_MOD_PROPORTION)
                if num_samples > 0:
                    modify_indices = np.random.choice(
                        df.index, size=num_samples, replace=False
                    )
                    allowed = allowed_mapping.get(col, None)
                    df.loc[modify_indices, col] = df.loc[modify_indices, col].apply(
                        lambda x: modify_value(x, allowed)
                    )
                    df.loc[modify_indices, "is_valid"] = False

    # 3. Introduce overlapping or inconsistent timestamps.
    if apply_timestamp_err and "start_time" in df.columns and "end_time" in df.columns:
        inconsistent_time_indices = np.random.choice(
            df.index, size=int(len(df) * TIMESTAMP_ERROR_PROPORTION), replace=False
        )
        for idx in inconsistent_time_indices:
            if pd.isna(df.at[idx, "start_time"]):
                continue
            if np.random.rand() < TIME_NEGATIVE_PROB:
                df.at[idx, "end_time"] = df.at[idx, "start_time"] - pd.Timedelta(
                    minutes=np.random.randint(1, 10)
                )
            else:
                overlap_duration = pd.Timedelta(minutes=np.random.randint(1, 10))
                df.at[idx, "start_time"] = df.at[idx, "start_time"] - overlap_duration
            df.at[idx, "is_valid"] = False

    # 4. Replace values using ground-truth mappings.
    if apply_mappings_replacement:
        for col, allowed in allowed_mapping.items():
            # Skip replacement if allowed mapping list is empty.
            if not allowed:
                continue

            # Convert allowed mapping values to the same type as the column.
            try:
                col_type = df[col].dtype.type
                allowed_converted = [col_type(val) for val in allowed]
            except Exception as e:
                print(f"Could not convert allowed mapping for {col}: {e}")
                allowed_converted = allowed

            # Compute invalid rows where the column value is not in the allowed mapping.
            invalid_vals = ~df[col].isin(allowed_converted)
            if invalid_vals.any():
                # Replace invalid values with a random allowed value.
                df.loc[invalid_vals, col] = df.loc[invalid_vals, col].apply(
                    lambda _: random.choice(allowed_converted)
                )
                df.loc[invalid_vals, "is_valid"] = False

    # 5. Randomly mark some rows as invalid.
    if apply_invalid_flag:
        invalid_indices = np.random.choice(
            df.index, size=int(len(df) * INVALID_FLAG_PROPORTION), replace=False
        )
        df.loc[invalid_indices, "is_valid"] = False

    # Prepare base for additional errors.
    false_data = df.copy()
    num_rows = len(false_data)

    # 6. Additional randomized errors on selected rows.
    if apply_additional_errors:
        for _ in range(int(num_rows * RANDOM_ERROR_PROPORTION)):
            row_index = random.randint(0, num_rows - 1)
            # a. Time inconsistency: Swap start_time and end_time.
            if (
                random.random() < TIME_SWAP_PROB
                and "start_time" in false_data.columns
                and "end_time" in false_data.columns
            ):
                (
                    false_data.loc[row_index, "start_time"],
                    false_data.loc[row_index, "end_time"],
                ) = (
                    false_data.loc[row_index, "end_time"],
                    false_data.loc[row_index, "start_time"],
                )
                false_data.loc[row_index, "is_valid"] = False

            # b. Foreign key violation: Set an ID column to -999 or None.
            if random.random() < FOREIGN_KEY_PROB:
                id_col = random.choice(["process_id", "resource_id", "part_id"])
                if id_col in false_data.columns:
                    false_data.loc[row_index, id_col] = random.choice([-999, None])
                    false_data.loc[row_index, "is_valid"] = False

            # c. Mismatched parts: Assign a random part_id within allowed values.
            if random.random() < MISMATCH_PART_PROB and "part_id" in false_data.columns:
                if "part_id" in allowed_mapping and len(allowed_mapping["part_id"]) > 0:
                    new_val = random.choice(allowed_mapping["part_id"])
                else:
                    new_val = random.randint(1000, 9999)
                false_data.loc[row_index, "part_id"] = new_val
                false_data.loc[row_index, "is_valid"] = False

            # d. Duplicate row: Append a duplicate of the current row if it exists.
            if random.random() < DUPLICATE_ROW_PROB:
                if row_index in false_data.index:
                    duplicate_row = false_data.loc[row_index]
                    false_data = pd.concat(
                        [false_data, duplicate_row.to_frame().T], ignore_index=True
                    )
                    num_rows = len(false_data)

            # e. ID swapping: Randomly swap two ID columns.
            if random.random() < ID_SWAP_PROB:
                available_id_cols = [
                    col for col in id_columns if col in false_data.columns
                ]
                if len(available_id_cols) >= 2:
                    swap_cols = random.sample(available_id_cols, 2)
                    (
                        false_data.loc[row_index, swap_cols[0]],
                        false_data.loc[row_index, swap_cols[1]],
                    ) = (
                        false_data.loc[row_index, swap_cols[1]],
                        false_data.loc[row_index, swap_cols[0]],
                    )
                    false_data.loc[row_index, "is_valid"] = False

    # Generate additional false rows based on the valid rows count.
    if additional_invalid_ratio > 0:
        valid_df = false_data[false_data["is_valid"] == 1]
        num_valid = len(valid_df)
        num_additional = int(num_valid * additional_invalid_ratio)
        if num_additional > 0:
            additional_rows = valid_df.sample(n=num_additional, replace=True).copy()
            additional_rows["is_valid"] = False
            false_data = pd.concat([false_data, additional_rows], ignore_index=True)

    # Recalculate the "duration" column (in seconds) for all rows based on updated start_time and end_time.
    if "start_time" in false_data.columns and "end_time" in false_data.columns:
        false_data["duration"] = (
            pd.to_datetime(false_data["end_time"], errors="coerce")
            - pd.to_datetime(false_data["start_time"], errors="coerce")
        ).dt.total_seconds()

    # Convert columns to their appropriate types.
    # Ensure start_time and end_time are datetime.
    false_data["start_time"] = pd.to_datetime(false_data["start_time"], errors="coerce")
    false_data["end_time"] = pd.to_datetime(false_data["end_time"], errors="coerce")

    conversion_mapping = {
        "process_execution_id": "int",
        "order_id": "int",
        "part_id": "int",
        "process_id": "int",
        "resource_id": "int",
        "process_type": "int",
        "is_valid": "bool",  # or bool if preferred: false_data["is_valid"] = false_data["is_valid"].astype(bool)
    }
    for col, dtype in conversion_mapping.items():
        if col in false_data.columns:
            false_data.loc[false_data[col].notna(), col] = false_data.loc[
                false_data[col].notna(), col
            ].astype(dtype)

    return false_data

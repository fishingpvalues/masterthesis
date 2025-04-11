import pandas as pd
from upsetplot import UpSet
from matplotlib import pyplot as plt
import matplotlib  # Import matplotlib directly to access rcParams easily
import itertools

# --- Define Feature Sets ---
feature_sets = {
    "Time Model": [
        "duration",
        "sequence_number",
        "hour_of_day_cos",
        "hour_of_day_sin",
        "day_of_week_cos",
        "day_of_week_sin",
        "is_break",
        "is_not_weekday",
    ],
    "Resource Model": ["resource_id", "part_id", "process_id"],
    "Transformation Model": ["part_id", "process_id", "sequence_number"],
    "Transition Model": ["part_id", "resource_id", "sequence_number", "duration"],
    "Process Model": ["process_id", "duration", "sequence_number"],
    "KPI-based": ["throughput", "cycle_time_sec", "lead_time_sec", "setup_time_sec"],
}

# --- Data Preparation ---

# Convert lists to sets for easier operations
feature_sets_sets = {name: set(features) for name, features in feature_sets.items()}

# Find all unique features
all_features = sorted(
    list(set.union(*feature_sets_sets.values()))
)  # Sort for consistent order
print(f"Total unique features: {len(all_features)}\n")
print(f"All Features: {', '.join(all_features)}\n")


# Prepare data for UpSet plot (Boolean Membership DataFrame)
# This DataFrame is key to identifying features per intersection
upset_data = pd.DataFrame(index=all_features)
for name, features in feature_sets_sets.items():
    upset_data[name] = upset_data.index.map(lambda x: x in features)

# Generate the UpSet plot input data (Counts per Intersection)
# The index of this Series represents the intersection combinations
set_names = list(feature_sets.keys())
upset_plot_data = upset_data.groupby(set_names).size()

# Filter out combinations with zero members (optional, but cleaner)
upset_plot_data = upset_plot_data[upset_plot_data > 0]

print("\n--- Data structure for UpSet plot input (Counts per Intersection) ---")
print(upset_plot_data)

# --- Detailed Breakdown: Features per Intersection ---
print("\n--- Features per Specific Intersection ---")
# This section explicitly lists features for each bar in the UpSet plot

intersection_details = {}  # Store details for potential file output

# The index of upset_plot_data is a MultiIndex of booleans
for combo_index, count in upset_plot_data.items():
    # 'combo_index' is a tuple of booleans (True/False) corresponding to set_names
    if count == 0:
        continue  # Skip empty intersections if not already filtered

    # Build a boolean mask to filter the original upset_data DataFrame
    mask = pd.Series(True, index=upset_data.index)  # Start with all True
    combo_sets_present = []
    combo_sets_absent = []

    for i, set_name in enumerate(set_names):
        is_member = combo_index[
            i
        ]  # Boolean: Is the feature in this set for this combo?
        mask &= upset_data[set_name] == is_member
        if is_member:
            combo_sets_present.append(set_name)
        else:
            combo_sets_absent.append(set_name)

    # Get the features (index names) matching this specific combination
    features_in_combo = upset_data[mask].index.tolist()

    # Create a descriptive name for the combination
    if combo_sets_present:
        present_str = " & ".join(combo_sets_present)
        if len(combo_sets_present) == len(set_names):
            combo_desc = f"All Sets ({present_str})"
        # elif not combo_sets_absent: # This case is unlikely if multiple sets exist
        #      combo_desc = f"{present_str} Only (All Sets)" # Simplified logic below
        elif (
            len(combo_sets_present) + len(combo_sets_absent) == len(set_names)
            and combo_sets_absent
        ):
            # More common case: Present in some, absent from others
            combo_desc = f"{present_str} ONLY"
        else:  # Only present in these sets (implies others are absent)
            combo_desc = f"{present_str} ONLY"

    else:
        # This case (no sets present) should have been filtered out by upset_plot_data > 0
        combo_desc = "Error: No sets present but count > 0?"

    print(f"\nCombination: {combo_desc}")
    print(f"  - Represented by Boolean: {combo_index}")
    print(f"  - Feature Count: {count}")
    print(f"  - Features: {', '.join(features_in_combo)}")

    intersection_details[combo_desc] = {
        "boolean_index": combo_index,
        "count": count,
        "features": features_in_combo,
    }

# --- Optionally save details to a file ---
try:
    with open("feature_intersection_details.txt", "w") as f:
        f.write("--- Detailed Feature Intersection Report ---\n\n")
        # Sort items for consistent file output (optional)
        for combo_desc, details in sorted(intersection_details.items()):
            f.write(f"Combination: {combo_desc}\n")
            f.write(f"  - Represented by Boolean: {details['boolean_index']}\n")
            f.write(f"  - Feature Count: {details['count']}\n")
            f.write(f"  - Features: {', '.join(details['features'])}\n\n")
        print(
            "\nDetailed intersection report saved to feature_intersection_details.txt"
        )
except Exception as e:
    print(f"\nCould not save detailed report to file. Error: {e}")


# --- Generate UpSet Plot ---
print("\n--- Generating UpSet Plot ---")
try:
    # --- SET FONT CONFIGURATION ---
    # Ensure 'Times New Roman' is installed on your system and accessible by Matplotlib
    matplotlib.rcParams.update(
        {
            "font.family": [
                "Times New Roman",
                "serif",
            ],  # Use Times New Roman, fallback to serif
            "pdf.fonttype": 42,  # Embed TrueType fonts in PDF for portability
            "ps.fonttype": 42,  # Embed TrueType fonts in PS/EPS for portability
            # 'font.size': 10 # Optionally set base font size
        }
    )
    # ------------------------------------

    # Create the figure AFTER setting rcParams
    plt.figure(figsize=(12, 7))  # Adjusted figure size

    # Create the UpSet plot object
    upset = UpSet(
        upset_plot_data,
        sort_by="cardinality",  # Sort intersection bars by size (desc)
        sort_categories_by="-cardinality",  # Sort set names by total size (desc)
        show_counts=True,  # Show counts above intersection bars
        # min_subset_size=1             # Optionally hide intersections smaller than N
    )

    # Render the plot onto the current figure
    upset.plot()

    # Access the figure object the UpSet plot was drawn on
    fig = plt.gcf()  # Get Current Figure

    # Set title on the figure object using the configured font
    fig.suptitle(
        "Feature Overlap Across SBDT Component Subsets",
        # Matplotlib should use the rcParams font by default
    )

    # Adjust layout AFTER setting the title to prevent overlap
    # rect=[left, bottom, right, top] in figure coordinates
    plt.tight_layout(rect=[0, 0.02, 1, 0.95])

    # Save the plot to files
    plt.savefig("upset.png", dpi=600, bbox_inches="tight")
    plt.savefig("feature_overlap_upset.pdf", bbox_inches="tight")
    print("\nUpSet plot saved as feature_overlap_upset.png/pdf")
    print(
        "Refer to the console output above or 'feature_intersection_details.txt' for the list of features in each bar."
    )

    # Uncomment the line below if you want the plot window to open interactively
    # plt.show()

    # Optional: Reset rcParams if you're making other plots later with default settings
    # matplotlib.rcdefaults()

except Exception as e:
    print(f"\nCould not generate UpSet plot. Error: {e}")
    # Check if the error might be related to finding the font
    if "findfont" in str(e).lower():
        print("---")
        print(
            "Font Error Hint: Matplotlib might not be able to find 'Times New Roman'."
        )
        print(
            "1. Ensure the 'Times New Roman' font is correctly installed on your system."
        )
        print(
            "2. Try rebuilding Matplotlib's font cache (may require deleting cache files, see Matplotlib docs)."
        )
        print(
            "3. Check the exact name Matplotlib recognizes (it can be case-sensitive or require specific naming)."
        )
        # Example check (uncomment to run):
        # from matplotlib.font_manager import findfont, FontProperties
        # try:
        #     print(f"Path found: {findfont(FontProperties(family=['Times New Roman']))}")
        # except ValueError:
        #     print("'Times New Roman' not found by findfont.")
        print("---")
    print(
        "Also ensure 'upsetplot', 'matplotlib', and 'pandas' are installed (`pip install upsetplot matplotlib pandas`)"
    )

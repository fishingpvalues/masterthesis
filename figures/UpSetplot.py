import pandas as pd
from upsetplot import UpSet
from matplotlib import pyplot as plt

feature_sets = {
    "Time": [
        "duration",
        "sequence_number",
        "hour_of_day_cos",
        "hour_of_day_sin",
        "day_of_week_cos",
        "day_of_week_sin",
        "is_break",
        "is_not_weekday",
    ],
    "Resource": [
        "resource_id",
        "part_id",
        "process_id",
    ],
    "Transformation": [
        "part_id",
        "process_id",
        "sequence_number",
    ],
    "Transition": [
        "part_id",
        "resource_id",
        "sequence_number",
        "duration",
    ],
    "Process": [
        "process_id",
        "duration",
        "sequence_number",
    ],
    "KPI": [
        "throughput",
        "cycle_time_sec",
        "lead_time_sec",
        "setup_time_sec",
    ],
}

# Convert lists to sets for easier operations
feature_sets_sets = {name: set(features) for name, features in feature_sets.items()}

# Find all unique features
all_features = set.union(*feature_sets_sets.values())
print(f"Total unique features: {len(all_features)}\n")

# --- Calculate and Print Intersections/Unique Features ---
print("--- Feature Membership ---")

for feature in sorted(list(all_features)):
    members = [
        name for name, features in feature_sets_sets.items() if feature in features
    ]
    print(f"- '{feature}': Present in {', '.join(members)}")

print("\n--- Unique Features per Component ---")
for name, features in feature_sets_sets.items():
    others_union = set.union(*(f for n, f in feature_sets_sets.items() if n != name))
    unique = features - others_union
    if unique:
        print(f"- {name} only: {', '.join(sorted(list(unique)))}")
    else:
        print(f"- {name} only: None")

print("\n--- Notable Intersections ---")
# Example: Features in Time AND Transition
time_transi = feature_sets_sets["Time"].intersection(feature_sets_sets["Transition"])
print(f"- Time & Transition: {time_transi}")

# Example: Features common to Transformation, Transition, Process
transf_transi_proc = (
    feature_sets_sets["Transformation"]
    .intersection(feature_sets_sets["Transition"])
    .intersection(feature_sets_sets["Process"])
)
print(f"- Transformation & Transition & Process: {transf_transi_proc}")
# Add more specific intersection calculations if needed

# --- Prepare data for UpSet plot ---
# We need a format that indicates membership for each feature across all sets
upset_data = pd.DataFrame(index=sorted(list(all_features)))
for name, features in feature_sets_sets.items():
    upset_data[name] = upset_data.index.map(lambda x: x in features)

# Convert boolean to int for UpSet plot aggregation if needed, or use directly
# upset_data = upset_data.astype(int)

# Create the UpSet plot data structure (multi-index Series)
upset_plot_data = upset_data.groupby(list(feature_sets.keys())).size()

print("\nData structure for UpSet plot input:\n", upset_plot_data)

# --- Generate UpSet Plot ---
try:
    plt.figure(figsize=(10, 6))  # Adjust figure size as needed
    upset = UpSet(upset_plot_data, sort_categories_by="cardinality", show_counts=True)
    # You might need to adjust parameters depending on the upsetplot version
    # upset.add_catplot(value='counts', kind='strip', color='blue') # Example catplot
    upset.plot()
    plt.suptitle("Feature Overlap Across SBDT Component Subsets")
    # plt.show() # Display the plot interactively
    plt.savefig("feature_overlap_upset.png", dpi=300)  # Save the plot
    plt.savefig("feature_overlap_upset.pdf")  # Save as PDF
    print("\nUpSet plot saved as feature_overlap_upset.png/pdf")
except Exception as e:
    print(f"\nCould not generate UpSet plot. Error: {e}")
    print(
        "Please ensure 'upsetplot' and 'matplotlib' are installed (`pip install upsetplot matplotlib`)"
    )

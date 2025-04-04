from collections import Counter

import matplotlib.patches as patches  # Import patches for the circle
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import distance

# --- Configuration ---
K = 5  # Number of neighbors to consider
N_POINTS_PER_CLASS = 30
N_CLASSES = 2
OUTLIER_COUNT_CLASS_A = 2
OUTLIER_COUNT_CLASS_B = 1

# --- Generate Synthetic Data ---
np.random.seed(42)  # for reproducibility

# Class A (Blue Circles)
class_A = np.random.randn(N_POINTS_PER_CLASS, 2) * 0.8 + np.array([2, 2])
# Class B (Green Squares)
class_B = np.random.randn(N_POINTS_PER_CLASS, 2) * 0.7 + np.array([6, 6])

# Outliers
outliers_A = np.random.randn(OUTLIER_COUNT_CLASS_A, 2) * 0.5 + np.array(
    [7, 1.5]
)  # Far from main A cluster
outliers_B = np.random.randn(OUTLIER_COUNT_CLASS_B, 2) * 0.5 + np.array(
    [1, 7]
)  # Far from main B cluster

# Combine training data
training_data = np.vstack((class_A, class_B, outliers_A, outliers_B))
labels = (
    ["A"] * N_POINTS_PER_CLASS
    + ["B"] * N_POINTS_PER_CLASS
    + ["A"] * OUTLIER_COUNT_CLASS_A
    + ["B"] * OUTLIER_COUNT_CLASS_B
)

# New data point to classify (Red Star)
# Place it somewhere between the clusters or near outliers for interest
new_point = np.array([[4.5, 4.0]])

# --- KNN Logic ---
# Calculate distances from the new point to all training points
distances = distance.cdist(new_point, training_data, "euclidean")[0]

# Get the indices and distances of the K nearest neighbors
sorted_indices = np.argsort(distances)
nearest_neighbor_indices = sorted_indices[:K]
k_distances = distances[nearest_neighbor_indices]  # Distances to the K neighbors

# Get the labels of the K nearest neighbors
nearest_neighbor_labels = [labels[i] for i in nearest_neighbor_indices]

# Determine the predicted class by majority vote
most_common = Counter(nearest_neighbor_labels).most_common(1)
predicted_class = most_common[0][0] if most_common else "Unknown"

# --- Plotting ---
plt.style.use("seaborn-v0_8-whitegrid")  # Use a clean style
fig, ax = plt.subplots(figsize=(10, 8))

# Plot Class A points
ax.scatter(
    class_A[:, 0],
    class_A[:, 1],
    c="blue",
    marker="o",
    label="Class A Cluster",
    s=60,
    alpha=0.7,
)
# Plot Class B points
ax.scatter(
    class_B[:, 0],
    class_B[:, 1],
    c="green",
    marker="s",
    label="Class B Cluster",
    s=60,
    alpha=0.7,
)

# Plot Outliers
ax.scatter(
    outliers_A[:, 0],
    outliers_A[:, 1],
    c="blue",
    marker="o",
    s=60,
    alpha=0.7,
    edgecolors="red",
    linewidth=1.5,
)
ax.scatter(
    outliers_B[:, 0],
    outliers_B[:, 1],
    c="green",
    marker="s",
    s=60,
    alpha=0.7,
    edgecolors="red",
    linewidth=1.5,
)
# Add a generic outlier label point for the legend (optional, as position defines them)
ax.scatter(
    [],
    [],
    c="gray",
    marker="o",
    s=60,
    edgecolors="red",
    linewidth=1.5,
    label="Outliers (by position)",
)


# Plot the new point
ax.scatter(
    new_point[:, 0],
    new_point[:, 1],
    c="red",
    marker="*",
    s=250,
    label="New Point (to classify)",
    zorder=5,
)

# Highlight the K nearest neighbors
neighbor_points = training_data[nearest_neighbor_indices]
ax.scatter(
    neighbor_points[:, 0],
    neighbor_points[:, 1],
    facecolors="none",
    edgecolors="orange",
    s=200,
    linewidth=2,
    label=f"K={K} Nearest Neighbors",
    zorder=4,
)

# --- ADD CIRCLE AROUND NEW POINT ---
# Radius can be distance to the Kth neighbor
radius_knn = k_distances[
    -1
]  # The Kth distance is the largest among the K smallest distances

# Create the circle patch
highlight_circle = patches.Circle(
    (new_point[0, 0], new_point[0, 1]),
    radius_knn,
    fill=False,
    edgecolor="purple",
    linewidth=2,
    linestyle="--",
    label=f"Radius to Kth Neighbor (K={K})",
    zorder=3,
)  # Add label
# Add the patch to the axes
ax.add_patch(highlight_circle)
# --- END CIRCLE ADDITION ---


# Optionally: draw lines from new point to neighbors
# for i in nearest_neighbor_indices:
#     ax.plot([new_point[0, 0], training_data[i, 0]],
#             [new_point[0, 1], training_data[i, 1]],
#             '--', color='orange', linewidth=0.8, zorder=3)


# --- Customize Appearance ---
ax.set_title(
    f"KNN Concept: Classification based on K={K} Nearest Neighbors\nPredicted Class for New Point: {predicted_class}",
    fontsize=14,
)

# Hide axes and ticks
ax.set_xticks([])
ax.set_yticks([])
# ax.axis('off') # You can use this for a cleaner removal
# Or remove spines individually
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)

# Add legend
# Adjust legend location if needed to avoid overlap
ax.legend(
    loc="lower right", fontsize=10, frameon=True, facecolor="white", framealpha=0.8
)

# Set plot limits slightly padded
all_x = np.concatenate([training_data[:, 0], new_point[:, 0]])
all_y = np.concatenate([training_data[:, 1], new_point[:, 1]])
ax.set_xlim(all_x.min() - 1, all_x.max() + 1)
ax.set_ylim(all_y.min() - 1, all_y.max() + 1)
ax.set_aspect("equal", adjustable="box")  # Ensure circle looks like a circle

plt.tight_layout()
plt.show()

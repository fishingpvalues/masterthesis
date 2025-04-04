import matplotlib.patches as patches
import matplotlib.pyplot as plt

# --- Diagram Configuration ---
fig_width = 8
fig_height = 6

# Colors (approximating the diagram)
box_fill = "lightyellow"  #'#FEFDE2' # Light yellow/cream
gate_fill_sigmoid = "#FFB6C1"  # Light pinkish for Sigmoid (Logistic)
gate_fill_tanh = "#ADD8E6"  # Light blue for Tanh
op_mult_fill = "lightgreen"  #'#C1FFC1' # Light green for multiply
op_add_fill = "lightcoral"  #'#FFC1C1' # Light red/coral for add
line_color = "black"
state_line_width = 2.5  # Thicker line for cell state
arrow_head_width = 0.15
arrow_head_length = 0.25

# --- Create Figure and Axes ---
fig, ax = plt.subplots(figsize=(fig_width, fig_height))
ax.set_aspect("equal")
ax.axis("off")  # Turn off the default axes
ax.set_xlim(-5, 5)
ax.set_ylim(-3.5, 3.5)

# --- Define Key Coordinates ---
# (Adjust these to fine-tune layout)
y_c_path = 2.0  # Y-coordinate for the cell state c(t) path
y_ops_c = 1.2  # Y-coordinate for the ops on the c path (*, +)
y_h_path = -1.5  # Y-coordinate for h(t) output path
y_gates = -1.0  # Y-coordinate for the gate calculation boxes
y_inputs = -2.5  # Y-coordinate for x(t) input arrow start

x_input_h = -4.5  # X-coordinate for h(t-1) input
x_input_c = -4.5  # X-coordinate for c(t-1) input
x_output = 4.5  # X-coordinate for outputs
x_gate_f = -3.0  # X for forget gate calc box
x_gate_g = -1.0  # X for candidate calc box (g)
x_gate_i = 1.0  # X for input gate calc box
x_gate_o = 3.0  # X for output gate calc box

op_radius = 0.3  # Radius for operation circles (*, +)
gate_box_width = 1.2
gate_box_height = 0.6

# --- Draw Main Cell Box (Optional) ---
cell_box = patches.Rectangle(
    (-4, -1.8),
    8,
    4.3,
    linewidth=1.5,
    edgecolor="black",
    facecolor=box_fill,
    zorder=0,
    label="LSTM Cell",
)
ax.add_patch(cell_box)
ax.text(0, -1.6, "LSTM Cell", ha="center", va="top", fontsize=9)

# --- Draw Gate/Calculation Representations ---
# Forget Gate (f_t) - Sigmoid
rect_f = patches.Rectangle(
    (x_gate_f - gate_box_width / 2, y_gates - gate_box_height / 2),
    gate_box_width,
    gate_box_height,
    facecolor=gate_fill_sigmoid,
    edgecolor="black",
    zorder=2,
)
ax.add_patch(rect_f)
ax.text(x_gate_f, y_gates, "FC", ha="center", va="center", fontsize=8, zorder=3)
ax.text(
    x_gate_f,
    y_gates + gate_box_height * 0.7,
    "$f_t$ (σ)",
    ha="center",
    va="bottom",
    fontsize=9,
    zorder=3,
)  # Our notation f_t, indicate sigmoid

# Candidate State (g_t -> c_tilde_t) - Tanh
rect_g = patches.Rectangle(
    (x_gate_g - gate_box_width / 2, y_gates - gate_box_height / 2),
    gate_box_width,
    gate_box_height,
    facecolor=gate_fill_tanh,
    edgecolor="black",
    zorder=2,
)
ax.add_patch(rect_g)
ax.text(x_gate_g, y_gates, "FC", ha="center", va="center", fontsize=8, zorder=3)
ax.text(
    x_gate_g,
    y_gates + gate_box_height * 0.7,
    "$\\tilde{c}_t$ (tanh)",
    ha="center",
    va="bottom",
    fontsize=9,
    zorder=3,
)  # Our notation c_tilde_t, indicate tanh

# Input Gate (i_t) - Sigmoid
rect_i = patches.Rectangle(
    (x_gate_i - gate_box_width / 2, y_gates - gate_box_height / 2),
    gate_box_width,
    gate_box_height,
    facecolor=gate_fill_sigmoid,
    edgecolor="black",
    zorder=2,
)
ax.add_patch(rect_i)
ax.text(x_gate_i, y_gates, "FC", ha="center", va="center", fontsize=8, zorder=3)
ax.text(
    x_gate_i,
    y_gates + gate_box_height * 0.7,
    "$i_t$ (σ)",
    ha="center",
    va="bottom",
    fontsize=9,
    zorder=3,
)  # Our notation i_t, indicate sigmoid

# Output Gate (o_t) - Sigmoid
rect_o = patches.Rectangle(
    (x_gate_o - gate_box_width / 2, y_gates - gate_box_height / 2),
    gate_box_width,
    gate_box_height,
    facecolor=gate_fill_sigmoid,
    edgecolor="black",
    zorder=2,
)
ax.add_patch(rect_o)
ax.text(x_gate_o, y_gates, "FC", ha="center", va="center", fontsize=8, zorder=3)
ax.text(
    x_gate_o,
    y_gates + gate_box_height * 0.7,
    "$o_t$ (σ)",
    ha="center",
    va="bottom",
    fontsize=9,
    zorder=3,
)  # Our notation o_t, indicate sigmoid


# --- Draw Operation Symbols ---
# Forget Gate Multiplication (*)
op_mult_f_pos = (x_gate_f, y_ops_c)
op_mult_f = patches.Circle(
    op_mult_f_pos, op_radius, facecolor=op_mult_fill, edgecolor="black", zorder=2
)
ax.add_patch(op_mult_f)
ax.text(
    op_mult_f_pos[0],
    op_mult_f_pos[1],
    "×",
    ha="center",
    va="center",
    fontsize=12,
    zorder=3,
)  # Using × for element-wise

# Input Gate Multiplication (*)
op_mult_i_pos = (x_gate_i, y_ops_c)
op_mult_i = patches.Circle(
    op_mult_i_pos, op_radius, facecolor=op_mult_fill, edgecolor="black", zorder=2
)
ax.add_patch(op_mult_i)
ax.text(
    op_mult_i_pos[0],
    op_mult_i_pos[1],
    "×",
    ha="center",
    va="center",
    fontsize=12,
    zorder=3,
)

# Cell State Addition (+)
op_add_c_pos = (0, y_ops_c + 0.1)  # Slightly offset from mult ops Y
op_add_c = patches.Circle(
    op_add_c_pos, op_radius, facecolor=op_add_fill, edgecolor="black", zorder=2
)
ax.add_patch(op_add_c)
ax.text(
    op_add_c_pos[0],
    op_add_c_pos[1],
    "+",
    ha="center",
    va="center",
    fontsize=12,
    zorder=3,
)

# Internal Tanh for output path
op_tanh_c_pos = (op_add_c_pos[0], y_h_path + 0.8)
op_tanh_c = patches.Circle(
    op_tanh_c_pos,
    op_radius * 1.1,
    facecolor=gate_fill_tanh,
    edgecolor="black",
    zorder=2,
)
ax.add_patch(op_tanh_c)
ax.text(
    op_tanh_c_pos[0],
    op_tanh_c_pos[1],
    "tanh",
    ha="center",
    va="center",
    fontsize=7,
    zorder=3,
)

# Output Gate Multiplication (*)
op_mult_o_pos = (x_gate_o - 0.5, y_h_path)
op_mult_o = patches.Circle(
    op_mult_o_pos, op_radius, facecolor=op_mult_fill, edgecolor="black", zorder=2
)
ax.add_patch(op_mult_o)
ax.text(
    op_mult_o_pos[0],
    op_mult_o_pos[1],
    "×",
    ha="center",
    va="center",
    fontsize=12,
    zorder=3,
)

# --- Draw Connections / Arrows ---
# Input Arrows
ax.arrow(
    x_input_h,
    y_gates,
    x_gate_f - gate_box_width / 2 - x_input_h - 0.1,
    0,
    head_width=arrow_head_width,
    head_length=arrow_head_length,
    fc=line_color,
    ec=line_color,
    length_includes_head=True,
)
ax.text(x_input_h - 0.2, y_gates, "$h_{t-1}$", ha="right", va="center", fontsize=10)

ax.arrow(
    x_input_c,
    y_c_path,
    op_mult_f_pos[0] - x_input_c - op_radius,
    0,
    head_width=arrow_head_width,
    head_length=arrow_head_length,
    fc=line_color,
    ec=line_color,
    length_includes_head=True,
    lw=state_line_width,
)
ax.text(x_input_c - 0.2, y_c_path, "$c_{t-1}$", ha="right", va="center", fontsize=10)

# Connect x_t to gates (using annotate for simplicity)
ax.annotate(
    "",
    xy=(x_gate_f, y_gates - gate_box_height / 2),
    xytext=(0, y_inputs),
    arrowprops=dict(arrowstyle="->", color=line_color, shrinkB=5),
)
ax.annotate(
    "",
    xy=(x_gate_g, y_gates - gate_box_height / 2),
    xytext=(0, y_inputs),
    arrowprops=dict(arrowstyle="->", color=line_color, shrinkB=5),
)
ax.annotate(
    "",
    xy=(x_gate_i, y_gates - gate_box_height / 2),
    xytext=(0, y_inputs),
    arrowprops=dict(arrowstyle="->", color=line_color, shrinkB=5),
)
ax.annotate(
    "",
    xy=(x_gate_o, y_gates - gate_box_height / 2),
    xytext=(0, y_inputs),
    arrowprops=dict(arrowstyle="->", color=line_color, shrinkB=5),
)
ax.text(0, y_inputs - 0.2, "$x_t$", ha="center", va="top", fontsize=10)

# Connect h_{t-1} to gates
ax.plot(
    [x_input_h, x_gate_o + gate_box_width / 2],
    [y_gates, y_gates],
    color=line_color,
    zorder=1,
)  # Horizontal line from h_t-1
ax.plot(
    [x_gate_f, x_gate_f],
    [y_gates, y_gates - gate_box_height / 2],
    color=line_color,
    zorder=1,
)  # Vertical taps
ax.plot(
    [x_gate_g, x_gate_g],
    [y_gates, y_gates - gate_box_height / 2],
    color=line_color,
    zorder=1,
)
ax.plot(
    [x_gate_i, x_gate_i],
    [y_gates, y_gates - gate_box_height / 2],
    color=line_color,
    zorder=1,
)
ax.plot(
    [x_gate_o, x_gate_o],
    [y_gates, y_gates - gate_box_height / 2],
    color=line_color,
    zorder=1,
)

# Cell state path c(t-1) -> c(t)
ax.annotate(
    "",
    xy=op_mult_f_pos,
    xytext=(x_gate_f, y_gates + gate_box_height * 0.7 + 0.2),  # From f_t label area
    arrowprops=dict(arrowstyle="->", color=line_color, shrinkA=5, shrinkB=5),
)
ax.arrow(
    op_mult_f_pos[0],
    op_mult_f_pos[1],
    op_add_c_pos[0] - op_mult_f_pos[0] - op_radius,
    0,
    head_width=arrow_head_width,
    head_length=arrow_head_length,
    fc=line_color,
    ec=line_color,
    length_includes_head=True,
    lw=state_line_width,
)

ax.annotate(
    "",
    xy=op_mult_i_pos,
    xytext=(x_gate_i, y_gates + gate_box_height * 0.7 + 0.2),  # From i_t label area
    arrowprops=dict(arrowstyle="->", color=line_color, shrinkA=5, shrinkB=5),
)
ax.annotate(
    "",
    xy=op_mult_i_pos,
    xytext=(
        x_gate_g,
        y_gates + gate_box_height * 0.7 + 0.2,
    ),  # From c_tilde_t label area
    arrowprops=dict(arrowstyle="->", color=line_color, shrinkA=5, shrinkB=5),
)
ax.arrow(
    op_mult_i_pos[0],
    op_mult_i_pos[1],
    op_add_c_pos[0] - op_mult_i_pos[0] - op_radius,
    0,
    head_width=arrow_head_width,
    head_length=arrow_head_length,
    fc=line_color,
    ec=line_color,
    length_includes_head=True,
)

ax.arrow(
    op_add_c_pos[0],
    op_add_c_pos[1],
    x_output - op_add_c_pos[0] - 0.1,
    y_c_path - op_add_c_pos[1] - 0.1,  # Diagonal to c_t output pos
    head_width=arrow_head_width,
    head_length=arrow_head_length,
    fc=line_color,
    ec=line_color,
    length_includes_head=True,
    lw=state_line_width,
)
ax.text(x_output + 0.2, y_c_path, "$c_t$", ha="left", va="center", fontsize=10)

# Output path c(t) -> h(t)
ax.plot(
    [op_add_c_pos[0], op_tanh_c_pos[0]],
    [op_add_c_pos[1] + op_radius, op_tanh_c_pos[1] + op_radius * 1.1],
    color=line_color,
    lw=state_line_width,
)  # Tap from '+' output line vertically down
ax.arrow(
    op_tanh_c_pos[0],
    op_tanh_c_pos[1] - op_radius * 1.1,
    0,
    op_mult_o_pos[1] - (op_tanh_c_pos[1] - op_radius * 1.1) + op_radius,
    head_width=arrow_head_width,
    head_length=arrow_head_length,
    fc=line_color,
    ec=line_color,
    length_includes_head=True,
)

ax.annotate(
    "",
    xy=op_mult_o_pos,
    xytext=(x_gate_o, y_gates + gate_box_height * 0.7 + 0.2),  # From o_t label area
    arrowprops=dict(
        arrowstyle="->",
        color=line_color,
        shrinkA=5,
        shrinkB=5,
        connectionstyle="arc3,rad=-0.3",
    ),
)  # Curved

ax.arrow(
    op_mult_o_pos[0],
    op_mult_o_pos[1],
    x_output - op_mult_o_pos[0] - 0.1,
    y_h_path - op_mult_o_pos[1],  # Horizontal to h_t
    head_width=arrow_head_width,
    head_length=arrow_head_length,
    fc=line_color,
    ec=line_color,
    length_includes_head=True,
)
ax.text(x_output + 0.2, y_h_path, "$h_t$", ha="left", va="center", fontsize=10)

# --- Add Descriptive Labels (Optional) ---
ax.text(
    op_mult_f_pos[0],
    op_mult_f_pos[1] + op_radius + 0.1,
    "Forget gate",
    ha="center",
    va="bottom",
    fontsize=8,
    color="gray",
)
ax.text(
    op_mult_i_pos[0],
    op_mult_i_pos[1] + op_radius + 0.1,
    "Input gate",
    ha="center",
    va="bottom",
    fontsize=8,
    color="gray",
)
ax.text(
    op_mult_o_pos[0],
    op_mult_o_pos[1] + op_radius + 0.1,
    "Output gate",
    ha="center",
    va="bottom",
    fontsize=8,
    color="gray",
)

# --- Add Legend (Approximation) ---
# CORRECTED legend_text: Replaced \square with text description
legend_text = (
    "$\\times$: Element-wise mult.\n"
    "+: Addition\n"
    "(Pink Box): FC + Sigmoid (σ)\n"  # Changed \square to text
    "(Blue Box): FC + Tanh\n"  # Changed \square to text
    "$\\bigcirc$ (Blue): Tanh"
)  # \bigcirc is usually supported
ax.text(
    x_output - 0.5,
    -3,
    legend_text,
    fontsize=8,
    ha="right",
    va="top",
    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8),
)
ax.text(
    x_output - 0.5,
    -3,
    legend_text,
    fontsize=8,
    ha="right",
    va="top",
    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8),
)


plt.tight_layout()
plt.show()

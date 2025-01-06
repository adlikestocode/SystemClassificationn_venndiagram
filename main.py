import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Define the sets and their labels
plt.figure(figsize=(10, 8))

# Create a Venn diagram
venn = venn3(
    subsets=(1, 1, 1, 1, 1, 1, 1),  # Sizes of the set intersections
    set_labels=("Time-Invariant", "Causal", "Static")
)

# Set colors for the circles
venn.get_patch_by_id('100').set_color('blue')  # Time-Invariant only
venn.get_patch_by_id('010').set_color('green')  # Causal only
venn.get_patch_by_id('001').set_color('yellow')  # Static only
venn.get_patch_by_id('110').set_color('teal')  # Time-Invariant + Causal
venn.get_patch_by_id('101').set_color('lightblue')  # Time-Invariant + Static
venn.get_patch_by_id('011').set_color('teal')  # Causal + Static
venn.get_patch_by_id('111').set_color('purple')  # All three

# Set labels for individual sections with smaller font size and matching colors
venn.get_label_by_id('100').set_text("Dynamic Systems")
venn.get_label_by_id('100').set_fontsize(8)
venn.get_label_by_id('100').set_color('blue')

venn.get_label_by_id('010').set_text("Causal Dynamic")
venn.get_label_by_id('010').set_fontsize(8)
venn.get_label_by_id('010').set_color('green')

venn.get_label_by_id('001').set_text("Static Systems")
venn.get_label_by_id('001').set_fontsize(8)
venn.get_label_by_id('001').set_color('yellow')

venn.get_label_by_id('110').set_text("TI + Causal")
venn.get_label_by_id('110').set_fontsize(8)
venn.get_label_by_id('110').set_color('teal')

venn.get_label_by_id('101').set_text("TI + Static")
venn.get_label_by_id('101').set_fontsize(8)
venn.get_label_by_id('101').set_color('lightblue')

venn.get_label_by_id('011').set_text("Causal + Static")
venn.get_label_by_id('011').set_fontsize(8)
venn.get_label_by_id('011').set_color('teal')

venn.get_label_by_id('111').set_text("All Properties")
venn.get_label_by_id('111').set_fontsize(8)
venn.get_label_by_id('111').set_color('purple')

# Title and display
plt.title("Euler Diagram of System Properties")
plt.show()

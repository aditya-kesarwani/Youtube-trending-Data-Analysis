import pandas as pd
import matplotlib.pyplot as plt

# Read cleaned Excel dataset
df = pd.read_excel(
    "cleaned_youtube_dataset.xlsx",
    engine="openpyxl"
)

# Figure size
plt.figure(figsize=(12,7))

# Soft gradient colors
colors = [
    "#FF9AA2",
    "#FFB7B2",
    "#FFDAC1",
    "#E2F0CB",
    "#B5EAD7",
    "#C7CEEA",
    "#A0CED9",
    "#FFC8A2",
    "#D5AAFF",
    "#85E3FF"
]

# Area chart
plt.fill_between(
    df["Title"],
    df["Views"],
    color="#B5EAD7",
    alpha=0.7
)

# Line on top
plt.plot(
    df["Title"],
    df["Views"],
    marker="o",
    linewidth=3,
    color="#6A5ACD"
)

# Labels and title
plt.title("YouTube Trending Videos Views Analysis")
plt.xlabel("Video Titles")
plt.ylabel("Views")

# Rotate labels
plt.xticks(rotation=45)

# Grid
plt.grid(True, linestyle="--", alpha=0.5)

# Adjust layout
plt.tight_layout()

# Save graph
plt.savefig("youtube_area_chart.png")

# Show graph
plt.show()
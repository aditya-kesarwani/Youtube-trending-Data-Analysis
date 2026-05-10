import pandas as pd
import numpy as np

# Read CSV dataset
df = pd.read_csv("youtube_trending_dataset.csv")

# Print original dataset
print("Original Dataset:\n")
print(df)

# Check missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

# Fill missing values using average
df["Views"].fillna(df["Views"].mean(), inplace=True)
df["Likes"].fillna(df["Likes"].mean(), inplace=True)
df["Comments"].fillna(df["Comments"].mean(), inplace=True)
df["Duration"].fillna(df["Duration"].mean(), inplace=True)

# Print cleaned dataset
print("\nCleaned Dataset:\n")
print(df)

# NumPy calculations
average_views = np.mean(df["Views"])
maximum_views = np.max(df["Views"])
minimum_views = np.min(df["Views"])

print("\nAverage Views:", average_views)
print("Maximum Views:", maximum_views)
print("Minimum Views:", minimum_views)

# Save cleaned dataset
df.to_csv("cleaned_youtube_dataset.csv", index=False)

print("\nCleaned dataset saved successfully!")
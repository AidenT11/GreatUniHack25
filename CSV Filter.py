import pandas as pd

# Load the original CSV
df = pd.read_csv("old_airports.csv")

# Normalize 'type' column (remove whitespace and lowercase everything)
df['type_clean'] = df['type'].str.strip().str.lower()

# Filter for only large and medium airports
filtered_df = df[df['type_clean'].isin(['large_airport'])]

# Select only the 5 columns you care about
columns_to_keep = ["name", "latitude_deg", "longitude_deg", "iso_country"]
filtered_df = filtered_df[columns_to_keep]

# Save the filtered data to a new CSV
filtered_df.to_csv("airports.csv", index=False)

print(f"Filtered CSV saved as 'airports.csv', {len(filtered_df)} rows included.")
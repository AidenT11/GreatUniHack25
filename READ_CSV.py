import pandas as pd

# Load your CSV
df = pd.read_csv("airports.csv")
i = 0

for country in df['iso_country']:
    if pd.notna(country):
        i+=1
    else:
        print(i, country)
        i+=1
import pandas as pd
import requests
from pathlib import Path

OUTPUT_DIR = Path("data/raw")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("Downloading country metadata from World Bank...")

url = "https://api.worldbank.org/v2/country?format=json&per_page=400"

response = requests.get(url)
response.raise_for_status()

countries = response.json()[1]

rows = []

for country in countries:
    # Ignore aggregates such as "World", "High income", etc.
    if country["region"]["value"] == "Aggregates":
        continue

    rows.append(
        {
            "country_code": country["id"],
            "country_name": country["name"],
            "region": country["region"]["value"],
            "income_group": country["incomeLevel"]["value"],
            "capital_city": country["capitalCity"],
            "longitude": country["longitude"],
            "latitude": country["latitude"],
        }
    )

df = (
    pd.DataFrame(rows)
    .sort_values("country_name")
    .reset_index(drop=True)
)

output_file = OUTPUT_DIR / "countries.csv"
df.to_csv(output_file, index=False)

print(f"Saved {len(df)} countries to {output_file}")
print(df.head())
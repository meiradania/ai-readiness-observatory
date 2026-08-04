from pathlib import Path

import pandas as pd
import pycountry

OUTPUT_DIR = Path("data/raw")
OUTPUT_DIR.mkdir(exist_ok=True)

rows = []

for country in pycountry.countries:
    rows.append(
        {
            "iso2": country.alpha_2,
            "iso3": country.alpha_3,
            "country_name": country.name,
            "numeric_code": country.numeric,
        }
    )

df = (
    pd.DataFrame(rows)
    .sort_values("country_name")
    .reset_index(drop=True)
)

df.to_csv(OUTPUT_DIR / "country_dictionary.csv", index=False)

print(df.head())
print(f"{len(df)} countries exported")
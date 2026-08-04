from pathlib import Path

import pandas as pd
import requests

OUTPUT_DIR = Path("data/raw")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

BASE_URL = "https://api.worldbank.org/v2/country/all/indicator"

INDICATORS = {
    "SL.UEM.TOTL.ZS": "unemployment_rate",
    "IT.NET.USER.ZS": "internet_users",
    "NY.GDP.PCAP.CD": "gdp_per_capita",
    "SE.TER.ENRR": "tertiary_enrollment",
}


def download_indicator(indicator_code: str, column_name: str) -> pd.DataFrame:
    print(f"Downloading {column_name}...")

    url = (
        f"{BASE_URL}/{indicator_code}"
        "?format=json"
        "&per_page=20000"
    )

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()[1]

    rows = []

    for row in data:

        # Ignore regions such as World, Europe, etc.
        if row["countryiso3code"] == "":
            continue

        if row["country"]["value"] == "World":
            continue

        value = row["value"]

        if value is None:
            continue

        rows.append(
            {
                "country_code": row["countryiso3code"],
                "year": int(row["date"]),
                column_name: value,
            }
        )

    return pd.DataFrame(rows)


dfs = []

for indicator, name in INDICATORS.items():
    dfs.append(download_indicator(indicator, name))

labour = dfs[0]

for df in dfs[1:]:
    labour = labour.merge(
        df,
        on=["country_code", "year"],
        how="outer",
    )

labour = labour.sort_values(
    ["country_code", "year"]
)

output = OUTPUT_DIR / "labour_market.csv"

labour.to_csv(
    output,
    index=False,
)

print()
print(f"Saved {len(labour):,} rows")
print(output)
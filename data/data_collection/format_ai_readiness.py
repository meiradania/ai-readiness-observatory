from pathlib import Path

import pandas as pd


INPUT_FILE = Path(
    "data/raw/2025-Government-AI-Readiness-Index-data-1.xlsx"
)

OUTPUT_FILE = Path(
    "data/raw/ai_readiness.csv"
)


def main():

    print("Reading AI readiness dataset...")

    df = pd.read_excel(
        INPUT_FILE,
        sheet_name="Global Rankings",
        usecols="B:D",
        skiprows=1
    )


    print(df.columns.tolist())


    # Rename to standard format
    df = df.rename(
        columns={
            "Country": "country_name",
            "Total Score": "ai_readiness_index",
            "Ranking": "ranking",
        }
    )

    # Add year metadata
    df["year"] = 2025

    df = df[
        [
            "year",
            "country_name",
            "ai_readiness_index",
            "ranking",
        ]
    ]

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"Saved {len(df)} rows to {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()
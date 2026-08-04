# Data

This folder contains the raw data sources used in the AI Readiness Observatory workshop.

## Folder structure
```text
data/
├── raw/
│   ├── ai_readiness_index.xlsx
│   ├── countries.csv
│   └── labour_market.csv
│
├── data_collection/
│   ├── collect_ai_readiness.py
│   ├── collect_countries.py
│   └── collect_labour_market.py
│
└── README.md
```

## Raw data

The `raw/` folder contains the original datasets used as input for the workshop.

These files should not be manually modified. Any cleaning or transformation should happen in the data modelling layer using Python and dbt.

## Data sources

### AI Readiness Index

Source:
Oxford Insights - Government AI Readiness Index

URL: https://oxfordinsights.com/ai-readiness/government-ai-readiness-index-2025/?#download-reports

File:
`raw/ai_readiness_index.xlsx`

The dataset contains country-level AI readiness scores.

The workshop uses the `Global Rankings` sheet.

Columns:

| Column | Description |
|---|---|
| ranking | Global ranking position |
| country | Country name |
| total_score | Overall AI readiness score |

---

### Labour Market

Source:
OECD

File:
`raw/labour_market.csv`

Contains labour market indicators by country and year.

---

### Countries dictionary

File:
`raw/countries.csv`

Contains country metadata used to standardize country identifiers.

Example:

| country | iso2 | iso3 |
|---|---|---|
| Germany | DE | DEU |

This table will be used as a reference dimension during data modelling.

---

## Data collection scripts

The scripts in `data_collection/` reproduce the process of obtaining the source datasets.

Example:

```bash
python data/data_collection/download_labour_narket.py
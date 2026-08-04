# AI Readiness Observatory

A hands-on dbt workshop that demonstrates how to build a modern analytics project using publicly available country-level datasets.

Participants will learn how to transform raw data into a trusted analytics layer by applying data modeling best practices, data quality tests, dimensional modeling, and the dbt Semantic Layer.

---

## Learning Objectives

By the end of this workshop, participants will be able to:

* Create and configure a dbt project
* Load raw data using dbt seeds
* Build staging and mart models
* Apply data quality tests
* Design dimension and fact tables
* Define semantic models and business metrics
* Explore the resulting analytics warehouse using DuckDB

---

## Project Architecture

```text
Raw Data
    │
    ▼
 Seeds
    │
    ▼
 Staging
    │
    ▼
 Marts
    │
    ▼
 Semantic Layer
```

---

## Datasets

The workshop combines publicly available country-level datasets.

| Dataset       | Description                                 |
| ------------- | ------------------------------------------- |
| Countries     | Country reference data (ISO2, ISO3, region) |
| Labour Market | OECD labour market indicators               |
| AI Readiness  | Global AI Readiness Index                   |

The scripts used to prepare the datasets are available in:

```text
data/data_collection/
```

Raw source files are stored in:

```text
data/raw/
```

---

## Repository Structure

```text
.
├── .devcontainer/
├── data/
│   ├── raw/
│   ├── countries.csv
│   ├── labour_market.csv
│   └── ai_readiness.csv
├── data_collection/
│
└── dbt/
    ├── models/
    │   ├── staging/
    │   ├── intermediate/
    │   ├── marts/
    │   └── semantic_models/
    ├── seeds/
    └── dbt_project.yml
```

---

## Workshop Setup

The easiest way to run this workshop is using **GitHub Codespaces**.

1. Fork this repository.
2. Open it in GitHub Codespaces.
3. Wait for the development container to finish building.
4. Open a terminal.

Then run:

```bash
cd dbt

dbt debug
```

This command will check that the setup is working.
---

## Workshop Flow

Each exercise has a corresponding solution branch.

| Exercise | Branch                         | Topics                                |
| -------- | ------------------------------ | ------------------------------------- |
| 0        | `workshop-starter`             | Project setup                         |
| 1        | `dbt-seed-setup`               | Loading seed data into DuckDB         |
| 2        | `transformation-layer`         | Staging tables                        |
| 3        | `data-marts`                   | Dimension and fact tables             |
| 4        | `marts-tested-and-documented`  | Documentation and tests               |
| 5        | `semantic-layer`               | Semantic models and metrics           |

Participants should complete each exercise before comparing their work with the corresponding checkpoint branch.

---

## Useful Commands

Build everything:

```bash
dbt build
```

Run models only:

```bash
dbt run
```

Load seeds:

```bash
dbt seed
```

Run tests:

```bash
dbt test
```

List resources:

```bash
dbt ls
```

Compile SQL:

```bash
dbt compile
```

Generate documentation:

```bash
dbt docs generate
dbt docs serve
```

---

## Technologies

* dbt Core
* DuckDB
* Python
* GitHub Codespaces
* VS Code Dev Containers
* MetricFlow / dbt Semantic Layer

---

## License

This project is intended for educational purposes.

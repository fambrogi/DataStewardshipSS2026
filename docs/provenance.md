# Provenance Documentation

## Purpose

This document describes the provenance of the relational database created for WP2/T2.1 of the Data Stewardship SS2026 assignment.

The goal of this provenance documentation is to clearly describe:

- where the data originated,
- who originally created and published the data,
- which transformations were performed,
- which new artefacts were created,
- and which parts were created by the student group.

This supports reproducibility, traceability, transparency, and FAIR reuse.

---

# 1. Original Dataset

## Dataset title

Concentrations of major ions in wet precipitation samples in Austria

## Original creators

- Peter Redl
- Thomas Steinkogler
- Anne Kasper-Giebl

## Original repository

TU Wien Research Data Repository

## Original DOI

https://doi.org/10.48436/b0g4h-rv840

## Original files used

- `precipitationdata.csv`
- `stationcoordinates.csv`

## Original data type

Environmental precipitation chemistry measurements collected at monitoring stations in Austria.

## Original data characteristics

The dataset contains:

- precipitation amount,
- conductivity,
- pH values,
- ion concentrations,
- Pb concentrations,
- Cd concentrations,
- quality flags,
- station coordinates,
- temporal sampling information.

---

# 2. Student Group Contribution

The student group did NOT create the original precipitation measurements.

The student group contribution consists of:

- restructuring the original CSV files,
- designing a relational schema in Third Normal Form (3NF),
- creating SQL CREATE statements,
- generating an ER diagram,
- creating DBRepo tables through the REST API,
- documenting metadata,
- documenting provenance,
- preparing the data infrastructure for the machine learning workflow.

The work was performed as part of the Data Stewardship SS2026 course assignment.

---

# 3. Transformation Workflow

The following transformations were applied to the original source data.

## Step 1 — Load source CSV files

The original CSV files were loaded into Python using pandas.

Files:

- `precipitationdata.csv`
- `stationcoordinates.csv`

---

## Step 2 — Extract station information

Station information was separated from the original precipitation table.

A dedicated relational table named `stations` was created.

The table stores:

- station identifiers,
- station codes,
- latitude,
- longitude.

An internal primary key `station_id` was created.

---

## Step 3 — Create precipitation_measurements table

The precipitation chemistry data were transformed into a relational table named `precipitation_measurements`.

The original station names were replaced with `station_id` foreign keys.

Additional internal identifiers:

- `measurement_id`

were generated.

---

## Step 4 — Preserve quality flags

Quality flag columns from the original dataset were preserved in the relational schema.

Examples:

- `NS_flag`
- `Pb_flag`
- `Cd_flag`

These flags remain associated with their corresponding measurements.

---

## Step 5 — Create measurement_variables table

A metadata table named `measurement_variables` was created.

This table documents:

- variable codes,
- human-readable labels,
- units of measurement.

This improves interpretability and reuse of the database.

---

## Step 6 — Generate SQL schema

SQL CREATE statements were generated and saved to:

`sql/create_tables.sql`

---

## Step 7 — Generate ER diagram

An entity–relationship diagram describing the relational schema was generated and saved to:

`outputs/er_diagram.png`

---

## Step 8 — Create DBRepo tables

The relational tables were uploaded to DBRepo using the DBRepo REST API from a Jupyter notebook.

The following tables were created:

- `stations`
- `precipitation_measurements`
- `measurement_variables`

Descriptive metadata were added during DBRepo table creation.

---

# 4. Derived Artefacts

The following artefacts were created by the student group.

| Artefact | Description |
|---|---|
| `stations` table | Relational station metadata |
| `precipitation_measurements` table | Relational chemistry measurements |
| `measurement_variables` table | Variable/unit documentation |
| `create_tables.sql` | SQL schema |
| `er_diagram.png` | ER diagram |
| `dbrepo_schema_creation.ipynb` | DBRepo workflow notebook |
| `data_dictionary.md` | Column and variable documentation |
| `provenance.md` | Provenance documentation |

---

# 5. License and Rights

The student group does not claim ownership of the original environmental measurements.

The original creators, repository, and rights holders remain associated with the original dataset.

The relational DBRepo representation inherits the reuse conditions of the original dataset license.

The license must be verified directly from the original DOI landing page before final submission.

---

# 6. Reproducibility Information

The relational schema creation process can be reproduced using:

- Python
- pandas
- Jupyter Notebook
- DBRepo REST API

Main workflow notebook:

`notebooks/dbrepo_schema_creation.ipynb`

Supporting files:

- `sql/create_tables.sql`
- `outputs/er_diagram.png`
- `docs/data_dictionary.md`

---
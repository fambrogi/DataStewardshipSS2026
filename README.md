# Prediction of Heavy Metal Concentrations (Pb, Cd) in Precipitation Using Machine Learning

Data Stewardship SS2026 — FAIR and Reproducible Machine Learning Experiment

---

## Project Overview

This repository contains a machine learning experiment developed within a Data Stewardship and FAIR data management framework.

The project investigates the prediction of missing heavy metal concentrations in precipitation chemistry datasets collected at Austrian monitoring stations.

Specifically, the experiment focuses on predicting:

* Lead concentration (`Pb`)
* Cadmium concentration (`Cd`)

using environmental precipitation chemistry measurements and machine learning models.

The repository also includes the relational DBRepo infrastructure developed for WP2/T2.1 of the course assignment.

---

## Authors

* Federico Ambrogi — [01449911@student.tuwien.ac.at](mailto:01449911@student.tuwien.ac.at)
* Puthenpurayil Biju Vijayalakshmi
* Saad Rashidul Amin
* Farooq Mian Azan

---

## Objectives

Two machine learning approaches are implemented and compared.

### 1. Sequential Prediction

* Predict Pb using available environmental variables
* Use predicted Pb values to predict Cd

### 2. Multi-output Prediction

* Predict Pb and Cd simultaneously using a single model

---

## Data Source

The experiment reuses the dataset:

**Concentrations of major ions in wet precipitation samples in Austria**

Original repository:
TU Wien Research Data Repository

Original DOI:
https://doi.org/10.48436/b0g4h-rv840

The dataset includes:

* precipitation chemistry measurements,
* ion concentrations,
* pH values,
* conductivity,
* Pb and Cd concentrations,
* quality flags,
* station metadata.

The student group did not create the original precipitation measurements.
The repository restructures and documents the data for FAIR and reproducible reuse within the course assignment.

---

## Repository Structure

```text
DataStewardshipSS2026/
│
├── data/
│   ├── precipitationdata.csv
│   ├── stationcoordinates.csv
│   └── README.md
│
├── docs/
│   ├── HeavyMetal_Precipitation_Project.pdf
│   ├── data_dictionary.md
│   ├── provenance.md
│   └── README.md
│
├── notebooks/
│   ├── dbrepo_schema_creation.ipynb
│   └── predict_heavymetal_precipitation.ipynb
│
├── outputs/
│   ├── diagrams/
│   │   └── er_diagram.png
│   │
│   ├── figures/
│   │   ├── fig_cd_prediction.png
│   │   ├── fig_feature_importance.png
│   │   └── fig_pb_prediction.png
│   │
│   └── models/
│       ├── model_cd_randomforest.pkl
│       └── model_multi_randomforest.pkl
│
├── sql/
│   └── create_tables.sql
│
├── src/
│   ├── evaluation.py
│   ├── models.py
│   ├── preprocessing.py
│   └── utils.py
│
├── .env
├── .gitignore
├── __init__.py
├── conda_env
└── README.md
```

---

## Main Components

### `notebooks/predict_heavymetal_precipitation.ipynb`

Main machine learning workflow notebook containing:

* preprocessing,
* train/validation/test splitting,
* model training,
* evaluation,
* prediction generation,
* visualization generation.

---

### `notebooks/dbrepo_schema_creation.ipynb`

WP2/T2.1 notebook implementing:

* relational schema design,
* Third Normal Form (3NF) restructuring,
* SQL schema generation,
* ER diagram generation,
* DBRepo table creation through the REST API,
* metadata documentation,
* provenance-aware publication.

---

### `docs/data_dictionary.md`

Documents:

* all relational tables,
* column meanings,
* units,
* variable descriptions,
* quality flag information.

---

### `docs/provenance.md`

Documents:

* original dataset source,
* creators and DOI,
* transformation workflow,
* generated artefacts,
* DBRepo publication process,
* reproducibility information.

---

## Running the Experiment

To run the experiment:

1. Open Jupyter Lab or Jupyter Notebook
2. Open:

```text
notebooks/predict_heavymetal_precipitation.ipynb
```

3. Execute the notebook cells sequentially.

---

## Environment

The conda environment configuration is provided in:

```text
conda_env
```

This environment contains the required Python dependencies for reproducing the experiment.

---

## Generated Outputs

### Figures

Generated plots are stored in:

```text
outputs/figures/
```

Examples include:

* prediction comparison plots,
* feature importance plots,
* evaluation visualizations.

---

### Trained Models

Serialized trained models are stored in:

```text
outputs/models/
```

---

### Database Infrastructure Outputs

Database-related outputs are stored in:

```text
outputs/diagrams/
sql/
```

including:

* ER diagrams,
* SQL CREATE statements.

---

## FAIR and Stewardship Documentation

### Data Dictionary

The relational schema documentation is available in:

```text
docs/data_dictionary.md
```

---

### Provenance Documentation

Detailed provenance information is available in:

```text
docs/provenance.md
```

This includes:

* original dataset provenance,
* transformation workflow,
* DBRepo publication steps,
* student group contributions,
* reproducibility information.

---
## Licences

This project has three different types of artefacts and each one has its own licence. They are not the same so it is important to consider them separately.

### Input data

The source dataset "Concentrations of major ions in wet precipitation samples in Austria" is published under **Creative Commons Attribution NonCommercial ShareAlike 4.0 International (CC BY-NC-SA 4.0)** by the original creators Peter Redl, Thomas Steinkogler, and Anne Kasper-Giebl.

DOI: https://doi.org/10.48436/b0g4h-rv840

Our use of this dataset is permitted under this licence since it is strictly for non-commercial academic research. Two things to note from this licence: the NonCommercial clause means neither this project nor its outputs can be used for commercial purposes, and the ShareAlike clause means any derived datasets we produce must be released under the same CC BY-NC-SA 4.0 licence.

### Software and code

All code in this repository is released under the **MIT licence**. See the [LICENSE](LICENSE) file for the full text.

MIT was chosen because it is simple and permissive, and it lets anyone use, modify and share the code freely. It is compatible with the CC BY-NC-SA 4.0 input data licence because the code is an independent software artefact and not a derived work of the data itself. Anyone who runs this code on the same dataset still needs to respect the CC BY-NC-SA 4.0 terms of the original data.

### Output data

The outputs of this project including the trained models, prediction results, evaluation figures and confusion matrices are released under **Creative Commons Attribution NonCommercial ShareAlike 4.0 International (CC BY-NC-SA 4.0)**.

Since the input dataset has a ShareAlike clause, any derived works need to carry the same licence. The output data is derived from that source so CC BY-NC-SA 4.0 applies here as well. This licence is also stated in all deposit records in the TU Wien Research Data Repository.

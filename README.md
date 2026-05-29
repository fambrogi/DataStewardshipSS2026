# Prediction of Heavy Metal Concentrations (Pb, Cd) in Precipitation Using Machine Learning

[![DOI](https://zenodo.org/badge/1228036424.svg)](https://doi.org/10.5281/zenodo.20423764)

### Authors

| Family name        | Name          | Student Id | ORCID               |
|--------------------|---------------|------------|---------------------|
| Ambrogi            | Federico      | 01449911   | 0000-0002-9486-0444 |
| Puthenpurayil Biju | Vijayalakshmi | 12551187   | 0009-0000-1739-2336 |
| Saad               | Rashidul Amin | 12410035   | 0009-0004-0529-5546 |
| Mian Azan          | Farooq        | 12433773   | 0009-0006-7973-2483 |

---

## Project Summary

This repository contains a machine learning experiment developed within a *Data Stewardship and FAIR data management* framework.

The project predicts the concentrations of toxic heavy metal, 
* Lead concentration (`Pb`)
* Cadmium concentration (`Cd`)

using chemistry datasets, collected at Austrian monitoring stations.

Two machine learning approaches are implemented and compared.

**1. Sequential Prediction**
Predict Pb using available environmental variables, in a sequential fashio: first the Pb values are extracted, and then the results are used to predict the Cd precipitation values
**2. Multi-output Prediction**
Predict Pb and Cd simultaneously using a single ML model 

---

## FAIR principles

This project was developed following FAIR (Findable, Accessible, Interoperable, and Reusable) data management principles and reproducible research practices.  To support FAIR compliance, the project incorporates:

- structured metadata documentation,
- explicit variable and unit definitions,
- reusable database retrieval interfaces,
- version-controlled source code
- machine learning model preservation and distribution
- clear data processing pipelines, analytical and validation procedures
- licensing for reuse and redistribution.

## Data Source

The experiment reuses the dataset **Concentrations of major ions in wet precipitation samples in Austria**
from the *TU Wien Research Data Repository*

DOI: https://doi.org/10.48436/b0g4h-rv840

The dataset includes:
* precipitation chemistry measurements,
* ion concentrations,
* pH values,
* conductivity,
* Pb and Cd concentrations,
* quality flags,
* station metadata.

The dataset includes two files: 
**stationcoordinates.csv**: contains precipitation data including chemicals, ph, conductivity (size: 1.2 MB)
**stationcoordinates.csv**: contains metadata of the observation stations (size: < 1 MB)

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
│   └── README.md
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
│   │   ├── model_cd_randomforest.pkl
│   │   ├── model_multi_randomforest.pkl
│   │
│   ├── metadata/
│   │   ├── FAIRML_model_cd.md
│   │   ├── FAIRML_model_multi.md
│   │   └── a
│   │   └── a
│   │   └── a
│   │   └── a
│   │
│   ├── sql/
│   ├── create_views.sql/
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

Trained models are stored in th eformat of pickle files in:

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


[!NOTE] 
The SQL commands are not used directly for the creation of the instance dataset on the TU WIEN DB Repsitory
 
---

## FAIR and Stewardship Documentation
In line with FAIR principles,
Under
```text
outputs/metadata/
```
we stored Croissant, CodeMeta, RO-Crate, and FAIR4ML metadata files were used to improve the interoperability, reproducibility, discoverability, and long-term reusability of the dataset, software, workflows, and machine learning models by providing standardized machine-readable metadata.

Additionally, we created explicitly a table in "data/units.csv" which reports the URl of the units describing the physical measurement used for experiment, mapping to the ontology concepts of the  SI Digital Framework  http://si-digital-framework.org/ , which provides standardized representations of SI (System of Units).

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


# Prediction of Heavy Metal Concentrations (Pb, Cd) in Precipitation Using Machine Learning

Data Stewardship SS2026 Implementation of a fully reproducible ML Experiment

This repository contains a machine learning experiment developed within a Data Stewardship framework, aiming to predict missing environmental variables in precipitation chemistry datasets.

Specifically, the project focuses on estimating concentrations of Lead (Pb) and Cadmium (Cd), which are not consistently measured across all monitoring stations due to lack of appropriate sensors, which constitute hazarduous pollutants.


### Authors:

Ambrogi Federico , 01449911@student.tuwien.ac.at

Puthenpurayil Biju Vijayalakshmi

Saad Rashidul Amin

Farooq Mian Azan


## Objectives

Two machine learning approaches are implemented and compared:


**1.Sequential Prediction**

Predict Pb using available features

Use predicted Pb to predict Cd


**2. Multi-output Prediction**

Predict Pb and Cd simultaneously using a single model


## Data Source

The dataset is publicly available from the TU Wien Research Data Repository

It includes:

- precipitation chemistry variables
- heavy metal concentrations (*Pb*, *Cd*)
- quality flags indicating data validity

For a full documentation, please refer to the project overview in *doc*


## Run
To run the experiment, open a python jupyter lab and run the notebook in

*notebooks/predict_heavymetal_precipitation.ipynb*


The file 

*conda_env.yaml* 

contains the anaconda enviromental variables for the reproduction of the experiment.


## Output
- Plots will be created inside the *output/figures* directory
- Models will be sotred inside the *output/models* directory


### File organisation

Here an overview of the structure of the project folder organization

```
project_root/
├── data/
│   ├── precipitation.csv
│   ├── stationcoordinates.csv
│
├── src/
│   ├── preprocessing.py
│   ├── models.py
│   ├── evaluation.py
│
├── outputs/
│   ├── figures/
│   ├── models/
│
├── notebooks/
│   └── predict_heavymetal_precipitation.ipynb  
|
├── conda_env.yaml
```
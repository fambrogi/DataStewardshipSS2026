# Model Card

## Model Overview

This repository contains machine learning models developed for the prediction of heavy metal concentrations in precipitation samples collected across Austria.

The models were trained using environmental precipitation chemistry variables including conductivity, pH, ion concentrations, and precipitation measurements.

The experiment focuses on predicting Lead (Pb) and Cadmium (Cd) concentrations using Random Forest regression approaches implemented in Python with scikit-learn.

---

## Authors

| Name                             | Role | ORCID                                 |
| -------------------------------- | ---- | ------------------------------------- |
| Saad Rashidul Amin               | A    | https://orcid.org/0009-0004-0529-5546 |
| Puthenpurayil Biju Vijayalakshmi | B    | https://orcid.org/0009-0000-1739-2336 |
| Federico Ambrogi                 | C    | https://orcid.org/0000-0002-9486-0444 |
| Farooq Mian Azan                 | D    | https://orcid.org/0009-0006-7973-2483 |

---

## Model Artifacts

### model_cd_randomforest.pkl

Type: RandomForestRegressor  
Framework: scikit-learn  
Task: Regression  
Target variable: Cd concentration

This model predicts Cadmium concentration using environmental precipitation chemistry measurements together with predicted Pb values generated in the sequential workflow.

The model is implemented inside a scikit-learn pipeline including mean-value imputation and Random Forest regression.

The model artifact is stored in:

`outputs/models/model_cd_randomforest.pkl`

---

### model_multi_randomforest.pkl

Type: Multi-output RandomForestRegressor  
Framework: scikit-learn  
Task: Multi-output regression  
Target variables: Pb and Cd concentrations

This model simultaneously predicts Pb and Cd concentrations using the environmental variables available in the precipitation chemistry dataset.

The multi-output workflow was implemented to compare joint prediction against the sequential prediction strategy.

The model artifact is stored in:

`outputs/models/model_multi_randomforest.pkl`

---

## Training Data

The models were trained using the dataset:

"Concentrations of major ions in wet precipitation samples in Austria"

Original DOI:  
https://doi.org/10.48436/b0g4h-rv840

The dataset contains precipitation chemistry measurements collected across Austrian monitoring stations, including ion concentrations, conductivity, precipitation amount, pH values, and heavy metal concentrations.

The student group did not generate the original measurements. The dataset was reused and restructured for FAIR and reproducible machine learning experimentation.

The original dataset is distributed under the license:

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

---

## Evaluation Results

| Model                       | RMSE                | MAE                 |
| --------------------------- | ------------------- | ------------------- |
| Pb Random Forest            | 0.23645176053042874 | 0.07070812127761528 |
| Cd Sequential Random Forest | 0.14199312508423387 | 0.04678229361582522 |
| Multi-output Random Forest  | 0.12941772556729142 | 0.04250304511045665 |

The evaluation was performed using held-out test datasets.

Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE) were used because the experiment addresses a regression task rather than classification.

The generated visualizations and evaluation outputs are stored in the `outputs/figures/` directory.

---

## Intended Use

The models are intended for educational and research purposes within the FAIR Data Science and Data Stewardship course.

The experiment demonstrates reproducible machine learning workflows, metadata management, FAIR documentation practices, and research data publication techniques.

The models are not intended for operational environmental monitoring or policy decision-making.

---

## Out-of-Scope Use

The models should not be used for environmental risk assessment, public safety decisions, or scientific conclusions regarding pollution levels.

The models were developed within a course exercise and were not validated for production deployment.

The experiment focuses on FAIRness, reproducibility, and stewardship practices rather than optimized predictive performance.

---

## Limitations

The dataset contains missing values and incomplete heavy metal measurements for several monitoring stations.

The experiment uses relatively simple preprocessing and does not incorporate advanced feature engineering or uncertainty estimation.

The prediction quality may vary significantly depending on station coverage and temporal variability in the environmental measurements.

---

## Ethical Considerations

The dataset does not contain personal or sensitive human data.

The experiment uses publicly available environmental monitoring data distributed under an open license.

The project aims to support transparent and reproducible scientific workflows aligned with FAIR data principles.

---

## Related Resources

GitHub Repository:  
https://github.com/fambrogi/DataStewardshipSS2026

DBRepo Database:  
https://test.dbrepo.tuwien.ac.at/database/bfa4385b-54a9-4ae3-b4f4-cb503d7bb016/info

Zenodo DOI:  
https://doi.org/10.5281/zenodo.20423764

TUWRD Model Deposit DOI:  
https://doi.org/10.70124/rwg1b-kfb59

TUWRD Generated Data Deposit DOI:  
https://doi.org/10.70124/kcmvz-fkw96

---

## License

The software components and trained model artefacts of this repository are distributed under the MIT License.

Copyright (c) 2026 Federico Ambrogi, Vijayalakshmi Puthenpurayil Biju, Saad Rashidul Amin, Farooq Mian Azan

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files to deal in the Software without restriction, subject to the conditions defined in the repository LICENSE file.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

The reused precipitation dataset remains subject to its original Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license.

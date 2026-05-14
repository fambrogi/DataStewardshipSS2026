# Data Dictionary

This data dictionary documents the relational DBRepo schema created for WP2/T2.1 from the original precipitation chemistry dataset.

Original dataset: Concentrations of major ions in wet precipitation samples in Austria  
Original creators: Peter Redl, Thomas Steinkogler, Anne Kasper-Giebl  
Original DOI: https://doi.org/10.48436/b0g4h-rv840  
Source files: `precipitationdata.csv`, `stationcoordinates.csv`

The student group did not create the original measurements. The group only restructured the CSV data into a relational DBRepo schema.

---

## Table: stations

Purpose: Stores information about precipitation monitoring stations.

| Column | Meaning | Type | Unit | Source / Notes |
|---|---|---|---|---|
| station_id | Internal station identifier | integer | none | Created during relational restructuring |
| station_code | Original station/location code | text | none | Derived from `Ort` in source files |
| latitude | Geographic latitude of the station | float | decimal degrees | Derived from `Lat` |
| longitude | Geographic longitude of the station | float | decimal degrees | Derived from `Long` |

---

## Table: precipitation_measurements

Purpose: Stores one precipitation chemistry measurement per sample date and station.

| Column | Meaning | Type | Unit | Source / Notes |
|---|---|---|---|---|
| measurement_id | Internal measurement identifier | integer | none | Created during relational restructuring |
| station_id | Link to the station where the sample was collected | integer | none | Foreign key to `stations.station_id` |
| sample_date | Date of precipitation sample | date/text | ISO date | Derived from `Datum` |
| NS | Precipitation amount | float | mm | Original variable |
| NS_flag | Quality flag for NS | float/integer | none | Original quality flag |
| LF | Conductivity | float | µS/cm | Original variable |
| LF_flag | Quality flag for LF | float/integer | none | Original quality flag |
| pH | Acidity/basicity value | float | dimensionless | Original variable |
| pH_flag | Quality flag for pH | float/integer | none | Original quality flag |
| NH4 | Ammonium concentration | float | mg/L | Original variable |
| NH4_flag | Quality flag for NH4 | float/integer | none | Original quality flag |
| Na | Sodium concentration | float | mg/L | Original variable |
| Na_flag | Quality flag for Na | float/integer | none | Original quality flag |
| K | Potassium concentration | float | mg/L | Original variable |
| K_flag | Quality flag for K | float/integer | none | Original quality flag |
| Ca | Calcium concentration | float | mg/L | Original variable |
| Ca_flag | Quality flag for Ca | float/integer | none | Original quality flag |
| Mg | Magnesium concentration | float | mg/L | Original variable |
| Mg_flag | Quality flag for Mg | float/integer | none | Original quality flag |
| Cl | Chloride concentration | float | mg/L | Original variable |
| Cl_flag | Quality flag for Cl | float/integer | none | Original quality flag |
| NO3 | Nitrate concentration | float | mg/L | Original variable |
| NO3_flag | Quality flag for NO3 | float/integer | none | Original quality flag |
| SO4 | Sulfate concentration | float | mg/L | Original variable |
| SO4_flag | Quality flag for SO4 | float/integer | none | Original quality flag |
| Pb | Lead concentration | float | µg/L | Target variable for ML prediction |
| Pb_flag | Quality flag for Pb | float/integer | none | Original quality flag |
| Cd | Cadmium concentration | float | µg/L | Target variable for ML prediction |
| Cd_flag | Quality flag for Cd | float/integer | none | Original quality flag |

---

## Table: measurement_variables

Purpose: Documents the meaning and unit of each scientific measurement variable.

| Column | Meaning | Type | Unit | Source / Notes |
|---|---|---|---|---|
| variable_id | Internal variable identifier | integer | none | Created during restructuring |
| variable_code | Short variable name used in the measurement table | text | none | Example: `Pb`, `Cd`, `pH` |
| label | Human-readable variable description | text | none | Example: Lead concentration |
| unit | Measurement unit | text | varies | Example: µg/L, mg/L, mm |

---

## Quality flags

The original dataset includes quality flag columns for measured variables. These flags are preserved in the relational schema because they are part of the original data quality information.

The exact interpretation of flag values should be checked against the original dataset documentation before analysis.
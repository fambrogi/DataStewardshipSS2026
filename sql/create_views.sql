-- View 1:
-- Clean ML-ready precipitation data with station information

CREATE VIEW ml_precipitation_features AS
SELECT
    pm.measurement_id,
    s.station_code AS Ort,
    pm.sample_date AS Datum,

    pm.NS,
    pm.LF,
    pm.pH,
    pm.NH4,
    pm.Na,
    pm.K,
    pm.Ca,
    pm.Mg,
    pm.Cl,
    pm.NO3,
    pm.SO4,

    pm.Pb,
    pm.Cd,

    s.latitude,
    s.longitude

FROM precipitation_measurements pm
JOIN stations s
ON pm.station_id = s.station_id
WHERE
    pm.NS_flag = 1
    AND pm.LF_flag = 1
    AND pm.pH_flag = 1
    AND pm.NH4_flag = 1
    AND pm.Na_flag = 1
    AND pm.K_flag = 1
    AND pm.Ca_flag = 1
    AND pm.Mg_flag = 1
    AND pm.Cl_flag = 1
    AND pm.NO3_flag = 1
    AND pm.SO4_flag = 1;



-- View 2:
-- Training-ready records for Pb prediction

CREATE VIEW pb_prediction_dataset AS
SELECT *
FROM ml_precipitation_features
WHERE Pb IS NOT NULL;



-- View 3:
-- Training-ready records for Cd prediction

CREATE VIEW cd_prediction_dataset AS
SELECT *
FROM ml_precipitation_features
WHERE Cd IS NOT NULL;
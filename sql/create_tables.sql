
CREATE TABLE stations (
    station_id INTEGER PRIMARY KEY,
    station_code VARCHAR(10) NOT NULL UNIQUE,
    latitude DOUBLE,
    longitude DOUBLE
);

CREATE TABLE measurement_variables (
    variable_id INTEGER PRIMARY KEY,
    variable_code VARCHAR(20) NOT NULL UNIQUE,
    label VARCHAR(255) NOT NULL,
    unit VARCHAR(50) NOT NULL
);

CREATE TABLE precipitation_measurements (
    measurement_id INTEGER PRIMARY KEY,
    station_id INTEGER NOT NULL,
    sample_date DATE NOT NULL,
    NS DOUBLE,
    NS_flag DOUBLE,
    LF DOUBLE,
    LF_flag DOUBLE,
    pH DOUBLE,
    pH_flag DOUBLE,
    NH4 DOUBLE,
    NH4_flag DOUBLE,
    Na DOUBLE,
    Na_flag DOUBLE,
    K DOUBLE,
    K_flag DOUBLE,
    Ca DOUBLE,
    Ca_flag DOUBLE,
    Mg DOUBLE,
    Mg_flag DOUBLE,
    Cl DOUBLE,
    Cl_flag DOUBLE,
    NO3 DOUBLE,
    NO3_flag DOUBLE,
    SO4 DOUBLE,
    SO4_flag DOUBLE,
    Pb DOUBLE,
    Pb_flag DOUBLE,
    Cd DOUBLE,
    Cd_flag DOUBLE,
    FOREIGN KEY (station_id) REFERENCES stations(station_id)
);

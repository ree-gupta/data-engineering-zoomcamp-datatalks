--Create external table
CREATE OR REPLACE EXTERNAL TABLE `lively-citizen-412110.nytaxi.external_green_tripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://lively-citizen-412110-terra-bucket-homework-3/green/2022/green_tripdata_2022-*.parquet']
);

-- Create a non partitioned table from external table
CREATE OR REPLACE TABLE lively-citizen-412110.nytaxi.green_tripdata_non_partitioned AS
SELECT * FROM lively-citizen-412110.nytaxi.external_green_tripdata;


-- Count the number of records for 2022 Green taxi data external
SELECT count(*) FROM `lively-citizen-412110.nytaxi.external_green_tripdata`;

-- Count the number of records for 2022 Green taxi data on BigQuery
SELECT count(*) FROM `lively-citizen-412110.nytaxi.green_tripdata_non_partitioned`;


-- Scanning for distinct PULocationIDs for 2022 Green taxi data external
SELECT DISTINCT(PULocationID) FROM `lively-citizen-412110.nytaxi.external_green_tripdata`;

-- Scanning for distinct PULocationIDs for 2022 Green taxi data on BigQuery
SELECT DISTINCT(PULocationID) FROM `lively-citizen-412110.nytaxi.green_tripdata_non_partitioned`;

-- Scanning for total fare amount 0 for 2022 Green taxi data external
SELECT count(*) FROM `lively-citizen-412110.nytaxi.external_green_tripdata`
WHERE fare_amount = 0;

-- Create a partitioned table from external table
CREATE OR REPLACE TABLE `lively-citizen-412110.nytaxi.greentripdata_partitioned_clustered`
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PUlocationID
AS
SELECT * FROM `lively-citizen-412110.nytaxi.external_green_tripdata`;

-- Query for unpartiontined table
SELECT DISTINCT(PULocationID)
FROM `lively-citizen-412110.nytaxi.green_tripdata_non_partitioned`
WHERE lpep_pickup_datetime BETWEEN '2022-06-01' AND '2022-06-30';


-- Query for partitioned and clustered table
SELECT DISTINCT(PULocationID)
FROM `lively-citizen-412110.nytaxi.greentripdata_partitioned_clustered`
WHERE lpep_pickup_datetime BETWEEN '2022-06-01' AND '2022-06-30';
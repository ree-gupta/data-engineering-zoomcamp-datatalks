

### Question 1

```sql
CREATE MATERIALIZED VIEW trip_stats AS
SELECT 
    pu_loc.Zone AS start_zone, 
    do_loc.Zone AS end_zone, 
    AVG(EXTRACT(EPOCH FROM (td.tpep_dropoff_datetime - td.tpep_pickup_datetime))) AS average_trip_time, 
    MIN(EXTRACT(EPOCH FROM (td.tpep_dropoff_datetime - td.tpep_pickup_datetime))) AS min_trip_time, 
    MAX(EXTRACT(EPOCH FROM (td.tpep_dropoff_datetime - td.tpep_pickup_datetime))) AS max_trip_time
FROM 
    trip_data td
JOIN 
    taxi_zone pu_loc ON td.PULocationID = pu_loc.location_id
JOIN 
    taxi_zone do_loc ON td.DOLocationID = do_loc.location_id
GROUP BY 
    start_zone, 
    end_zone;
```


```sql
SELECT 
    start_zone, 
    end_zone
FROM 
    trip_stats
ORDER BY 
    average_trip_time DESC
LIMIT 1;
```

```bash
   start_zone   | end_zone 
----------------+----------
 Yorkville East | Steinway
(1 row)
```

### Question 2

```sql
CREATE MATERIALIZED VIEW trip_stats_num AS
SELECT 
    pu_loc.Zone AS start_zone, 
    do_loc.Zone AS end_zone, 
    COUNT(*) AS number_of_trips,
    AVG(EXTRACT(EPOCH FROM (td.tpep_dropoff_datetime - td.tpep_pickup_datetime))) AS average_trip_time, 
    MIN(EXTRACT(EPOCH FROM (td.tpep_dropoff_datetime - td.tpep_pickup_datetime))) AS min_trip_time, 
    MAX(EXTRACT(EPOCH FROM (td.tpep_dropoff_datetime - td.tpep_pickup_datetime))) AS max_trip_time
FROM 
    trip_data td
JOIN 
    taxi_zone pu_loc ON td.PULocationID = pu_loc.location_id
JOIN 
    taxi_zone do_loc ON td.DOLocationID = do_loc.location_id
GROUP BY 
    start_zone, 
    end_zone;
```


```sql
SELECT 
    start_zone, 
    end_zone,
    number_of_trips
FROM 
    trip_stats_num
ORDER BY 
    average_trip_time DESC
LIMIT 1;
```

```bash
   start_zone   | end_zone | number_of_trips 
----------------+----------+-----------------
 Yorkville East | Steinway |               1
```

### Question 3

```sql
SELECT
    taxi_zone.Zone AS pickup_zone,
    count(*) AS pickup_count
FROM
    trip_data
        JOIN taxi_zone
            ON trip_data.PULocationID = taxi_zone.location_id
WHERE
    trip_data.tpep_pickup_datetime BETWEEN 
        (SELECT MAX(tpep_pickup_datetime) - INTERVAL '17' HOUR FROM trip_data) AND 
        (SELECT MAX(tpep_pickup_datetime) FROM trip_data)
GROUP BY
    taxi_zone.Zone
ORDER BY pickup_count DESC
    LIMIT 3;
```

``bash
    LIMIT 3;
     pickup_zone     | pickup_count 
---------------------+--------------
 LaGuardia Airport   |           19
 JFK Airport         |           17
 Lincoln Square East |           17
(3 rows)
```
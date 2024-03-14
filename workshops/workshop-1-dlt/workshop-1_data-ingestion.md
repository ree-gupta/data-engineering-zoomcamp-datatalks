# Data ingestion with dlt

- [Workshop Link](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024/workshops/dlt.md)
- Data loading does involve adding the metadata layer
- Incremental loading: only load the new data

## Extracting data

- What needs to be considered for extraction, to prevent pipelines from breaking:
  - Hardware limits - navigating the challenges of managing large data
  - Network limits - retries
  - Source api limits - rate limits

- How do we allow filling the memory?
    - Control the max memory that you use

- Control the max memory by streaming the data

- Data engineers usually stream the data between buffers, such as
  - from API to a local file
  - from webhooks to event 
  - from event queue to Bucket

- Streaming in python via generators
  - generators are functions that can return multiple times - by allowing multiple returns, the data can be released as it is prduced as a stream, instead of returning it all at once

- dlt handle things such as:
    - Schema: Inferring and evolving schema, alerting changes, using schemas as data contracts.
    - Typing data, flattening structures, renaming columns to fit database standards. In our example we will pass the “data” you can see above and see it normalised.
    - Processing a stream of events/rows without filling memory. This includes extraction from generators.
    - Loading to a variety of dbs or file formats.


## Analytics Engineering

### Analytics Engineering Basics

<iframe width="560" height="315" src="https://www.youtube.com/embed/uF76d5EmdtU?si=zEpn6nq10Ht-LeXc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

- Role sits in between data engineering and data analysis/data science
- Data modelling concepts:
  - ETL vs ELT: Extract, Transform, Load vs Extract, Load, Transform
    - ETL is the traditional way of doing things - Slightly more stable and compliant data analysis - higher storage and compute costs
    - ELT is the modern way of doing things - More faster and flexible data analysis - lower maintainance and compute costs
  - Kimball's Dimensional Modelling
    - Objective is to deliver data to the end user in a way that is easy to understand and use - deliver fast queries
    - Approach - prioritize user understandibility over non-redundancy
  - Bill Inmon's Data Warehousing (check and confirm)
    - Objective is to deliver data to the end user in a way that is non-redundant and consistent
    - Approach - prioritize non-redundancy over user understandibility
  - Data vault modelling
  - Elements of dimensional modelling
    - Fact tables
      - Measurements, metrics or facts
      - Corresponds to business processes
      - "verbs"
    - Dimension tables
      - Corresponds to business entities
      - Provides context to the facts
      - "nouns"
- Architecture of dimensional modelling:
  - Stage area
    - Raw data
    - No transformation
    - not meant for end users
  - Processing area
    - raw data to data models
    - focus on efficiency
    - ensuring data standards
  - Presentation area
    - final presentation of the data
    - exposure to business stakeholders

### dbt

<iframe width="560" height="315" src="https://www.youtube.com/embed/gsKuETFJr54?si=NV-wXE9pXP3kFv3j" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

- dbt is a transformation workflow that allows anyone that knows SQL to deploy analytics code following software engineering best practices like modularity, portability, CI/CD and documentation
- Each model is a:
  - SQL file
  - Select statement and no DDL or DML

Sidebar: What is DDL and DML? - Data Definition Language and Data Manipulation Language
DDL (Data Definition Language) and DML (Data Manipulation Language) are two types of operations in SQL (Structured Query Language) used to interact with databases.

**DDL (Data Definition Language)** includes SQL commands that define the structure of a database, including creating, altering, and deleting database objects such as tables, schemas, indexes, and views. Examples of DDL commands include:

- `CREATE`: to create a new table or database.
- `ALTER`: to alter the structure of the database.
- `DROP`: to delete a table or database.
- `TRUNCATE`: to remove all records from a table, including all spaces allocated for the records are removed.

**DML (Data Manipulation Language)** includes SQL commands that manipulate the data stored in database objects. DML is used for inserting, retrieving, modifying, and deleting data in a database. Examples of DML commands include:

- `SELECT`: to select specific data from a database.
- `INSERT`: to insert new data into a database.
- `UPDATE`: to update existing data within a database.
- `DELETE`: to delete records from a database.

In summary, DDL is used to create and manage tables and other structures in a database, while DML is used to manage the data itself.

- How to use dbt?
  - dbt Core
    - Open source project that allows you to run dbt locally
    - dbt CLI
  - dbt Cloud
    - SaaS product that allows you to run dbt in the cloud

- 
<!-- ========================================== -->

<!-- HEADER BANNER & TECH STACK BADGES          -->

<!-- ========================================== -->

<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=waving&color=0078D4&height=220&section=header&text=Microsoft%20Fabric%20Local%20Simulation&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&subtext=Medallion%20Architecture%20%E2%80%A2%20Delta%20Lake%20%E2%80%A2%20Direct%20Lake%20%E2%80%A2%20DuckDB%20%E2%80%A2%20MLflow&subtextSize=16&subtextAlignY=62"
    width="100%"
    alt="Microsoft Fabric Local Simulation"
  />
</p>

<p align="center">
  <a href="https://github.com/hamdankhan1208/microsoft-fabric-local-simulation">
    <img src="https://img.shields.io/badge/Microsoft%20Fabric-Local%20Simulation-0078D4?style=for-the-badge&logo=microsoft&logoColor=white" alt="Microsoft Fabric">
  </a>
  <img src="https://img.shields.io/badge/Delta%20Lake-00A4EF?style=for-the-badge&logo=delta&logoColor=white" alt="Delta Lake">
  <img src="https://img.shields.io/badge/DuckDB-FFF000?style=for-the-badge&logo=duckdb&logoColor=black" alt="DuckDB">
  <img src="https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white" alt="MLflow">
  <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions">
</p>

<p align="center">
  <a href="https://github.com/hamdankhan1208/microsoft-fabric-local-simulation/actions/workflows/pipeline.yml">
    <img src="https://github.com/hamdankhan1208/microsoft-fabric-local-simulation/actions/workflows/pipeline.yml/badge.svg" alt="CI/CD Pipeline Status">
  </a>
</p>

---

# 🏛️ Microsoft Fabric Local Simulation

An end-to-end local implementation of the **Microsoft Fabric Unified Analytics ecosystem**, built entirely with Python and open-source technologies.

This project recreates the core architectural concepts of Microsoft Fabric on a local machine, including:

* 🥉 **Bronze / Silver / Gold Medallion Architecture**
* 🗄️ **Delta Lake transactional storage**
* 🔄 **ACID transactions and time travel**
* ⚡ **Table optimization and file compaction**
* 🧹 **Data cleansing and schema enforcement**
* ⭐ **Kimball Star Schema dimensional modeling**
* 📊 **Power BI Direct Lake architectural concepts**
* 🦆 **DuckDB SQL Analytics Endpoint simulation**
* 🤖 **Machine Learning with scikit-learn**
* 📈 **MLflow experiment tracking**
* 🔗 **Data lineage and Delta table versioning**
* ⚙️ **GitHub Actions CI/CD automation**

The goal is not to reproduce Microsoft Fabric itself, but to demonstrate how its major architectural concepts can be implemented using open-source technologies in a reproducible local environment.

---

## 🎯 Project Objective

Microsoft Fabric combines data engineering, data warehousing, data science, real-time analytics, and business intelligence into a unified platform built around **OneLake**.

This project provides a local approximation of that architecture.

The pipeline takes raw transactional sales data and moves it through a complete analytical lifecycle:

```text
Raw Data
   │
   ▼
┌──────────────┐
│    BRONZE    │  Raw Delta Tables
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    SILVER    │  Cleansed & Conformed Data
└──────┬───────┘
       │
       ▼
┌──────────────┐
│     GOLD     │  Kimball Star Schema
└──────┬───────┘
       │
       ├──────────────► DuckDB SQL Analytics
       │
       └──────────────► MLflow + Machine Learning
```

---

# 🏗️ Architecture

## Microsoft Fabric Concept Mapping

| Local Pipeline Layer     | Open-Source Tooling            | Microsoft Fabric Equivalent                    | Architectural Focus                                                     |
| :----------------------- | :----------------------------- | :--------------------------------------------- | :---------------------------------------------------------------------- |
| **Storage Engine**       | `deltalake` / `delta-rs`       | **OneLake**                                    | Delta transaction logs, ACID transactions, versioning and table storage |
| **Bronze Layer**         | `pandas`, `deltalake`          | **Fabric Lakehouse**                           | Raw ingestion and append-only transactional storage                     |
| **Table Maintenance**    | Delta optimization / vacuum    | **V-Order & Table Maintenance**                | File compaction, storage optimization and garbage collection            |
| **Silver Layer**         | `pandas`, `deltalake`          | **Fabric Data Engineering**                    | Data cleansing, deduplication and schema enforcement                    |
| **Gold Layer**           | `pandas`, dimensional modeling | **Fabric Analytics Engineering / Direct Lake** | Business-ready Kimball Star Schema                                      |
| **SQL Analytics**        | `DuckDB`                       | **SQL Analytics Endpoint**                     | SQL-based analytical querying over Delta tables                         |
| **Data Science / MLOps** | `scikit-learn`, `MLflow`       | **Fabric Data Science**                        | Model training, experiment tracking and lineage                         |
| **DevOps / CI/CD**       | GitHub Actions                 | **Fabric Deployment Pipelines**                | Automated validation and pipeline execution                             |

---

# 🥉 Medallion Architecture

The project follows the standard **Bronze → Silver → Gold** data architecture pattern.

### 🥉 Bronze

The Bronze layer contains raw data as it arrives from the source.

Responsibilities include:

* Raw data ingestion
* Initial schema creation
* Delta table creation
* Append operations
* Transaction history
* Time-travel demonstrations

Location:

```text
fabric_lakehouse/bronze/raw_sales/
```

---

### 🥈 Silver

The Silver layer contains cleansed and conformed data.

Processing includes:

* Data type normalization
* Duplicate removal
* Schema enforcement
* Null handling
* Boundary-condition filtering
* Data quality transformations

Location:

```text
fabric_lakehouse/silver/clean_sales/
```

---

### 🥇 Gold

The Gold layer contains business-ready analytical models.

The project uses a **Kimball Star Schema** consisting of:

```text
                 ┌───────────────┐
                 │  dim_customer │
                 └───────┬───────┘
                         │
                         │
┌──────────────┐   ┌─────▼──────┐   ┌──────────────┐
│   dim_date   │──►│ fact_sales │◄──│   dim_store  │
└──────────────┘   └────────────┘   └──────────────┘
```

Location:

```text
fabric_lakehouse/gold/
├── dim_customer/
├── dim_date/
├── dim_store/
└── fact_sales/
```

This structure is designed to demonstrate the dimensional modeling patterns commonly used for analytical workloads and Power BI semantic models.

---

# ⚡ Delta Lake Capabilities

The project demonstrates several important Delta Lake concepts through `delta-rs`.

### ACID Transactions

Every write operation is represented in the Delta transaction log:

```text
_delta_log/
```

This provides a transaction history for the table and enables version-aware operations.

### Time Travel

The project demonstrates querying previous versions of the dataset, allowing historical states of a table to be inspected.

For example:

```text
Version 0
   │
   ├── Initial Bronze ingestion
   │
Version 1
   │
   └── Additional batch appended
```

### File Compaction

Small Parquet files can be consolidated to improve read performance and reduce file-management overhead.

### Vacuum

Obsolete physical files can be removed after they are no longer required.

> **Note:** Local Delta maintenance operations demonstrate the underlying storage concepts. They should not be interpreted as a one-to-one implementation of every Microsoft Fabric storage optimization feature.

---

# 🦆 SQL Analytics Endpoint Simulation

The project uses **DuckDB** to simulate a serverless SQL analytics endpoint.

DuckDB can query the Delta/Parquet-backed Gold tables without requiring a traditional database server.

Example analytical workflow:

```sql
SELECT
    s.store_location,
    SUM(f.amount) AS total_sales,
    COUNT(*) AS transaction_count
FROM fact_sales f
JOIN dim_store s
    ON f.store_id = s.store_id
GROUP BY s.store_location
ORDER BY total_sales DESC;
```

This demonstrates the architectural concept of querying lakehouse data through a SQL-based analytical interface without first copying the data into a separate relational database.

---

# 🤖 Machine Learning & MLflow

The project includes an end-to-end machine learning pipeline using:

* `scikit-learn`
* `MLflow`
* Delta Lake

The ML pipeline demonstrates:

1. Reading analytical data from the Gold layer
2. Feature extraction
3. Model training
4. Model evaluation
5. MLflow experiment tracking
6. Metric logging
7. Parameter logging
8. Model artifact tracking
9. Delta table version lineage

This provides a local approximation of the relationship between a Fabric Lakehouse and a Data Science / ML workflow.

---

# 📁 Project Structure

```text
microsoft-fabric-local-simulation/
│
├── .github/
│   └── workflows/
│       └── pipeline.yml
│
├── fabric_lakehouse/
│   ├── bronze/
│   │   └── raw_sales/
│   │
│   ├── silver/
│   │   └── clean_sales/
│   │
│   └── gold/
│       ├── dim_customer/
│       ├── dim_date/
│       ├── dim_store/
│       └── fact_sales/
│
├── 01_ingest_bronze.py
├── 02_append_and_timetravel.py
├── 03_optimize_and_vacuum.py
├── 04_bronze_to_silver.py
├── 05_silver_to_gold_star_schema.py
├── 06_ml_pipeline_mlflow.py
├── 07_sql_analytics_endpoint.py
│
├── .gitignore
└── README.md
```

### Script Responsibilities

| Script                             | Responsibility                                  |
| :--------------------------------- | :---------------------------------------------- |
| `01_ingest_bronze.py`              | Creates the initial Bronze Delta table          |
| `02_append_and_timetravel.py`      | Appends data and demonstrates Delta time travel |
| `03_optimize_and_vacuum.py`        | Performs table optimization and cleanup         |
| `04_bronze_to_silver.py`           | Cleans, deduplicates and validates Bronze data  |
| `05_silver_to_gold_star_schema.py` | Builds the Gold dimensional model               |
| `06_ml_pipeline_mlflow.py`         | Trains the ML model and logs experiments        |
| `07_sql_analytics_endpoint.py`     | Executes analytical SQL through DuckDB          |

---

# 🚀 Getting Started

## Prerequisites

Make sure the following are installed:

* **Python 3.10+**
* **Git**
* Windows, macOS or Linux

---

## 1. Clone the Repository

```bash
git clone https://github.com/hamdankhan1208/microsoft-fabric-local-simulation.git

cd microsoft-fabric-local-simulation
```

---

## 2. Create a Virtual Environment

### Windows — PowerShell

```powershell
python -m venv fabric_env

Set-ExecutionPolicy -ExecutionPolicy Process -Scope Process

.\fabric_env\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv fabric_env

source fabric_env/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🧪 Execute the Pipeline

The scripts are designed to be executed sequentially.

### Step 1 — Bronze Ingestion

Create the initial raw Delta table.

```bash
python 01_ingest_bronze.py
```

Creates the initial Bronze table:

```text
Version 0
```

---

### Step 2 — Append & Time Travel

Append another batch of records and inspect historical versions.

```bash
python 02_append_and_timetravel.py
```

Demonstrates:

* Delta append transactions
* Version history
* Point-in-time querying

---

### Step 3 — Optimize & Vacuum

Perform Delta table maintenance.

```bash
python 03_optimize_and_vacuum.py
```

Demonstrates:

* Small-file compaction
* Storage optimization
* Removal of obsolete files

---

### Step 4 — Bronze → Silver

Clean and transform the raw data.

```bash
python 04_bronze_to_silver.py
```

Processing includes:

```text
Raw Data
   │
   ├── Schema validation
   ├── Data cleaning
   ├── Deduplication
   ├── Data type normalization
   └── Boundary filtering
          │
          ▼
     Silver Delta Table
```

---

### Step 5 — Silver → Gold

Create the analytical Star Schema.

```bash
python 05_silver_to_gold_star_schema.py
```

Generates:

```text
gold/
├── dim_customer/
├── dim_date/
├── dim_store/
└── fact_sales/
```

---

### Step 6 — Machine Learning + MLflow

Run the machine learning pipeline.

```bash
python 06_ml_pipeline_mlflow.py
```

This performs:

* Feature extraction
* Model training
* Evaluation
* MLflow experiment logging
* Model artifact tracking
* Delta lineage tracking

---

### Step 7 — SQL Analytics

Run analytical SQL queries against the Gold layer.

```bash
python 07_sql_analytics_endpoint.py
```

This uses DuckDB as the local SQL analytics engine.

---

# 📖 Gold Layer Data Dictionary

The Gold layer follows a Kimball Star Schema.

## 📊 `fact_sales`

The central fact table stores transactional measures and foreign keys to the dimensional tables.

| Column           | Data Type   | Key Type    | Description                           |
| :--------------- | :---------- | :---------- | :------------------------------------ |
| `transaction_id` | `INTEGER`   | Primary Key | Unique transaction identifier         |
| `customer_id`    | `VARCHAR`   | Foreign Key | References `dim_customer.customer_id` |
| `store_id`       | `VARCHAR`   | Foreign Key | References `dim_store.store_id`       |
| `date_key`       | `INTEGER`   | Foreign Key | References `dim_date.date_key`        |
| `amount`         | `DOUBLE`    | Measure     | Monetary transaction amount in USD    |
| `timestamp`      | `TIMESTAMP` | Attribute   | UTC timestamp of the transaction      |

---

## 👤 `dim_customer`

Contains customer-level descriptive attributes.

| Column          | Data Type | Key Type    | Description                |
| :-------------- | :-------- | :---------- | :------------------------- |
| `customer_id`   | `VARCHAR` | Primary Key | Unique customer identifier |
| `customer_name` | `VARCHAR` | Attribute   | Customer display name      |

---

## 🏬 `dim_store`

Contains retail store attributes.

| Column           | Data Type | Key Type    | Description             |
| :--------------- | :-------- | :---------- | :---------------------- |
| `store_id`       | `VARCHAR` | Primary Key | Unique store identifier |
| `store_location` | `VARCHAR` | Attribute   | Physical store location |

---

## 📅 `dim_date`

A conformed date dimension supporting time-based analytical queries.

| Column       | Data Type | Key Type    | Description                             |
| :----------- | :-------- | :---------- | :-------------------------------------- |
| `date_key`   | `INTEGER` | Primary Key | Surrogate date key in `YYYYMMDD` format |
| `date`       | `DATE`    | Attribute   | Calendar date                           |
| `year`       | `INTEGER` | Attribute   | Four-digit calendar year                |
| `month`      | `INTEGER` | Attribute   | Numeric month from 1–12                 |
| `month_name` | `VARCHAR` | Attribute   | Full month name                         |
| `day`        | `INTEGER` | Attribute   | Day of month                            |
| `day_name`   | `VARCHAR` | Attribute   | Full day-of-week name                   |

---

# 🔄 End-to-End Data Flow

```text
                    ┌─────────────────────┐
                    │     Raw Dataset     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       BRONZE        │
                    │                     │
                    │ Raw Delta Table     │
                    │ ACID Transactions   │
                    │ Time Travel         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       SILVER        │
                    │                     │
                    │ Cleansing           │
                    │ Deduplication       │
                    │ Schema Enforcement  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │        GOLD         │
                    │                     │
                    │ Kimball Star Schema │
                    │ Fact + Dimensions   │
                    └──────┬───────┬──────┘
                           │       │
                ┌──────────┘       └──────────┐
                ▼                             ▼
       ┌─────────────────┐          ┌──────────────────┐
       │     DuckDB      │          │  MLflow + ML     │
       │                 │          │                  │
       │ SQL Analytics   │          │ Model Training   │
       │ & Exploration   │          │ Experiment Logs  │
       └─────────────────┘          └──────────────────┘
```

---

# ⚙️ CI/CD

The repository includes a GitHub Actions workflow:

```text
.github/
└── workflows/
    └── pipeline.yml
```

The CI/CD pipeline is intended to automatically validate the project and execute the data pipeline in a clean environment.

This helps demonstrate concepts such as:

* Automated testing
* Regression detection
* Reproducible execution
* Dependency installation
* Pipeline validation
* Continuous integration

---

# 🧰 Technology Stack

| Technology                | Purpose                                            |
| :------------------------ | :------------------------------------------------- |
| **Python**                | Primary development language                       |
| **Pandas**                | Data manipulation and transformation               |
| **PyArrow**               | Parquet and columnar data processing               |
| **Delta Lake / delta-rs** | Transactional lakehouse storage                    |
| **DuckDB**                | Local analytical SQL engine                        |
| **scikit-learn**          | Machine learning                                   |
| **MLflow**                | Experiment tracking and model lifecycle management |
| **GitHub Actions**        | CI/CD automation                                   |
| **Parquet**               | Columnar analytical storage                        |

---

# 🧠 What This Project Demonstrates

This project demonstrates practical understanding of modern data-platform architecture rather than simply implementing isolated data-processing scripts.

### Data Engineering

* Medallion Architecture
* Lakehouse design
* Delta Lake
* ACID transactions
* Time travel
* Data cleansing
* Schema enforcement
* Deduplication
* Table optimization

### Data Warehousing

* Kimball dimensional modeling
* Fact tables
* Dimension tables
* Surrogate keys
* Star Schema
* Conformed dimensions
* Analytical query design

### Analytics

* SQL over lakehouse data
* DuckDB
* Columnar storage
* Aggregation workloads
* Analytical data access patterns

### Machine Learning

* Feature engineering
* Model training
* Model evaluation
* Experiment tracking
* Model artifacts
* Data/model lineage

### DevOps

* Git
* GitHub
* GitHub Actions
* Automated pipeline execution
* Reproducible environments

---

# 🏛️ Microsoft Fabric vs Local Implementation

This project is intentionally a **conceptual and functional simulation**, not a replacement for Microsoft Fabric.

| Microsoft Fabric            | Local Implementation                        |
| :-------------------------- | :------------------------------------------ |
| OneLake                     | Local filesystem + Delta Lake               |
| Lakehouse                   | Delta tables                                |
| Data Engineering            | Python + Pandas                             |
| Spark                       | Pandas / PyArrow processing                 |
| V-Order / maintenance       | Delta optimization / compaction             |
| SQL Analytics Endpoint      | DuckDB                                      |
| Direct Lake                 | Star Schema optimized for analytical access |
| Fabric Data Science         | scikit-learn + MLflow                       |
| Fabric Deployment Pipelines | GitHub Actions                              |

The purpose is to understand **why these components exist, how they interact, and what architectural problems they solve**.

---

# 📌 Limitations

Because this project runs locally, some Microsoft Fabric capabilities are represented conceptually rather than reproduced exactly.

For example:

* DuckDB is not the Microsoft Fabric SQL Analytics Endpoint.
* Local Delta Lake storage is not OneLake.
* Pandas is not Apache Spark.
* Delta compaction is not identical to Fabric V-Order.
* The local Gold layer demonstrates Direct Lake-compatible modeling principles but does not provide an actual Power BI Direct Lake connection.
* GitHub Actions provides CI/CD functionality but is not identical to Fabric Deployment Pipelines.

These differences are intentional.

The project focuses on reproducing the **underlying architectural patterns** using accessible open-source technologies.

---

# 📈 Future Improvements

Potential extensions include:

* [ ] Add automated unit and data-quality tests
* [ ] Add Great Expectations or equivalent data validation
* [ ] Add incremental Silver processing
* [ ] Add Slowly Changing Dimensions (SCD Type 2)
* [ ] Add partitioning strategies
* [ ] Add more advanced Delta Lake operations
* [ ] Add a local Power BI-compatible analytical workflow
* [ ] Add Apache Spark for a closer Fabric Data Engineering simulation
* [ ] Add containerization with Docker
* [ ] Add automated ML model registration
* [ ] Add model serving
* [ ] Add experiment comparison dashboards
* [ ] Add pipeline orchestration
* [ ] Add data lineage visualization
* [ ] Add automated documentation generation

---

# 👨‍💻 Author

**Hamdan Khan**

GitHub:

<a href="https://github.com/hamdankhan1208">
  github.com/hamdankhan1208
</a>

---

# 📄 License

MIT License

Copyright (c) 2026 Hamdan Khan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

<p align="center">
  <strong>Built to explore modern Lakehouse architecture locally.</strong>
</p>

<p align="center">
  Microsoft Fabric concepts • Delta Lake • Medallion Architecture • DuckDB • MLflow • CI/CD
</p>

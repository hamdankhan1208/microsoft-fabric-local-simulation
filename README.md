<!-- ========================================== -->
<!-- HEADER BANNER & TECH STACK BADGES          -->
<!-- ========================================== -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0078D4&height=220&section=header&text=Microsoft%20Fabric%20Local%20Simulation&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&subtext=Medallion%20Architecture%20%E2%80%A2%20Delta%20Lake%20%E2%80%A2%20Direct%20Lake%20%E2%80%A2%20MLflow&subtextSize=16&subtextAlignY=62" width="100%" alt="Microsoft Fabric Banner" />
</p>

<p align="center">
  <a href="https://github.com/your-username/microsoft-fabric-local-simulation">
    <img src="https://img.shields.io/badge/Microsoft_Fabric-Local_Simulation-0078D4?style=for-the-badge&logo=microsoft&logoColor=white" alt="Microsoft Fabric">
  </a>
  <img src="https://img.shields.io/badge/Delta_Lake-00A4EF?style=for-the-badge&logo=delta&logoColor=white" alt="Delta Lake">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white" alt="MLflow">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn">
  <img src="https://github.com/hamdankhan1208/microsoft-fabric-local-simulation/actions/workflows/pipeline.yml/badge.svg" alt="Pipeline Status">
</p>

<br />

# 🏛️ Enterprise Microsoft Fabric Local Simulation

An end-to-end local simulation of the **Microsoft Fabric Unified Analytics Ecosystem** built with Python and open-source Delta standards (`delta-rs`, `pandas`, `pyarrow`, `scikit-learn`, `mlflow`). 

This project implements a production-grade **Medallion Architecture**, Delta Lake transaction mechanics, a **Kimball Star Schema** optimized for Power BI Direct Lake mode, and **MLflow Experiment Tracking** mirroring Fabric's Data Science experience.

---

## 📐 Architecture & Microsoft Fabric Concept Mapping

| Local Pipeline Layer | Open-Source Tooling | Microsoft Fabric Equivalent | Architectural Focus |
| :--- | :--- | :--- | :--- |
| **Storage Engine** | `deltalake` (`delta-rs`) | **OneLake Unified Namespace** | ACID transactions, Delta transaction log (`_delta_log`), multi-version concurrency control. |
| **Bronze Layer** | `pandas`, `deltalake` | **Fabric Lakehouse (Raw Ingestion)** | Append-only raw ingestion, transactional batch processing, schema generation. |
| **Table Maintenance** | `dt.optimize.compact()`, `dt.vacuum()` | **Fabric V-Order & Maintenance** | Small-file compaction, Write Amplification vs. Read performance optimization, storage pruning. |
| **Silver Layer** | `pandas`, `deltalake` | **Fabric Data Engineering / PySpark** | Data hygiene, deduplication, schema enforcement, boundary condition filtering. |
| **Gold Layer** | Dimensional Modeling | **Fabric Analytics Engineer / Direct Lake** | Kimball Star Schema (Fact & Dimension tables) optimized for Power BI Direct Lake mode. |
| **MLOps / Data Science** | `scikit-learn`, `mlflow` | **Fabric Synapse Data Science** | Feature extraction, experiment run tracking, model registry, Delta version lineage. |

---

## 🗂️ Project Directory Structure

```text
FabricPractice/
│
├── fabric_lakehouse/                  # Simulated OneLake Local Namespace
│   ├── bronze/                        # Raw Ingested Delta Tables
│   │   └── raw_sales/
│   ├── silver/                        # Cleansed & Conformed Delta Tables
│   │   └── clean_sales/
│   └── gold/                          # Business-Ready Kimball Star Schema
│       ├── dim_customer/
│       ├── dim_date/
│       ├── dim_store/
│       └── fact_sales/
│
├── 01_ingest_bronze.py                # Bronze Ingestion & Delta Log Creation
├── 02_append_and_timetravel.py        # Append Transactions & Point-in-Time Time Travel
├── 03_optimize_and_vacuum.py          # File Compaction (V-Order equivalent) & Garbage Collection
├── 04_bronze_to_silver.py             # Silver Cleaning, Deduplication & Schema Enforcement
├── 05_silver_to_gold_star_schema.py   # Gold Layer Kimball Modeling for Direct Lake
├── 06_ml_pipeline_mlflow.py           # End-to-End ML Pipeline & Fabric MLflow Experiment Logging
├── .gitignore                         # Environment & build file exclusion rules
└── README.md                          # Project Documentation
```

---

## 🚀 Getting Started

### Prerequisites
* **Python 3.10+**
* **Git**

### Installation & Local Environment Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/microsoft-fabric-local-simulation.git
   cd microsoft-fabric-local-simulation
   ```

2. **Create and activate a virtual environment:**
   * **Windows (PowerShell):**
     ```powershell
     python -m venv fabric_env
     Set-ExecutionPolicy -ExecutionPolicy Process -Scope Process
     .abric_env\Scripts ctivate
     ```
   * **Mac/Linux:**
     ```bash
     python3 -m venv fabric_env
     source fabric_env/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install pandas deltalake pyarrow scikit-learn mlflow
   ```

---

## 🧪 Step-by-Step Execution Pipeline

Run the scripts sequentially to execute the full data lifecycle:

```bash
# 1. Ingest raw sales data into Bronze Delta Table (Version 0)
python 01_ingest_bronze.py

# 2. Append batch data (Version 1) & run Point-in-Time Time Travel queries
python 02_append_and_timetravel.py

# 3. Compact small Parquet files & purge stale physical files via VACUUM
python 03_optimize_and_vacuum.py

# 4. Clean, deduplicate, and enforce schemas into Silver Delta Table
python 04_bronze_to_silver.py

# 5. Transform Silver data into a Gold Star Schema (Fact + Dimensions)
python 05_silver_to_gold_star_schema.py

# 6. Train Customer Classification model, logging Delta lineage & MLflow metrics
python 06_ml_pipeline_mlflow.py
```

### Launch Local MLflow UI

To view logged hyperparameter runs, metrics, and registered model artifacts:
```bash
mlflow ui
```
Navigate to `http://127.0.0.1:5000` in your web browser.

---
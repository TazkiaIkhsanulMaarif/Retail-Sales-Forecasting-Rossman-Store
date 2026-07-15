# 🛒 Retail Data Warehouse & Sales Forecasting

End-to-end data pipeline built on the [Rossmann Store Sales](https://www.kaggle.com/c/rossmann-store-sales) dataset — from raw retail data to an interactive BI dashboard, covering data engineering, machine learning forecasting, and business intelligence.

> **Live Dashboard:** [Tableau Public Link](#) *(update after publishing)*
> **Portfolio target:** Data Analyst / Business Intelligence Analyst / Data Engineer

<img width="741" height="457" alt="image" src="https://github.com/user-attachments/assets/a76dac5e-6ca9-49a3-93ef-eba9212352ef" />

---

## 🎯 Business Objective

Rossmann operates 1,115 stores across Europe. This project builds a full analytics pipeline to help stakeholders understand historical sales drivers (promotions, seasonality, store segmentation, competition) and forecast short-term demand to support inventory and staffing decisions.

---

## 🔧 Tech Stack

| Layer | Tools |
|---|---|
| Language | Python (Pandas, Scikit-learn) |
| Data Warehouse | Snowflake |
| Orchestration | Apache Airflow |
| Modeling | RandomForest (Advanced), evaluated via MAE/RMSE/R² |
| BI / Visualization | Tableau |
| Query | SQL |

---

## 📊 Data Model (Star Schema)

**Schema `DWH`**

| Table | Type | Key Columns |
|---|---|---|
| `DIM_DATE` | Dimension | DATE_KEY, CALENDAR_DATE, YEAR, MONTH, QUARTER, WEEK, DAYOFWEEK, IS_WEEKEND |
| `DIM_STORE` | Dimension | STORE_KEY, STORETYPE, ASSORTMENT, COMPETITION_DISTANCE, PROMO2, PROMO_INTERVAL |
| `FACT_SALES` | Fact | DATE_KEY (FK), STORE_KEY (FK), SALES, CUSTOMERS, IS_OPEN, IS_PROMO, STATE_HOLIDAY_TYPE |

**Schema `ANALYTICS`**

| Table | Type | Key Columns |
|---|---|---|
| `FACT_FORECAST` | Fact | DATE_KEY, STORE_KEY, ACTUAL_SALES, PREDICTED_SALES, MODEL_NAME, MODEL_VERSION |
| `MODEL_EVALUATION` | Reference | MODEL_NAME, MODEL_VERSION, MAE, RMSE, R2, TRAINING_DATE |

Data flows through 4 schemas: `RAW` (untouched source) → `STAGING` (standardized column names) → `DWH` (star schema) → `ANALYTICS` (ML outputs).

---

## 🤖 Forecasting Model

| Metric | Value |
|---|---|
| Model | RandomForest_Advanced |
| Version | v2.0.0 |
| MAE | 535 |
| RMSE | 791 |
| R² | 0.954 |
| Forecast window | 14 days (2015-08-01 → 2015-08-14) |
| Forecast volume | 15,610 predictions (1,115 stores × 14 days) |

**Validation checks:** 0 duplicates, 0 null predictions, all 1,115 stores have exactly 14 predictions each.

---

## 📈 BI Dashboard

Built as an **analytical dashboard** — designed for exploration and root-cause analysis, not executive/KPI monitoring. Three connected pages:

### 1. Main Dashboard
Six linked visuals with global filters (Year, Store Type, Promo):
- **Sales by Store Type × Assortment** — segment contribution breakdown
- **Monthly Sales Trend (Promo vs Non-Promo)** — promotion effectiveness over time
- **Sales Heatmap (Month × Weekday)** — seasonality patterns
- **Competitor Distance vs Sales** — external factor impact analysis
- **Sales Distribution by Store Type (Box Plot)** — performance consistency/variability
- **Store Deviation: Predicted vs Historical** — forecast-based risk flagging

### 2. Insight & Recommendation
Written key findings paired with actionable business recommendations, backed by supporting mini-charts.

### 3. Detail Records
Row-level drill-down table (store, date, sales, customers) with contextual filters — for data verification and traceability.

![Insight Page](docs/screenshots/insight_page.png)

---

## 💡 Key Insights

1. **Store Performance** — Store Type A generates ~54% of total sales (€3.17B), while Store Type B has the lowest total sales but the highest performance variability across stores.
2. **Promotion Effectiveness** — Promotions do not consistently raise sales; timing appears to matter more than promo frequency.
3. **Seasonal Trends** — Sales consistently peak on Mondays and in December.
4. **Competition Impact** — Competitor distance shows minimal correlation with sales; internal factors (assortment, promotions) matter more.
5. **Forecast Performance** — The model achieves R²=0.954 (MAE 535), and the 14-day forecast signals a broad seasonal sales decline across most stores.

## 🎯 Business Recommendations

1. Prioritize inventory and resource allocation toward Store Type A, especially Assortment A & B.
2. Optimize promotions based on seasonal demand patterns rather than uniform campaigns.
3. Increase inventory and staffing ahead of Mondays and December.
4. Focus improvement efforts on internal drivers (assortment, promo timing) over competitor-distance strategy.
5. Use the forecasting model for short-term inventory/workforce planning, while investigating the cause of the predicted seasonal decline.

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/retail-dwh.git
cd retail-dwh

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure Snowflake & Airflow connections
# edit config/ with your credentials

# 4. Run ETL pipeline via Airflow
airflow dags trigger retail_etl_pipeline

# 5. Run forecasting
python forecasting/train_and_predict.py
```

---

## 📸 Screenshots

| Main Dashboard | Insight & Recommendation | Detail Records |
|---|---|---|
| <img width="741" height="457" alt="image" src="https://github.com/user-attachments/assets/7a98325f-3234-4435-9d96-daa3b4affa3e" /> | <img width="745" height="463" alt="image" src="https://github.com/user-attachments/assets/49326001-3856-493c-b42e-eefd13a2fb67" /> | <img width="725" height="451" alt="image" src="https://github.com/user-attachments/assets/6791b94f-8765-485d-b0f4-de28b6fd803e" /> |

---

## 📬 Contact

*(add your name, LinkedIn, and portfolio link here)*

# Redback Operations  
## Requirement Gathering Summary   

---

## Table of Contents  
1. [Project 1 – IoT Bike & VR Game Integration](#project-1--iot-bike--vr-game-integration)  
2. [Project 2 – Elderly Wearable Tech (Lachesis)](#project-2--elderly-wearable-tech-lachesis)  
3. [Project 3 – Athlete Wearable Tech](#project-3--athlete-wearable-tech)  
4. [Project 4 – Computer Vision & Streaming Analytics](#project-4--computer-vision--streaming-analytics)  
5. [Overall Observations](#overall-observations)  

---

## Project 1 – IoT Bike & VR Game Integration  
  
- **Key Features:** SmartBike (Wahoo/KICKR), mobile app, Unity VR integration  
- **Data Source:** IoT sensors – cadence, heart rate, power, incline, RPM  
- **Format:** JSON  
- **Storage Format:** Raw data; some values (e.g., heart rate = 0) need cleaning  
- **Volume:** Few MB per session  
- **Ingestion Frequency:** Suggested batch uploads every 10–30 seconds  
- **Storage Requirements:** Scalable, automated ingestion; time-based partitioning  
- **Access Needs:** Read (VR team, Mobile team), Admin (Engineers)  
- **Issues:** Manual uploads inefficient, no access to legacy server  
- **Quality Concerns:** Some sensor zeros, unprocessed data  
- **Warehouse Suggestions:** SQL backend with API access; remote access flexibility  

---

## Project 2 – Elderly Wearable Tech (Lachesis)  
 
- **Key Features:** Predictive health models (Alzheimer’s, Diabetes, Sleep Disorders, etc.)  
- **Data Source:** External medical datasets (UCI, Kaggle), internal experiments  
- **Format:** CSV, JSON, TXT, XLSX  
- **Volume:** Approx. 300 GB total  
- **Ingestion Frequency:** Real-time to monthly, varies by dataset  
- **Data Shape:** Structured + semi-structured  
- **Challenges:** VM access issues, limited documentation, GPU required  
- **Quality Concerns:** Needs variable linking, dataset validation  
- **Security Needs:** Local GPU processing, secure infrastructure preferred  
- **Warehouse Suggestions:** Enable AI model processing in a secure, local environment  

---

## Project 3 – Athlete Wearable Tech  

- **Valuable Data:** HR, speed, fatigue index, HRV, cadence, environment  
- **Format:** CSV, XLSX (future JSON/API from Garmin/Strava)  
- **Structure:** Structured/tabular  
- **Cleaning Needs:** Extensive – timestamp alignment, outliers, normalization  
- **Access Frequency:** Multiple times daily, including real-time  
- **Storage Estimate:** 250–750MB/day → 500GB+/year expected  
- **Security:** Must comply with Australian Privacy Act; RBAC, encryption  
- **Querying Needs:** Real-time and batch queries; predictive analysis  
- **Insights Expected:** Injury risk, training load, performance forecasting  
- **Warehouse Suggestions:** PostgreSQL on-prem, Python ETL, BI dashboard integration (e.g., Superset, Metabase)  

---

## Project 4 – Computer Vision & Streaming Analytics (Project Orion) 
  
- **Key Features:** Visual data pipeline using YOLOv8, heatmaps, phase detection  
- **Source:** Video/image data → processed via computer vision models  
- **Format:** BLOBs and JSON (Spring schema)  
- **Data Status:** Pre-existing datasets; no new data collected  
- **Ingestion System:** Real-time Kafka streaming  
- **Cleaning Responsibility:** Not handled by Data Warehouse  
- **Storage Needs:** No long-term storage needed  
- **Access:** Power BI for security teams; Next.js frontend for visualizations  
- **Security:** No production-level requirements for capstone  
- **Warehouse Suggestions:** Kafka integration, scalable architecture with fault tolerance  
- **Analytics Tools:** Power BI, Next.js app  

---

## Overall Observations  

- **Ingestion:** Real-time & batch ingestion is expected across all projects  
- **Security:** High security and data privacy required in Projects 2 and 3  
- **ETL Needs:** Flexible ETL pipelines and transformation rules are necessary  
- **BI Integration:** Projects 3 and 4 mention Power BI, Superset integration  
- **AI & Prediction:** AI and predictive modelling planned in Projects 2 and 3  
- **Streaming:** Kafka streaming system emphasized in Project 4  

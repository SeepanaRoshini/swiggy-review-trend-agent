# 📊 Swiggy Review Trend Analysis using Agentic AI

## 📌 Problem Statement
Product teams need to continuously monitor user issues, feature requests, and feedback from app store reviews.  
This project builds an **agentic AI system** that ingests **daily Google Play Store reviews** (treated as batches) and generates a **rolling trend analysis (T-30)** of key topics.

Traditional topic modeling techniques (LDA, TopicBERT) are avoided due to low accuracy and poor deduplication.

---

## 🎯 Key Objectives
- Process daily batches of app reviews
- Identify issues, requests, and feedback topics
- Merge semantically similar topics into a single category
- Track topic frequency trends from **T-30 to T**
- Automatically detect **new emerging topics**

---

## 🤖 Agentic AI Architecture

This system uses **multiple cooperating AI agents**, each responsible for a focused task.

### 🧠 Agent 1: Topic Extraction Agent
**File:** `agents/topic_extractor.py`

- Reads raw review text
- Extracts high-recall issue/request topics
- Focuses on capturing *all relevant signals* rather than precision

Example:
- “Delivery was very late”
- “Food arrived cold”

---

###  Agent 2: Topic Merger (Deduplication Agent)
**File:** `agents/topic_merger.py`

- Prevents similar topics from being treated separately
- Uses semantic similarity / rules to merge variants

Example:
- “Delivery guy was rude”
- “Delivery partner behaved badly”
- “Delivery person was impolite”

 Merged into:
**Delivery partner rude**

This solves the key challenge of inaccurate trend fragmentation.

---

### 📈 Agent 3: Trend Analyzer Agent
**File:** `agents/trend_analyzer.py`

- Maintains a rolling **T-30 window**
- Updates topic frequency per day
- Supports appearance of new topics over time
- Outputs a trend table consumable by product teams

---

## 🗂️ Project Structure

#structure
swiggy-review-trend-agent/
│
├── data/
│ ├── raw/ # Daily review batches (CSV)
│ └── processed/
│
├── agents/
│ ├── topic_extractor.py
│ ├── topic_merger.py
│ └── trend_analyzer.py
│
├── output/
│ ├── trend_report.csv
│ └── sample_report.md
│
├── utils/
│ ├── embeddings.py
│ └── date_utils.py
│
├── main.py # Orchestrator
├── requirements.txt
└── README.md


---

##  How to Run

### 1️ Install Dependencies
```bash
pip install -r requirements.txt
```
##Place CSV files inside:
data/raw/YYYY-MM-DD.csv
 review
 Delivery was delayed
 Food was stale
 Delivery partner was rude
 
##Run the Agent Pipeline
python main.py

The trend report is generated at:

output/trend_report.csv

#output format

| Topic                     | 2024-06-01 | 2024-06-02 | ... | 2024-06-30 |
| ------------------------- | ---------- | ---------- | --- | ---------- |
| Delivery issue            | 12         | 8          | ... | 23         |
| Food stale                | 5          | 7          | ... | 11         |
| Delivery partner rude     | 8          | 12         | ... | 9          |
| Maps not working properly | 2          | 4          | ... | 5          |





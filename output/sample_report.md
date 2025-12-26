#  Swiggy Review Trend Analysis — Sample Report

##  Overview
This report summarizes **daily Google Play Store review trends** for the Swiggy app.  
Reviews are processed in **daily batches**, and topics are consolidated using an **agentic AI system**.

**Analysis Window:** June 1, 2024 – June 30, 2024  
**Batch Frequency:** Daily

---

##  Methodology (High-Level)
- Raw reviews are ingested daily
- AI agents extract issues, feature requests, and feedback topics
- Semantically similar topics are merged into a single category
- Topic frequencies are tracked over a rolling **T-30 window**

---

##  Key Observations
- **Delivery-related issues** show consistently high volume across the month
- **Food quality complaints** spike on multiple days
- **Behavior-related feedback** about delivery partners appears intermittently
- **Feature requests** such as faster delivery re-emerge over time
- New topics automatically appear as users introduce new feedback

---

## 📈 Sample Trend Table (Excerpt)

| Topic | 2024-06-01 | 2024-06-02 |
|------|-----------|-----------|
| Delivery issue | 2 | 1 |
| Food stale | 1 | 1 |
| Delivery partner rude | 2 | 1 |
| Maps not working properly | 1 | 1 |
| Instamart should be open all night | 1 | 0 |
| Bring back 10 minute bolt delivery | 1 | 1 |

> 📎 *For the complete trend data, refer to* `trend_report.csv`.

---

## ✅ Intended Usage
This report is designed for:
- Product managers to identify **recurring user pain points**
- Operations teams to track **delivery and partner issues**
- Feature teams to spot **emerging user requests**

---

## 🏁 Conclusion
The agentic approach ensures **high recall**, **accurate topic consolidation**, and **clear trend visibility**, making the output actionable for real-world product decision-making.

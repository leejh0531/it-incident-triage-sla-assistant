# System Design

## 1. Overview

This system is designed as a simple IT operations support tool for incident and helpdesk ticket management.

The system loads synthetic IT ticket data, assigns ticket priority, calculates SLA risk, recommends a responsible team, searches related FAQs, and displays operational insights through a Streamlit dashboard.

The purpose of this design is to show how IT operational problems can be translated into system components and decision-support logic.

---

## 2. Architecture

```text
CSV Data
→ Data Loader
→ Priority Engine
→ SLA Risk Calculator
→ Assignment Router
→ FAQ Search
→ Insight Generator
→ Streamlit Dashboard
```

---

## 3. Main Components

| Component           | File                       | Role                                                             |
| ------------------- | -------------------------- | ---------------------------------------------------------------- |
| Data Loader         | `src/data_loader.py`       | Loads ticket, FAQ, and SLA policy data from CSV files            |
| Priority Engine     | `src/priority_engine.py`   | Assigns ticket priority based on impact and urgency              |
| SLA Risk Calculator | `src/sla_risk.py`          | Calculates elapsed time, SLA risk score, and SLA status          |
| Assignment Router   | `src/assignment_router.py` | Recommends a responsible support team based on ticket category   |
| FAQ Search          | `src/faq_search.py`        | Searches related FAQs using TF-IDF and cosine similarity         |
| Insight Generator   | `src/insight_generator.py` | Generates simple operational insights from processed ticket data |
| Dashboard           | `app.py`                   | Provides the Streamlit user interface                            |

---

## 4. Data Flow

1. The system loads ticket data from `data/sample_tickets.csv`.
2. The system loads FAQ data from `data/sample_faq.csv`.
3. The system loads SLA policy data from `data/sla_policy.csv`.
4. Ticket priority is assigned based on impact and urgency.
5. The responsible support team is recommended based on ticket category.
6. SLA risk score is calculated using elapsed time and SLA policy.
7. Related FAQs are searched using the ticket description.
8. Dashboard metrics, charts, ticket tables, FAQ results, and insights are displayed.

---

## 5. Data Files

| File                      | Description                                    |
| ------------------------- | ---------------------------------------------- |
| `data/sample_tickets.csv` | Synthetic IT incident and helpdesk ticket data |
| `data/sample_faq.csv`     | Synthetic internal IT FAQ data                 |
| `data/sla_policy.csv`     | SLA rule table by priority level               |

---

## 6. Priority Logic

Ticket priority is determined by combining impact and urgency.

| Impact | Urgency | Priority |
| ------ | ------- | -------- |
| High   | High    | Critical |
| High   | Medium  | High     |
| Medium | High    | High     |
| Medium | Medium  | Medium   |
| Others | Others  | Low      |

This rule-based approach was selected because it is simple, explainable, and easy to modify.

---

## 7. SLA Risk Logic

The SLA risk score is calculated as follows:

```text
SLA Risk Score = elapsed hours / SLA limit hours × 100
```

|   Risk Score | SLA Status |
| -----------: | ---------- |
|        0-50% | Normal     |
|       50-80% | Warning    |
|      80-100% | High Risk  |
| 100% or more | Violated   |

This design allows operators to identify tickets that may violate SLA before the deadline.

---

## 8. FAQ Search Logic

The FAQ search function uses TF-IDF and cosine similarity.

The ticket description is compared with FAQ questions and answers, and the top related FAQ entries are returned.

This makes it possible to reuse existing troubleshooting knowledge and reduce repeated manual support work.

---

## 9. Design Considerations

* The system uses CSV files to keep the project simple and easy to run locally.
* The business rules are explainable and rule-based.
* The system does not use real company or personal data.
* Each function is separated into modules to make the system easier to understand and extend.
* The project can be extended with a database, notification system, authentication, or LLM-based response generation.

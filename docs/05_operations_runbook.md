# Operations Runbook

## 1. Overview

This runbook explains how to set up, run, and troubleshoot the IT Incident Triage & SLA Risk Assistant.

The application is a local Streamlit-based IT operations support tool. It uses synthetic CSV data and does not require external services or real company data.

---

## 2. System Requirements

* Python 3.10 or later
* pip
* Web browser
* Local terminal or VSCode terminal

---

## 3. Installation

Install the required Python packages.

```bash
pip install -r requirements.txt
```

The required libraries are:

* streamlit
* pandas
* scikit-learn
* plotly

---

## 4. How to Run

Run the following command from the project root directory.

```bash
streamlit run app.py
```

After running the command, the Streamlit application should open in the browser.

If it does not open automatically, check the terminal output and open the displayed local URL manually.

---

## 5. Input Files

The following files must exist in the `data/` folder.

| File                 | Description                                    |
| -------------------- | ---------------------------------------------- |
| `sample_tickets.csv` | Synthetic IT incident and helpdesk ticket data |
| `sample_faq.csv`     | Synthetic internal IT FAQ data                 |
| `sla_policy.csv`     | SLA policy by priority level                   |

---

## 6. Output Files

The processed ticket data is exported to the following file:

```text
results/sample_processed_tickets.csv
```

This file includes additional columns such as:

* priority
* recommended_team
* team_match
* elapsed_hours
* sla_hours
* sla_risk_score
* sla_status

---

## 7. Normal Operation Procedure

1. Confirm that the input CSV files exist in the `data/` folder.
2. Run the Streamlit application.
3. Review dashboard metrics.
4. Check high-risk or violated SLA tickets.
5. Review recommended support teams.
6. Select a ticket and check related FAQs.
7. Review operational insights.
8. Check the exported processed CSV file if needed.

---

## 8. Common Issues and Troubleshooting

### Issue 1: Streamlit command not found

Run the following command:

```bash
pip install streamlit
```

Then run the application again.

```bash
streamlit run app.py
```

---

### Issue 2: ModuleNotFoundError

Install all dependencies again.

```bash
pip install -r requirements.txt
```

---

### Issue 3: CSV file not found

Check whether the following files exist:

```text
data/sample_tickets.csv
data/sample_faq.csv
data/sla_policy.csv
```

If any file is missing, create the file again or restore it from the repository.

---

### Issue 4: Missing column error

Check whether `sample_tickets.csv` includes all required columns.

Required columns:

```text
ticket_id
created_at
category
sub_category
requester_department
impact
urgency
status
assigned_team
resolved_at
description
```

---

### Issue 5: Date parsing error

Use the following datetime format:

```text
YYYY-MM-DD HH:MM
```

Example:

```text
2026-06-01 09:10
```

---

### Issue 6: FAQ search results are not relevant

Possible causes:

* FAQ data is too small.
* Ticket description is too short.
* FAQ questions and answers do not contain related keywords.

Possible improvements:

* Add more FAQ examples.
* Write more detailed FAQ answers.
* Improve ticket descriptions.
* Add category-based filtering before FAQ search.

---

## 9. Maintenance Notes

When updating the system:

* Keep business rules simple and explainable.
* Do not include real company data or personal information.
* Update documentation when changing priority or SLA logic.
* Add new test cases when adding new features.
* Check that the application still runs after modifying CSV formats.

---

## 10. Future Improvements

The current system is designed as a simple local prototype. Future improvements may include:

* Ticket registration form
* SQLite or PostgreSQL database integration
* User authentication
* Slack or email notification for high-risk tickets
* Cloud deployment
* LLM-based response suggestion
* Historical trend analysis
* Monthly SLA performance report
* Role-based dashboard views

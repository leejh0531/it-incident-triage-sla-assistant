# Test Plan

## 1. Overview

This test plan defines basic test cases for the IT Incident Triage & SLA Risk Assistant.

The purpose of testing is to confirm that the system correctly assigns priority, calculates SLA risk, recommends support teams, searches related FAQs, and displays dashboard outputs.

---

## 2. Test Scope

The following functions are included in the test scope:

* CSV data loading
* Ticket priority assignment
* SLA risk score calculation
* SLA status classification
* Responsible team recommendation
* Related FAQ search
* Dashboard display
* Processed CSV export

---

## 3. Functional Test Cases

| Test ID | Function            | Input                         | Expected Output           |
| ------- | ------------------- | ----------------------------- | ------------------------- |
| TC-001  | Priority assignment | impact=High, urgency=High     | priority=Critical         |
| TC-002  | Priority assignment | impact=High, urgency=Medium   | priority=High             |
| TC-003  | Priority assignment | impact=Medium, urgency=High   | priority=High             |
| TC-004  | Priority assignment | impact=Medium, urgency=Medium | priority=Medium           |
| TC-005  | Priority assignment | impact=Low, urgency=Low       | priority=Low              |
| TC-006  | Team routing        | category=Network              | recommended_team=Infra    |
| TC-007  | Team routing        | category=Cloud                | recommended_team=Infra    |
| TC-008  | Team routing        | category=Login                | recommended_team=Helpdesk |
| TC-009  | Team routing        | category=Database             | recommended_team=DB       |
| TC-010  | Team routing        | category=Security             | recommended_team=Security |
| TC-011  | Team routing        | category=Application          | recommended_team=App      |

---

## 4. SLA Risk Test Cases

| Test ID | Condition           | Expected Output                        |
| ------- | ------------------- | -------------------------------------- |
| TC-012  | elapsed=2h, SLA=8h  | risk_score=25%, sla_status=Normal      |
| TC-013  | elapsed=5h, SLA=8h  | risk_score=62.5%, sla_status=Warning   |
| TC-014  | elapsed=7h, SLA=8h  | risk_score=87.5%, sla_status=High Risk |
| TC-015  | elapsed=10h, SLA=8h | risk_score=125%, sla_status=Violated   |
| TC-016  | elapsed=4h, SLA=4h  | risk_score=100%, sla_status=Violated   |

---

## 5. FAQ Search Test Cases

| Test ID | Input Query                 | Expected Result                                                  |
| ------- | --------------------------- | ---------------------------------------------------------------- |
| TC-017  | Users cannot connect to VPN | VPN-related FAQ should be included in top results                |
| TC-018  | User cannot reset password  | Password reset FAQ should be included in top results             |
| TC-019  | CRM system is slow          | Application or CRM-related FAQ should be included in top results |
| TC-020  | Database query timeout      | Database-related FAQ should be included in top results           |
| TC-021  | Access permission request   | Security or access request FAQ should be included in top results |

---

## 6. Dashboard Test Cases

| Test ID | Test Item        | Expected Output                                                                   |
| ------- | ---------------- | --------------------------------------------------------------------------------- |
| TC-022  | Dashboard launch | Streamlit app opens without error                                                 |
| TC-023  | Metric cards     | Total tickets, open tickets, critical tickets, and SLA risk tickets are displayed |
| TC-024  | Category chart   | Tickets by category chart is displayed                                            |
| TC-025  | SLA chart        | SLA status chart is displayed                                                     |
| TC-026  | Ticket table     | Processed ticket table is displayed                                               |
| TC-027  | SLA filter       | Table is filtered by selected SLA status                                          |
| TC-028  | FAQ section      | Related FAQs are displayed for the selected ticket                                |
| TC-029  | Insight section  | Operational insights are displayed                                                |

---

## 7. Data Validation Test Cases

| Test ID | Condition                             | Expected Output                            |
| ------- | ------------------------------------- | ------------------------------------------ |
| TC-030  | Required columns exist in ticket CSV  | Data is loaded successfully                |
| TC-031  | Missing required column in ticket CSV | Error is raised                            |
| TC-032  | Empty resolved_at field               | Ticket is treated as unresolved            |
| TC-033  | Invalid date format                   | Date is converted to NaT or handled safely |
| TC-034  | Empty description                     | System does not crash                      |

---

## 8. Manual Test Procedure

1. Install required packages.

```bash
pip install -r requirements.txt
```

2. Run the Streamlit application.

```bash
streamlit run app.py
```

3. Confirm that the dashboard opens in the browser.
4. Check that all metric cards are displayed.
5. Check that category and SLA charts are displayed.
6. Select different SLA statuses in the filter.
7. Select a ticket in the FAQ search section.
8. Confirm that related FAQs are displayed.
9. Confirm that operational insights are displayed.
10. Confirm that `results/sample_processed_tickets.csv` is created.

---

## 9. Acceptance Criteria

The system is considered complete when:

* The application runs without errors.
* Ticket priority is assigned correctly.
* SLA risk score and SLA status are calculated correctly.
* Responsible teams are recommended correctly.
* Related FAQs are displayed for selected tickets.
* Dashboard metrics and charts are displayed.
* Processed ticket data is exported as CSV.

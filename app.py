import streamlit as st
import pandas as pd
import plotly.express as px

from src.data_loader import load_tickets, load_faq, load_sla_policy
from src.priority_engine import apply_priority
from src.assignment_router import apply_team_recommendation
from src.sla_risk import calculate_sla_risk
from src.faq_search import search_related_faq
from src.insight_generator import generate_insights


st.set_page_config(
    page_title="IT Incident Triage & SLA Risk Assistant",
    layout="wide",
)


@st.cache_data
def load_all_data():
    tickets = load_tickets("data/sample_tickets.csv")
    faq = load_faq("data/sample_faq.csv")
    sla_policy = load_sla_policy("data/sla_policy.csv")
    return tickets, faq, sla_policy


st.title("IT Incident Triage & SLA Risk Assistant")

st.write(
    "This application supports IT operations by assigning incident priority, "
    "calculating SLA risk, recommending responsible teams, and searching related FAQs."
)

tickets, faq, sla_policy = load_all_data()

processed = apply_priority(tickets)
processed = apply_team_recommendation(processed)
processed = calculate_sla_risk(processed, sla_policy)

processed.to_csv("results/sample_processed_tickets.csv", index=False)

st.subheader("Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

total_tickets = len(processed)
open_tickets = len(processed[processed["status"].isin(["Open", "In Progress"])])
critical_tickets = len(processed[processed["priority"] == "Critical"])
sla_risk_tickets = len(processed[processed["sla_status"].isin(["High Risk", "Violated"])])

col1.metric("Total Tickets", total_tickets)
col2.metric("Open / In Progress", open_tickets)
col3.metric("Critical Tickets", critical_tickets)
col4.metric("High Risk / Violated SLA", sla_risk_tickets)

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Tickets by Category")
    category_counts = processed["category"].value_counts().reset_index()
    category_counts.columns = ["category", "count"]
    fig_category = px.bar(category_counts, x="category", y="count")
    st.plotly_chart(fig_category, use_container_width=True)

with right:
    st.subheader("SLA Status")
    sla_counts = processed["sla_status"].value_counts().reset_index()
    sla_counts.columns = ["sla_status", "count"]
    fig_sla = px.pie(sla_counts, names="sla_status", values="count")
    st.plotly_chart(fig_sla, use_container_width=True)

st.divider()

st.subheader("Processed Ticket Table")

selected_status = st.multiselect(
    "Filter by SLA Status",
    options=processed["sla_status"].unique().tolist(),
    default=processed["sla_status"].unique().tolist(),
)

filtered = processed[processed["sla_status"].isin(selected_status)]

st.dataframe(
    filtered[
        [
            "ticket_id",
            "category",
            "sub_category",
            "impact",
            "urgency",
            "priority",
            "status",
            "assigned_team",
            "recommended_team",
            "elapsed_hours",
            "sla_hours",
            "sla_risk_score",
            "sla_status",
            "description",
        ]
    ],
    use_container_width=True,
)

st.divider()

st.subheader("Related FAQ Search")

ticket_options = processed["ticket_id"].tolist()
selected_ticket_id = st.selectbox("Select a ticket", ticket_options)

selected_ticket = processed[processed["ticket_id"] == selected_ticket_id].iloc[0]
st.write("Ticket Description:")
st.info(selected_ticket["description"])

related_faq = search_related_faq(selected_ticket["description"], faq, top_k=3)

st.write("Top Related FAQs")
st.dataframe(related_faq, use_container_width=True)

st.divider()

st.subheader("Operational Insights")

insights = generate_insights(processed)

for insight in insights:
    st.write(f"- {insight}")
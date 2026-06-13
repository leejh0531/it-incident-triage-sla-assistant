def generate_insights(df):
    insights = []

    if df.empty:
        return ["No ticket data available."]

    top_category = df["category"].value_counts().idxmax()
    top_category_count = df["category"].value_counts().max()
    total_count = len(df)
    top_category_ratio = top_category_count / total_count * 100

    insights.append(
        f"{top_category} tickets account for {top_category_ratio:.1f}% of all incidents. "
        f"This area may require operational review or preventive measures."
    )

    risk_df = df[df["sla_status"].isin(["High Risk", "Violated"])]
    if not risk_df.empty:
        top_risk_team = risk_df["recommended_team"].value_counts().idxmax()
        insights.append(
            f"The {top_risk_team} team has the highest number of high-risk or violated SLA tickets. "
            f"Escalation rules or workload balancing may be required."
        )
    else:
        insights.append(
            "No high-risk or violated SLA tickets were detected in the current dataset."
        )

    open_count = len(df[df["status"].isin(["Open", "In Progress"])])
    insights.append(
        f"There are {open_count} unresolved tickets. "
        f"Open and in-progress tickets should be reviewed regularly to prevent SLA violations."
    )

    return insights
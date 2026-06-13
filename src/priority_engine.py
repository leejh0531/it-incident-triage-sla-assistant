def assign_priority(impact: str, urgency: str) -> str:
    impact = str(impact).strip()
    urgency = str(urgency).strip()

    if impact == "High" and urgency == "High":
        return "Critical"
    if impact == "High" and urgency == "Medium":
        return "High"
    if impact == "Medium" and urgency == "High":
        return "High"
    if impact == "Medium" and urgency == "Medium":
        return "Medium"
    return "Low"


def apply_priority(df):
    df = df.copy()
    df["priority"] = df.apply(
        lambda row: assign_priority(row["impact"], row["urgency"]),
        axis=1,
    )
    return df
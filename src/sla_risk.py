import pandas as pd


def get_reference_time(df: pd.DataFrame):
    resolved_max = df["resolved_at"].max()
    created_max = df["created_at"].max()

    if pd.notna(resolved_max):
        return max(resolved_max, created_max)

    return created_max


def classify_risk(score: float) -> str:
    if score >= 100:
        return "Violated"
    if score >= 80:
        return "High Risk"
    if score >= 50:
        return "Warning"
    return "Normal"


def calculate_sla_risk(df: pd.DataFrame, sla_policy: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    sla_map = dict(zip(sla_policy["priority"], sla_policy["sla_hours"]))
    reference_time = get_reference_time(df)

    elapsed_hours = []

    for _, row in df.iterrows():
        end_time = row["resolved_at"] if pd.notna(row["resolved_at"]) else reference_time
        elapsed = (end_time - row["created_at"]).total_seconds() / 3600
        elapsed_hours.append(round(elapsed, 2))

    df["elapsed_hours"] = elapsed_hours
    df["sla_hours"] = df["priority"].map(sla_map)
    df["sla_risk_score"] = (df["elapsed_hours"] / df["sla_hours"] * 100).round(1)
    df["sla_status"] = df["sla_risk_score"].apply(classify_risk)

    return df
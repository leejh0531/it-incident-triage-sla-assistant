import pandas as pd


REQUIRED_TICKET_COLUMNS = [
    "ticket_id",
    "created_at",
    "category",
    "sub_category",
    "requester_department",
    "impact",
    "urgency",
    "status",
    "assigned_team",
    "resolved_at",
    "description",
]


def load_tickets(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    missing_columns = [col for col in REQUIRED_TICKET_COLUMNS if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing ticket columns: {missing_columns}")

    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
    df["resolved_at"] = pd.to_datetime(df["resolved_at"], errors="coerce")

    df["description"] = df["description"].fillna("")
    df["assigned_team"] = df["assigned_team"].fillna("Unassigned")

    return df


def load_faq(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    df["question"] = df["question"].fillna("")
    df["answer"] = df["answer"].fillna("")

    return df


def load_sla_policy(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df
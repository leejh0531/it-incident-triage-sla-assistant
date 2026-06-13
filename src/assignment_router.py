TEAM_RULES = {
    "Network": "Infra",
    "Cloud": "Infra",
    "Login": "Helpdesk",
    "Database": "DB",
    "Security": "Security",
    "Application": "App",
}


def recommend_team(category: str) -> str:
    return TEAM_RULES.get(str(category).strip(), "Helpdesk")


def apply_team_recommendation(df):
    df = df.copy()
    df["recommended_team"] = df["category"].apply(recommend_team)
    df["team_match"] = df["assigned_team"] == df["recommended_team"]
    return df
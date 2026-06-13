import csv
import random
from datetime import datetime, timedelta

random.seed(42)

OUTPUT_PATH = "data/sample_tickets.csv"
NUM_TICKETS = 100

categories = {
    "Network": ["VPN", "Office Wi-Fi", "Proxy", "Firewall"],
    "Login": ["Password", "MFA", "Account Lock", "SSO"],
    "Database": ["Query Error", "Connection", "Timeout", "Backup"],
    "Application": ["Performance", "Bug", "Error Message", "Data Sync"],
    "Security": ["Permission", "Access Request", "Suspicious Login", "Shared Folder"],
    "Cloud": ["Server Alert", "Storage", "CPU Usage", "Deployment"],
}

departments = [
    "Sales",
    "HR",
    "Finance",
    "Engineering",
    "Marketing",
    "Operations",
    "IT",
    "Legal",
]

impact_values = ["High", "Medium", "Low"]
urgency_values = ["High", "Medium", "Low"]
status_values = ["Open", "In Progress", "Resolved"]

team_rules = {
    "Network": "Infra",
    "Cloud": "Infra",
    "Login": "Helpdesk",
    "Database": "DB",
    "Security": "Security",
    "Application": "App",
}

descriptions = {
    "Network": [
        "Users cannot connect to VPN during remote work.",
        "Office Wi-Fi is unstable in the meeting room.",
        "Users cannot access external websites through the proxy.",
        "Firewall configuration may be blocking business applications.",
    ],
    "Login": [
        "Employee cannot log in to the internal system.",
        "User cannot complete multi-factor authentication.",
        "User account is locked after multiple login attempts.",
        "Single sign-on fails when accessing the HR system.",
    ],
    "Database": [
        "Monthly report query fails with timeout error.",
        "Application cannot connect to the production database.",
        "Database backup job did not complete successfully.",
        "Slow query performance is affecting business reports.",
    ],
    "Application": [
        "CRM system response time is very slow.",
        "Inventory system shows incorrect stock values.",
        "Application shows an unexpected error message.",
        "Customer data is not synchronized correctly.",
    ],
    "Security": [
        "User requests access to a shared folder.",
        "Suspicious login attempt was detected.",
        "New employee needs access to internal documents.",
        "Permission settings need to be reviewed.",
    ],
    "Cloud": [
        "CPU usage alert triggered on production server.",
        "Cloud storage usage reached the warning threshold.",
        "Deployment failed in the staging environment.",
        "Server monitoring alert was triggered.",
    ],
}


def choose_impact_and_urgency():
    """
    Generate impact and urgency values with a slightly realistic distribution.
    Medium and Low issues appear more frequently than High issues.
    """
    impact = random.choices(
        impact_values,
        weights=[25, 45, 30],
    )[0]

    urgency = random.choices(
        urgency_values,
        weights=[30, 45, 25],
    )[0]

    return impact, urgency


def generate_created_at():
    """
    Generate ticket creation time within a two-week period.
    """
    base_date = datetime(2026, 6, 1, 8, 0)

    random_days = random.randint(0, 13)
    random_hours = random.randint(0, 10)
    random_minutes = random.choice([0, 10, 20, 30, 40, 50])

    return base_date + timedelta(
        days=random_days,
        hours=random_hours,
        minutes=random_minutes,
    )


def generate_resolved_at(created_at, status, impact, urgency):
    """
    Generate resolved_at only for resolved tickets.
    Open and In Progress tickets keep resolved_at empty.
    """
    if status != "Resolved":
        return ""

    if impact == "High" and urgency == "High":
        hours = random.uniform(1, 8)
    elif impact == "High" or urgency == "High":
        hours = random.uniform(2, 14)
    elif impact == "Medium" or urgency == "Medium":
        hours = random.uniform(4, 30)
    else:
        hours = random.uniform(10, 80)

    resolved_at = created_at + timedelta(hours=hours)
    return resolved_at.strftime("%Y-%m-%d %H:%M")


def choose_assigned_team(correct_team):
    """
    Assign the correct team in most cases.
    Some tickets are intentionally assigned to a different team
    so that the recommendation function has meaningful output.
    """
    if random.random() < 0.85:
        return correct_team

    all_teams = ["Infra", "Helpdesk", "DB", "Security", "App"]
    wrong_teams = [team for team in all_teams if team != correct_team]

    return random.choice(wrong_teams)


rows = []

for i in range(1, NUM_TICKETS + 1):
    ticket_id = f"T{i:03d}"

    category = random.choice(list(categories.keys()))
    sub_category = random.choice(categories[category])
    requester_department = random.choice(departments)

    impact, urgency = choose_impact_and_urgency()

    status = random.choices(
        status_values,
        weights=[25, 25, 50],
    )[0]

    created_at = generate_created_at()
    correct_team = team_rules[category]
    assigned_team = choose_assigned_team(correct_team)

    resolved_at = generate_resolved_at(
        created_at=created_at,
        status=status,
        impact=impact,
        urgency=urgency,
    )

    description = random.choice(descriptions[category])

    rows.append(
        {
            "ticket_id": ticket_id,
            "created_at": created_at.strftime("%Y-%m-%d %H:%M"),
            "category": category,
            "sub_category": sub_category,
            "requester_department": requester_department,
            "impact": impact,
            "urgency": urgency,
            "status": status,
            "assigned_team": assigned_team,
            "resolved_at": resolved_at,
            "description": description,
        }
    )

fieldnames = [
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

with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Generated {NUM_TICKETS} synthetic IT tickets: {OUTPUT_PATH}")
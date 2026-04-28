from api.models import Report
from matching.priority import get_priority_reports


def ask_rag(question):
    question = str(question).lower()

    reports = Report.objects.all()

    if "priority" in question or "urgent" in question:
        priority_reports = get_priority_reports(reports)

        if not priority_reports:
            return "No reports found."

        top = priority_reports[0]

        return (
            f"Top priority task is '{top['title']}' in {top['location']} "
            f"with priority score {top['priority_score']}. "
            f"Category: {top['category']}. Status: {top['status']}."
        )

    if "pending" in question:
        pending = Report.objects.filter(status="pending")
        return f"There are {pending.count()} pending reports."

    if "assigned" in question:
        assigned = Report.objects.filter(status="assigned")
        return f"There are {assigned.count()} assigned reports."

    return "Ask about priority tasks, urgent tasks, pending reports, or assigned reports."

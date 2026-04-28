def calculate_priority(report):
    return report.urgency * 4 + report.severity * 3 + report.people_affected * 2


def get_priority_reports(reports):
    data = []

    for report in reports:
        data.append({
            "id": report.id,
            "title": report.title,
            "description": report.description,
            "location": report.location,
            "category": report.category,
            "status": report.status,
            "priority_score": calculate_priority(report)
        })

    return sorted(data, key=lambda x: x["priority_score"], reverse=True)
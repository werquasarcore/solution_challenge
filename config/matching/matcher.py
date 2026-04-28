def match_volunteers(report, volunteers):
    matches = []

    report_category = (report.category or "").lower().strip()
    report_location = (report.location or "").lower().strip()

    for volunteer in volunteers:
        if not volunteer.available:
            continue

        volunteer_skill = (volunteer.skill or "").lower().strip()
        volunteer_location = (volunteer.location or "").lower().strip()

        score = 0

        if report_category in volunteer_skill:
            score += 5

        if report_location == volunteer_location:
            score += 3

        if score > 0:
            matches.append({
                "id": volunteer.id,
                "name": volunteer.name,
                "skill": volunteer.skill,
                "location": volunteer.location,
                "available": volunteer.available,
                "match_score": score
            })

    return sorted(matches, key=lambda x: x["match_score"], reverse=True)
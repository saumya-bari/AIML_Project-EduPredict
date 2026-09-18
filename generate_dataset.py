def recommendations(record, risk_level):
    suggestions = []

    if record["attendance"] < 75:
        suggestions.append("Improve attendance and attend missed classes.")
    if record["study_hours"] < 4:
        suggestions.append("Create a daily study schedule with focused study blocks.")
    if record["assignment_completion"] < 75:
        suggestions.append("Complete pending assignments before deadlines.")
    if record["internal_marks"] < 60:
        suggestions.append("Revise weak topics and discuss difficulties with the teacher.")
    if record["previous_gpa"] < 6:
        suggestions.append("Use academic mentoring and regular progress reviews.")
    if record["sleep_hours"] < 6:
        suggestions.append("Maintain a consistent and healthier sleep routine.")
    if record["backlogs"] > 0:
        suggestions.append("Prepare a recovery plan for backlog subjects.")

    if not suggestions:
        suggestions.append("Maintain the current academic routine and monitor progress.")

    prefix = "Priority action: " if risk_level == "High" else ("Monitor: " if risk_level == "Medium" else "Maintain: ")
    return [prefix + item for item in suggestions]

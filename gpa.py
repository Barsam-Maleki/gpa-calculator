def calculate_gpa(courses):
    """courses is a list of (grade, units)"""
    if not courses:
        raise ValueError("Course list is empty")
    total_points = 0
    total_units = 0
    for grade, units in courses:
        total_points += grade * units
        total_units += units
    return round(total_points / total_units, 2)


def is_passed(grade):
    """A course is passed with a grade of 10 or more."""
    return grade >= 10
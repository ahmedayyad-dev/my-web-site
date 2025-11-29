"""
Utility functions - Heavy calculations and business logic in Python
"""
from datetime import datetime
from typing import Dict, Any


def calculate_age_from_date(birth_date: str) -> int:
    """
    Calculate age from birth date string
    Args:
        birth_date: Date in format "YYYY-MM-DD"
    Returns:
        Age in years
    """
    birth = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.now()

    age = today.year - birth.year

    # Adjust if birthday hasn't occurred this year
    if (today.month, today.day) < (birth.month, birth.day):
        age -= 1

    return age


def calculate_experience_years(start_date: str) -> int:
    """
    Calculate years of experience from start date
    Args:
        start_date: Date in format "YYYY-MM-DD"
    Returns:
        Years of experience (minimum 1)
    """
    start = datetime.strptime(start_date, "%Y-%m-%d")
    today = datetime.now()

    years = today.year - start.year

    # Adjust if anniversary hasn't occurred this year
    if (today.month, today.day) < (start.month, start.day):
        years -= 1

    return max(1, years)


def calculate_days_since(date_str: str) -> int:
    """Calculate days since a specific date"""
    date = datetime.strptime(date_str, "%Y-%m-%d")
    today = datetime.now()
    return (today - date).days


def calculate_months_since(date_str: str) -> int:
    """Calculate months since a specific date"""
    date = datetime.strptime(date_str, "%Y-%m-%d")
    today = datetime.now()

    months = (today.year - date.year) * 12 + (today.month - date.month)

    if today.day < date.day:
        months -= 1

    return max(0, months)


def format_date_ar(date_str: str) -> str:
    """Format date in Arabic"""
    date = datetime.strptime(date_str, "%Y-%m-%d")
    months_ar = [
        "يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو",
        "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"
    ]
    return f"{date.day} {months_ar[date.month - 1]} {date.year}"


def format_date_en(date_str: str) -> str:
    """Format date in English"""
    date = datetime.strptime(date_str, "%Y-%m-%d")
    return date.strftime("%B %d, %Y")


def calculate_detailed_age(birth_date: str) -> Dict[str, Any]:
    """
    Calculate detailed age breakdown
    Returns years, months, days
    """
    birth = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.now()

    years = today.year - birth.year
    months = today.month - birth.month
    days = today.day - birth.day

    # Adjust for negative days
    if days < 0:
        months -= 1
        # Get days in previous month
        if today.month == 1:
            prev_month_days = 31
        else:
            from calendar import monthrange
            prev_month_days = monthrange(today.year, today.month - 1)[1]
        days += prev_month_days

    # Adjust for negative months
    if months < 0:
        years -= 1
        months += 12

    return {
        "years": years,
        "months": months,
        "days": days,
        "total_days": (today - birth).days,
        "total_months": years * 12 + months
    }


def calculate_detailed_experience(start_date: str) -> Dict[str, Any]:
    """
    Calculate detailed experience breakdown
    Returns years, months, days
    """
    return calculate_detailed_age(start_date)


def generate_timeline(events: list) -> list:
    """
    Generate timeline with calculated durations
    Events format: [{"date": "YYYY-MM-DD", "title": "...", "description": "..."}]
    """
    timeline = []

    for event in sorted(events, key=lambda x: x["date"], reverse=True):
        days_ago = calculate_days_since(event["date"])
        months_ago = calculate_months_since(event["date"])
        years_ago = months_ago // 12

        timeline.append({
            **event,
            "days_ago": days_ago,
            "months_ago": months_ago,
            "years_ago": years_ago,
            "formatted_date_ar": format_date_ar(event["date"]),
            "formatted_date_en": format_date_en(event["date"])
        })

    return timeline


def calculate_productivity_stats(start_date: str) -> Dict[str, Any]:
    """
    Calculate productivity statistics
    """
    days = calculate_days_since(start_date)
    months = calculate_months_since(start_date)
    years = months // 12

    # Estimate working days (excluding weekends and holidays ~30%)
    working_days = int(days * 0.7)

    return {
        "total_days": days,
        "total_months": months,
        "total_years": years,
        "working_days_estimate": working_days,
        "working_hours_estimate": working_days * 8,
        "weeks": days // 7
    }

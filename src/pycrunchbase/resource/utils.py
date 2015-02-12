from datetime import datetime


def safe_int(int_like):
    try:
        return int(int_like)
    except TypeError:
        return None


def parse_date(datelike):
    """Helper for parsing dates in Organization properties"""
    try:
        return datetime.strptime(datelike, "%Y-%m-%d")
    except ValueError:
        return datelike

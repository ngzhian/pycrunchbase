def safe_int(int_like):
    try:
        return int(int_like)
    except TypeError:
        return None

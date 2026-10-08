def rate(passed, attempted):
    return round(passed / max(attempted, 1), 2)

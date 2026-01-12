
def get_total(payload: dict):
    """
    payload esperado:
    {
        "costs": {"socks": 5, "shoes": 60},
        "items": ["socks", "shoes"],
        "tax": 0.09
    }
    """
    costs = payload["costs"]
    items = payload["items"]
    tax = payload["tax"]

    subtotal = sum(costs[item] for item in items if item in costs)
    total = subtotal * (1 + tax)

    return round(total, 2)
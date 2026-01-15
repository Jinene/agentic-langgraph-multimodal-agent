def calculator(expression: str) -> str:
    try:
        return str(eval(expression))
    except Exception:
        return "Invalid mathematical expression"

def suggest_optimizations(code: str):
    """
    Analyzes Python code text and suggests potential optimizations.
    This is a lightweight rule-based static analyzer (no execution required).

    Args:
        code (str): The code to analyze.

    Returns:
        list[str]: A list of suggestion strings.
    """
    suggestions = []

    if "for" in code and ".append(" in code:
        suggestions.append("Consider using list comprehensions instead of appending in loops.")
    if "open(" in code and "read()" in code:
        suggestions.append("Consider using context managers or buffered reads for large files.")
    if "== None" in code:
        suggestions.append("Use 'is None' instead of '== None' for better readability.")
    if "==" in code and "True" in code:
        suggestions.append("Avoid comparing to True directly; use 'if variable:' instead.")
    if "range(len(" in code:
        suggestions.append("Use 'enumerate()' instead of 'range(len(...))' for cleaner loops.")
    if "time.sleep(" in code:
        suggestions.append("Avoid unnecessary time.sleep() in production code for better performance.")

    if not suggestions:
        suggestions.append("No obvious optimizations detected. Nice work!")

    return suggestions

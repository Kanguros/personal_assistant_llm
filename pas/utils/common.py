from typing import Any


def isinstanceany(obj: Any, class_list: list[type]) -> bool:
    """Returns True if obj is an instance of the classes in class_list"""
    return any(isinstance(obj, cls) for cls in class_list)


def str_to_int(inp: str | None) -> int | None:
    """
    Safely converts a string value to integer.
    Args:
        inp: input string

    Returns: input string as int if possible, None if not
    """
    if inp is None:
        return None
    try:
        return int(inp)
    except Exception:
        return None


def is_empty(val: Any) -> bool:
    """Returns True if val is None or empty"""
    if val is None or len(val) == 0 or val == "":
        return True
    return False

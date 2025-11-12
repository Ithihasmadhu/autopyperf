from .profiler import profile_function
from .analyzer import profile_script
from .suggestions import suggest_optimizations

__all__ = [
    "profile_function",
    "profile_script",
    "suggest_optimizations"
]

import cProfile
import pstats
import io
import os


def profile_script(script_path: str):
    """
    Profiles an entire Python script and prints the top 10 slowest functions.
    
    Args:
        script_path (str): Path to the Python script file.
    
    Example:
        profile_script("examples/example_script.py")
    """
    if not os.path.exists(script_path):
        print(f"[autopyperf] Error: Script '{script_path}' not found.")
        return

    pr = cProfile.Profile()
    pr.enable()

    with open(script_path, "rb") as f:
        code = compile(f.read(), script_path, "exec")
        exec(code, {})

    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
    ps.print_stats(10)

    print("[autopyperf] Top 10 performance hotspots:\n")
    print(s.getvalue())

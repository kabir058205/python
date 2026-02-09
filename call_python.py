import subprocess
import sys
import os

DEFAULT_IFSC = "SBIN0000001"


def run_script(script_name, args=None):
    if args is None:
        args = []

    print(f"\n=== RUNNING: {script_name} ===")

    if not os.path.exists(script_name):
        raise FileNotFoundError(f"{script_name} not found")

    subprocess.run(
        [sys.executable, script_name] + args,
        check=True
    )


def ask_ifsc_code():
    value = input(
        f"Enter IFSC code (press Enter for default {DEFAULT_IFSC}): "
    ).strip()
    return value or DEFAULT_IFSC


def main():
    print("=== MASTER PIPELINE STARTED ===")

    run_script("hello.py")
    run_script("Pandas_basic_step.py")
    run_script("pandas_advance_step.py")
    run_script("numpy_basics_step.py")
    run_script("numpy_advance_step.py")
    run_script("check_missing.py")

    ifsc_code = ask_ifsc_code()
    run_script("Ifsc.py", args=[ifsc_code])

    print("\n=== MASTER PIPELINE COMPLETED SUCCESSFULLY ===")


if __name__ == "__main__":
    main()

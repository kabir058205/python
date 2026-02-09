import sys
import subprocess
import os
import re
from importlib.metadata import version, PackageNotFoundError


def parse_args():
    quiet = True
    force_install = False
    script_args = []

    for arg in sys.argv[1:]:
        if arg == "--verbose":
            quiet = False
        elif arg == "--force-install":
            force_install = True
        else:
            script_args.append(arg)

    if not script_args:
        raise ValueError("Usage: python master_run.py <script.py>")

    return quiet, force_install, script_args


def get_requirements_file():
    if os.path.exists("requirements-pip.txt"):
        return "requirements-pip.txt"
    if os.path.exists("requirements.txt"):
        return "requirements.txt"
    return None


def install_dependencies(req_file, force=False, quiet=True):
    if not req_file:
        return

    missing = []
    with open(req_file) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            pkg = re.split(r"[<=>!~]", line)[0]
            try:
                version(pkg)
            except PackageNotFoundError:
                missing.append(pkg)

    if missing or force:
        if not quiet:
            print("Installing dependencies...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", req_file],
            check=True
        )


def run_script(script, args):
    subprocess.run([sys.executable, script] + args, check=True)


def main():
    quiet, force_install, args = parse_args()
    script, script_args = args[0], args[1:]

    if not os.path.exists(script):
        raise FileNotFoundError(script)

    install_dependencies(get_requirements_file(), force_install, quiet)
    run_script(script, script_args)


if __name__ == "__main__":
    main()

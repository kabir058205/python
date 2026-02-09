# Master Python Runner

This project demonstrates how to use a master Python script to execute
other Python scripts by passing them as parameters.

## How to run

```bash
python master_run.py scripts/hello.py

This folder contains a small helper to run example Python scripts
and manage lightweight dependency installation for local testing.

Files
-----

- `master_run.py` — Small launcher that runs another Python script passed
	as an argument. It uses the running Python interpreter (`sys.executable`) and
	optionally installs dependencies from a pip-style requirements file.
- `requirements.txt` — Pip-format requirements (e.g. `pandas`).
- `requirements-pip.txt` — alternate/explicit pip requirements (preferred by
	the launcher when present).
- `requirements-doc.md` — documentation-style requirements that were
	preserved from earlier commits.

Usage
-----

Run a script from inside this folder:

```bash
cd python
python3 master_run.py pandas_step.py
```

Run from the repository root using the convenience script:

```bash
./run_master.sh pandas_step.py
```

Notes
-----

- The launcher will install dependencies only when a clean pip-style
	requirements file exists. It avoids installing when `requirements.txt`
	appears to be markdown or documentation to prevent pip parse errors.
- If you need the launcher to accept additional arguments for the target
	script, we can extend it to forward `--` arguments.
- Pip behavior: the launcher disables pip's automatic version-check notice
	and runs `pip install` in quiet mode to reduce noise. If you prefer to
	see full pip output or the upgrade notice, set `PIP_DISABLE_PIP_VERSION_CHECK`
	to `0` in your environment or run `pip` manually.
 - Conditional installs: the launcher now inspects the pip requirements file
	and only runs `pip install` when packages are missing. This makes repeated
	runs fast and avoids unnecessary network calls.
 - CLI flags:
	- Behavior: launcher is quiet by default so the target script's output
		appears immediately.
	- `--verbose` — show pre-run messages (running script, dependency checks).
	- `--quiet` — explicit quiet mode (same as default).
	- `--force-install` — forces `pip install -r` even when dependencies appear
		satisfied.

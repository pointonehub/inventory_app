# Copilot / AI Agent Instructions — inventory_app

Purpose: quick, actionable guidance so an AI coding agent can be productive immediately.

- **Project entry point:** `main.py` at the repository root is the only source file currently present. Treat `main.py` as the primary focus for edits and feature additions.
- **Run locally:** execute `python main.py` from the project root. There is no CI, test suite, or dependency manifest detected.
- **Dependencies:** no `requirements.txt` or `pyproject.toml` found. If you add external packages, also add a `requirements.txt` (pip) or `pyproject.toml` (poetry/PEP 621).

- **Architecture & scope:** this is a single-file script (small CLI/utility). Expect simple linear flow and in-file functions rather than a multi-module package. For larger features, propose converting to a package layout (create `inventory_app/` package, add `__main__.py`, add tests).

- **Where to look for behavior to change:** modify `main.py`. Search for an `if __name__ == "__main__":` block or top-level function definitions to identify the entry path.

- **When adding features:**
  - Add small, focused functions and unit tests under a new `tests/` directory.
  - Add a `requirements.txt` if external libs are required.
  - If adding a CLI interface, prefer `argparse` and keep usage examples in `README.md`.

- **Testing & verification:** no tests found. Minimal verification is running `python main.py` and validating expected stdout/behavior. Add automated tests when changing logic.

- **Style & commits:** follow the existing minimal style — keep changes small and focused. Provide a short PR description explaining the why and list manual verification steps.

- **Examples from this repo:**
  - Edit the script: modify `main.py` to change behavior.
  - Add dependencies: create `requirements.txt` and update README with run instructions.

If any section is unclear or you want richer guidance (for example: preferred testing framework, CI, or packaging convention), tell me which area to expand. 

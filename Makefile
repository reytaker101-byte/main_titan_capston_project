# Declares these targets as commands, not actual files.
# This ensures they run whenever you execute them using make.
.PHONY: install test compile blue-green-demo

# INSTALL:
# Installs all Python dependencies listed in requirements.txt.
# Run using: make install
install:
	python -m pip install -r requirements.txt

# TEST:
# Runs the automated tests located in ai/tests.
# Helps verify that the AI-SRE Guardian code behaves as expected.
# Run using: make test
test:
	python -m pytest -q ai/tests

# COMPILE:
# Checks Python files for syntax errors without executing the application.
# -q keeps the output concise.
# Covers AI, application services, and notification code.
# Run using: make compile
compile:
	python -m compileall -q ai services notifications

# BLUE-GREEN DEMO:
# Executes the script that switches the active Blue/Green environment.
# Use only when you intentionally want to perform this operation.
# Review the script and target environment before running it.
# Run using: make blue-green-demo
blue-green-demo:
	bash devops-infra/blue-green/switch_color.sh

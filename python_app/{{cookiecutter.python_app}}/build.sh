#!/bin/bash
set -e

USAGE="
Usage:
    $0 <command>

Commands:
    dev     install package for development
    tar     build tar
    wheel   build wheel
    test    run tests
"

if [[ $# -ne 1 ]]; then
    echo "$USAGE"
    exit 2
fi

PY="${PY:-python}"
VENVPY="${VENVPY:-./venv/Scripts.python.exe}"

case "$1" in
dev)
    "$PY" -m venv venv
    "$VENVPY" -m pip install -r requirements.txt
    "$VENVPY" -m pip install -e .
    ;;
tar)
    "$VENVPY" setup.py sdist
    ;;
wheel)
    "$VENVPY" setup.py bdist_wheel
    ;;
test)
    "$VENVPY" -m pytest -v tests
    ;;
*)
    echo
    echo Invalid command
    echo "$USAGE"
    exit 2
    ;;
esac
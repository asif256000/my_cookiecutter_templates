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

case "$1" in
dev)
    "$PY" -m venv venv
    "$PY" -m pip install -r requirements.txt
    "$PY" -m pip install -e .
    ;;
tar)
    "$PY" setup.py sdist
    ;;
wheel)
    "$PY" setup.py bdist_wheel
    ;;
test)
    "$PY" -m pytest -v tests
    ;;
*)
    echo
    echo Invalid command
    echo "$USAGE"
    exit 2
    ;;
esac
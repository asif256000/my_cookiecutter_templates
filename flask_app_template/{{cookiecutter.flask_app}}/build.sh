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

# TODO: Check which type of variables are reqd here: ENV{}, SHELL(), or NORMAL.
PY="${PY:-python}"
CURDIR="$(pwd)/"
SCRDIR="${CURDIR}/venv/Scripts/"
PYVENV="${SCRDIR}/python"

case "$1" in
dev)
    "$PY" -m venv venv
    source "$SCRDIR"/activate
    "$PYVENV" -m pip install -r requirements.txt
    "$PYVENV" -m pip install -e .
    ;;
tar)
    "$PYVENV" setup.py sdist
    ;;
wheel)
    "$PYVENV" setup.py bdist_wheel
    ;;
test)
    "$PYVENV" -m pytest -v tests
    ;;
*)
    echo
    echo Invalid command
    echo "$USAGE"
    exit 2
    ;;
esac
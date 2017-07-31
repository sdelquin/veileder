#!/bin/bash
# Master script.

cd "$(dirname "$0")"
source $HOME/.virtualenvs/veileder/bin/activate
python main.py

#!/usr/bin/env bash

# The main idea here is to separate the "engine" from the actual "gameplay".
# In src/, we will have a subdir named engine/.
# Into the engine folder will be things like events processing, context switching, fps, spritesheet class etc.
# Files up in src/ will hook into the engine stuff.

cd "$(dirname "$0")" || exit 1
python3 src/main.py

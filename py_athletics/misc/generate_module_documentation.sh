#!/bin/bash
export PYTHONPATH=${PYTHONPATH}:${HOME}/py_athletics/src/
cd ~/py_athletics
pdoc3 py_athletics -o /py_athletics/documents/modules/html --html --force
pdoc3 py_athletics -o /py_athletics/documents/modules/md --force

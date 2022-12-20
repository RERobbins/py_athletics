#!/bin/bash

cd ~/py_athletics/py_athletics/src
enscript -GEpython --color py_athletics.py           -o - | ps2pdf - ../documents/pdf-source-listings/py_athletics.pdf
enscript -GEpython --color activity/activity.py      -o - | ps2pdf - ../documents/pdf-source-listings/activity.pdf
enscript -GEpython --color athlete/athlete.py        -o - | ps2pdf - ../documents/pdf-source-listings/athlete.pdf
enscript -GEpython --color goal/goal.py              -o - | ps2pdf - ../documents/pdf-source-listings/goal.pdf
enscript -GEpython --color shell/shell.py            -o - | ps2pdf - ../documents/pdf-source-listings/shell.pdf
enscript -GEpython --color helpers/garmin_helpers.py -o - | ps2pdf - ../documents/pdf-source-listings/garmin_helpers.pdf
enscript -GEpython --color helpers/helpers.py        -o - | ps2pdf - ../documents/pdf-source-listings/helpers.pdf

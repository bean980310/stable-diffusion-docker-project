#!/bin/bash
set -e

export HF_HOME="/app"

cd /app/Fooocus

if [[ ${PRESET} ]]
then
    python3 entry_with_update.py --listen --port 7860 --preset ${PRESET}
else
    python3 entry_with_update.py --listen --port 7860
fi
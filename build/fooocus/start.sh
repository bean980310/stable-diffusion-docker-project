#!/bin/bash
set -e

export HF_HOME="/app"

cd /app/Fooocus

if [[ ${PRESET} ]]
then
    nohup python3 entry_with_update.py --listen --port 7860 --preset ${PRESET} > /workspace/logs/fooocus.log 2>&1 &
else
    nohup python3 entry_with_update.py --listen --port 7860 > /workspace/logs/fooocus.log 2>&1 &
fi
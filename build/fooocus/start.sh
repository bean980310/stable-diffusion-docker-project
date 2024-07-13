#!/bin/bash

export HF_HOME="/app"

cd /app/Fooocus

if [[ ${PRESET} ]]
then
    echo "Starting Fooocus using preset: ${PRESET}"
    nohup python3 entry_with_update.py --listen --port 3001 --preset ${PRESET} > /workspace/logs/fooocus.log 2>&1 &
else
    echo "Starting Fooocus using defaults"
    nohup python3 entry_with_update.py --listen --port 3001 > /workspace/logs/fooocus.log 2>&1 &
fi
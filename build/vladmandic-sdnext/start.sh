#!/bin/bash
set -e

export HF_HOME="/app"

cd /app/automatic
nohup ./webui.sh -f > /app/sdnext.log 2>&1 &
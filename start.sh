#!/usr/bin/env bash

# Figure out how many processes to serve based on the number
# of logical cores, assuming not many. Most recommendations 
# say logical cores + 1
num_cpu=2
if [[ $(uname) = 'Darwin' ]]; then
    num_cpu=$(sysctl -n hw.logicalcpu_max)
else
    num_cpu=$(lscpu -p | egrep -v '^#' | wc -l)
fi
workers=$(($num_cpu + 1))

echo "Starting server for ${PY_ENV:=prod} with $num_cpu workers."

cd src
gunicorn --bind localhost:8080 --workers $workers --worker-class egg:meinheld#gunicorn_worker server:app --reload

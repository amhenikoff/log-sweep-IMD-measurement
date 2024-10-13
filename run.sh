#!/bin/bash

trap 'kill $(jobs -p); exit' SIGINT

jupyter nbconvert --to notebook --execute generate_stimulus_signal.ipynb &&
python3 play.py &
python3 record.py &

wait
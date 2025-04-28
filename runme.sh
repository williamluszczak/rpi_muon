#!/usr/bin/bash

interrupt() {
  kill $PID1
  exit
}

trap interrupt SIGINT

while true; do
  python3 take_data.py $1
  PID1=$!
done

echo "Bash script finished running at $(date)"

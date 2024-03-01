#!/bin/sh
# a=`ls`
# echo ${a}
rm -r ${PWD}/temp_json
mkdir -p -- "temp_json"
rm -r ${PWD}/images
mkdir -p -- "images"
mkdir -p -- "images/output"
python3 ${PWD}/cleanup.py
mkdir -p -- "temp_json"
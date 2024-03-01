#!/bin/bash

# Update package lists
sudo apt-get update

# Install libpcap-dev
sudo apt-get install -y libpcap-dev

# Install python packages using pip
pip install scipy matplotlib
pip install -r requirements.txt

# Install json-c
sudo apt-get install -y libjson-c-dev
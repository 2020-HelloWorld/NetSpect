#!/bin/sh

# Function to handle SIGINT signal
cleanup() {
    echo "Caught SIGINT, cleaning up..."
    
    # Kill all background processes
    kill 0
    
    # Exit the script
    exit 1
}
# Trap SIGINT and call the cleanup function
trap cleanup SIGINT
${PWD}/ttl_detect/packet_capture > "${PWD}/temp_json/layer1_logs.txt" 
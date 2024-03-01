import json
import subprocess

# Load JSON data from file
with open("./temp_json/currently_covert.json", "r") as json_file:
    data = json.load(json_file)

# Construct the command based on JSON data
for key, value in data.items():
    source_ip, dest_ip = key.split(" - ")

    command = f'echo "{source_ip} {dest_ip} {max(value["TTL_Values"])}" > /sys/kernel/my_module/allowed_ips'
    print(command)
    # Execute the command
    subprocess.run(command, shell=True)

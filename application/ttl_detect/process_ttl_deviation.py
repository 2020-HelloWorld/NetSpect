import json

# Initialize a dictionary to store TTL values for each flow
ttl_dict = {}

# Load the JSON data from the file
with open("./temp_json/packet_data_TTL.json", "r") as json_file:
    for line in json_file:
        packet_data = json.loads(line)

        # Extract relevant information
        source_ip = packet_data["source_ip"]
        dest_ip = packet_data["destination_ip"]
        ttl = packet_data["ttl"]

        # Create a key in the format "(source IP - destination IP)"
        flow_key = f"{source_ip} - {dest_ip}"

        # Initialize an empty set for the flow if it doesn't exist
        if flow_key not in ttl_dict:
            ttl_dict[flow_key] = set()

        # Add the TTL value to the set
        ttl_dict[flow_key].add(ttl)

# Print or further process the TTL values for each flow
# for flow, ttl_values in ttl_dict.items():
#     if len(ttl_values)>1:

#         print(f"Flow: {flow}, TTL Values: {', '.join(map(str, ttl_values))}")

output_data = {}

for flow, ttl_values in ttl_dict.items():
    if len(ttl_values) > 1:
        output_data[flow] = {"TTL_Values": list(ttl_values)}

with open("./temp_json/currently_covert.json", "w") as output_file:
    json.dump(output_data, output_file, indent=2)

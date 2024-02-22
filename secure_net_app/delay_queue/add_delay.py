import subprocess
import json

with open("./temp_json/flow_result.json", "r") as json_file:
    data = json.load(json_file)

NETCARD = "enp0s3"

# Delete the existing tc qdisc and add a new HTB qdisc
subprocess.run(f"tc qdisc del dev {NETCARD} root handle 1", shell=True)
subprocess.run(f"tc qdisc add dev {NETCARD} root handle 1: htb", shell=True)
subprocess.run(
    f"tc class add dev {NETCARD} parent 1: classid 1:1 htb rate 10000mbit", shell=True
)
mark = 10
print("Done")
# Create a class for each IP source with the random delay
for record in data:
    if record["isCovert"] == True:
        src_ip, dst_ip, max_delay = record["src"], record["dst"], record["max_delay"]
        print(src_ip)
        mark = mark + 1
        subprocess.run(
            f"tc class add dev {NETCARD} parent 1:1 classid 1:{mark} htb rate 100mbit",
            shell=True,
        )

        subprocess.run(
            f"tc filter add dev {NETCARD} parent 1: protocol ip u32 match ip src {src_ip} match ip dst {dst_ip} flowid 1:{mark}",
            shell=True,
        )
        subprocess.run(
            f"tc qdisc add dev {NETCARD} parent 1:{mark} handle {mark}: netem delay {max_delay//2}ms {max_delay//2}ms",
            shell=True,
        )

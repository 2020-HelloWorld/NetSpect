import subprocess
try:
    print("Clean up")
    NETCARD = "enp0s3"

    # Delete the existing tc qdisc and add a new HTB qdisc
    subprocess.run(f"tc qdisc del dev {NETCARD} root handle 1", shell=True)
except Exception as e:
    print(e)

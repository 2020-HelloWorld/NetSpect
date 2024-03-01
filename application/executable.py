import os
l = [
    "ttl_prevent/ttl_maximize.sh",
    "dependencies.sh",
    "initialize.sh",
    "cleanup.sh",
    "delay_detect/layer2_detect.sh",
    "delay_detect/layer2_analysis.sh",
    "delay_queue/add_delay.sh",
    "tcp_override/cleanup.sh",
    "tcp_override/remove.sh",
    "tcp_override/tcp_override.sh",
    "ttl_detect/layer1_analysis.sh",
    "ttl_detect/layer1_detect.sh",
    "ttl_prevent/cleanup.sh",
    "ttl_prevent/inject_kernel_object.sh"
]

for i in l:
    os.system(f"chmod u+x {i}")
    os.system(f"dos2unix {i}")

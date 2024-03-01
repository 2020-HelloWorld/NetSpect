from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
import subprocess, threading
import os, json, time


# Create your views here.
@login_required(login_url="/login/")
def dashboard_api(request):
    return render(request, "dashboard_file.html")


def startFlowAnalysis(request):
    if request.method == "POST":
        value = request.POST.get("value")

        # Clear all the previous data
        subprocess.call(["sh", "./cleanup.sh"])
        subprocess.call(["sh", "./ttl_prevent/cleanup.sh"])
        subprocess.call(["sh", "./tcp_override/cleanup.sh"])
        # os.system("python3 ./cleanup.py")

        # Start new analysis
        print("Start Detection:", value)

        def run_command(command):
            try:
                subprocess.run(command, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Threads stopped: {command}: {e}")

        def capture_data():
            command1 = [
                "timeout",
                str(300),
                "bash",
                "./delay_detect/layer2_detect.sh",
            ]
            command2 = [
                "timeout",
                str(300),
                "bash",
                "./ttl_detect/layer1_detect.sh",
            ]

            # Create threads for each command
            thread1 = threading.Thread(target=run_command, args=(command1,))
            thread2 = threading.Thread(target=run_command, args=(command2,))

            # Start the threads
            thread1.start()
            thread2.start()

            # Wait for both threads to finish
            thread1.join()
            thread2.join()

        def analyse_capture():
            print("analysing capture")
            subprocess.run(["bash", "./delay_detect/layer2_analysis.sh"], check=True)
            subprocess.run(["bash", "./ttl_detect/layer1_analysis.sh"], check=True)

        if value == "true":
            data = []

            try:
                capture_data()
                # time.sleep(300)
                analyse_capture()

            except Exception as e:
                print("Unexpected Exception:", e)

            with open("./temp_json/flow_result.json", "r") as json_file:
                json_data = json.load(json_file)
                for flow in json_data:
                    if flow["isCovert"]:
                        data.append(
                            {
                                "src": flow["src"],
                                "dst": flow["dst"],
                                "status": "Covert" if flow["isCovert"] else "Overt",
                                "type": "IAT",
                            }
                        )
            # Load JSON data from file
            with open("./temp_json/currently_covert.json", "r") as json_file:
                json_data = json.load(json_file)
                # Construct the command based on JSON data
                for key, value in json_data.items():
                    source_ip, dest_ip = key.split(" - ")
                    data.append(
                        {
                            "src": source_ip,
                            "dst": dest_ip,
                            "status": "Covert",
                            "type": "TTL",
                        }
                    )
            print(data)
            return JsonResponse({"data": data}, status=201)
        else:
            return HttpResponse("False received", status=201)

    else:
        return HttpResponse("Only POST requests allowed", status=302)


def insertTcpOverridingModule(request):
    if request.method == "POST":
        value = request.POST.get("value")
        print("TCP Overriding:", value)
        if value == "true":
            subprocess.run(["bash", "./tcp_override/tcp_override.sh"], check=True)
            return HttpResponse("Success", status=201)
        else:
            subprocess.run(["bash", "./tcp_override/remove.sh"], check=True)
            return HttpResponse("Success", status=201)
    else:
        return HttpResponse("Only POST requests allowed", status=302)


def insertDelyaQueue(request):
    if request.method == "POST":
        value = request.POST.get("value")
        print("Delay Overriding:", value)
        if value == "true":
            subprocess.run(["bash", "./delay_queue/add_delay.sh"], check=True)
            return HttpResponse("Success", status=201)
        else:
            return HttpResponse("No switch off functionality", status=201)
    else:
        return HttpResponse("Only POST requests allowed", status=302)


def applyTtlMaximization(request):
    if request.method == "POST":
        value = request.POST.get("value")
        print("TTL Overriding:", value)
        if value == "true":
            subprocess.run(["bash", "./ttl_prevent/ttl_maximize.sh"], check=True)
            subprocess.run(
                ["bash", "./ttl_prevent/inject_kernel_object.sh"], check=True
            )
            return HttpResponse("Success", status=201)
        else:
            return HttpResponse("No switch off functionality", status=201)
    else:
        return HttpResponse("Only POST requests allowed", status=302)

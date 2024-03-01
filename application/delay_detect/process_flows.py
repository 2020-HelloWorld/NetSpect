import json
import numpy as np
from scipy.stats import gaussian_kde, mode
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
import math

# Read packet data from the JSON file created during packet sniffing
with open("./temp_json/packet_data.json", "r") as json_file:
    packet_data = [json.loads(line) for line in json_file]

# Create a dictionary to store flow information and IAT values
flow_iat = {}


def tab(x):
    if x <= 3:
        return 7
    if x in range(4, 16):
        return 3
    if x >= 16:
        return 1
    raise ValueError


# Extract packet data and calculate IAT values for each flow
for packet in packet_data:
    src_ip = packet["source_ip"]
    dst_ip = packet["destination_ip"]
    timestamp_sec = packet["timestamp_sec"]
    timestamp_us = packet["timestamp_us"]

    flow_id = src_ip, "-", dst_ip

    if flow_id not in flow_iat:
        flow_iat[flow_id] = {"timestamps": []}

    total_timestamp = timestamp_sec + (timestamp_us // 1000) / 1000
    flow_iat[flow_id]["timestamps"].append(total_timestamp)

# Calculate the fields for each flow
results = []
for flow_id, data in flow_iat.items():
    try:
        timestamps = data["timestamps"]
        if len(timestamps) <= 2:
            continue
        iat_values = np.round(np.diff(timestamps), 3)
        print("IAT", iat_values)
        print("TS", timestamps)
        print("*****")

        unique_iat = len(np.unique(iat_values))  # done

        density = gaussian_kde(iat_values)

        # Evaluate KDE at a range of x values
        x_values = np.linspace(min(iat_values), max(iat_values), 1000)
        kde_estimate = density.evaluate(x_values)

        # Find local maxima indices
        local_maxima_indices = argrelextrema(kde_estimate, np.greater, mode="wrap")

        max_delay = max(x_values[local_maxima_indices[0]])

        kde_peaks = len(local_maxima_indices[0])  # done

        peak_widths = []
        for idx in local_maxima_indices[0]:
            kernel_std = density.covariance_factor() * np.std(iat_values)
            peak_widths.append(2 * np.sqrt(2 * np.log(2)) * kernel_std)

        # Calculate the average width
        average_width = np.mean(peak_widths) if len(peak_widths) > 0 else 0

        # Plot the original data and KDE
        plt.figure(figsize=(10, 6))

        for idx, width in zip(local_maxima_indices[0], peak_widths):
            plt.axvline(
                x=x_values[idx],
                color="green",
                linestyle="--",
                label="Peak Width" if idx == local_maxima_indices[0][0] else None,
            )
            plt.axvline(x=x_values[idx] - width / 2, color="green", linestyle=":")
            plt.axvline(x=x_values[idx] + width / 2, color="green", linestyle=":")

        # Plot the histogram of the original data
        plt.hist(
            iat_values, bins=unique_iat, density=True, alpha=0.5, label="Data Histogram"
        )

        # Plot the KDE estimate
        plt.plot(x_values, kde_estimate, label="KDE")

        # Highlight the identified peaks using local maxima
        plt.scatter(
            x_values[local_maxima_indices],
            kde_estimate[local_maxima_indices],
            color="red",
            label="Local Maxima",
        )

        # Display the average width on the plot
        plt.text(
            0.5, 0.8, "Average Width:" + str(average_width), transform=plt.gca().transAxes
        )

        plt.xlabel("Values")
        plt.ylabel("Density")
        plt.title("Data and KDE with Local Maxima as Peaks")
        plt.legend()

        s = "./images/output/" + str(flow_id) + ".png"

        plt.savefig(s)

        symbols = len(set(iat_values))  # Not considered
        peak_std_mean = average_width  # done
        autocorr_sum = np.sum(np.correlate(iat_values, iat_values, mode="full"))

        # Calculate the mode of IAT values using scipy.stats.mode()
        mode_result = mode(iat_values)
        mode_iat = mode_result[0]
        # print(mode_iat,mode_result.mode)

        p_mode = np.count_nonzero(iat_values == mode_iat) / len(iat_values)

        num_packets = len(timestamps)
        # COvert bytes
        covert_bytes = num_packets / tab(math.floor(kde_peaks))

        result = {
            "flow_id": flow_id,  # Done
            "unique": unique_iat,  # Done
            "multimod": kde_peaks,  # Done
            "multimod2": symbols,  # Not considered
            "widthave": peak_std_mean,  # Done
            "autocorr": autocorr_sum,
            "c": covert_bytes,
            "nrPacketsMode": p_mode,  # Done
            "nrPackets": num_packets,  # Done
            "maxDelay_ms": max_delay * 1000,
        }
        results.append(result)
    except Exception as e:
        print("Error processing flow:",e)


# Store the results in a JSON file
output_filename = "./temp_json/flow_analysis.json"
with open(output_filename, "w") as json_file:
    json.dump(results, json_file, indent=4)

print("Results stored in 'flow_analysis.json'")

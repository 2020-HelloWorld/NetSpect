# NetSpect
## Team Pesumists
Repository for AI based threat protection against covert channels

## Problem 
In the era of next-generation firewalls, being efficient in firewall configuration is the need of the hour for an organisation. Even if the firewalls are correctly configured, there is a high probability that illegal data might go undetected inside the network.
Risk of data theft and illegal communications by making use of hidden channels which can potentially cause problems to various sectors including but not limited to Defence, Science and Research, Business organizations, Top secret government facilities etc.
Thus, we aim to develop a 'Covert Channel Detection and Prevention' tool that will try to detect and disrupt covert timing channels in computer networks. The tool will be designed to work with a variety of network protocols and hardware configurations.

## Solution
The focus is on creating an automated and efficient system that can identify and stop these unauthorized information channels before they cause any harm or data breaches. Future work focus 
should be on improving usability where constant analysis of the traffic is done to implement prevention mechanisms according to pre configured settings, Accuracy where focus is on reducing 
false positives and improving accuracy of the system by developing a machine learning model on bigger and versatile dataset and Robustness where we have to improve the system to handle issuesrelated to limited allocated resources in the Kernel space to accommodate large number of flows.
- The idea is to detect the covert timing channels which goes undetected by existing security protection devices 
- This project aims at detecting and preventing covert timing channels using a two-layered approach. 
- The first layer targets covert communication prevention by addressing the communication based on modification of timing-related values in packet headers, specifically TTL values and TCP Timestamps. 
- Layer two aims at the detection and prevention of IAT-based covert communication using Machine Learning, Decision Tree model to obtain classification rules for detection purposes.

[Presentation](https://www.canva.com/design/DAF9hsGU8G4/RL1L1kRqMNvUjyGEbipFlw/edit?utm_content=DAF9hsGU8G4&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

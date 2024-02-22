#include <stdlib.h>
#include <stdio.h>
#include <pcap.h>
#include <arpa/inet.h>
#include <sys/time.h> // Include the sys/time.h header for gettimeofday
#include <inttypes.h>
#include <json-c/json_object.h>

struct timeval start_time; // Store the start time
/* Ethernet header */
struct ethheader
{
    u_char ether_dhost[6]; /* destination host address */
    u_char ether_shost[6]; /* source host address */
    u_short ether_type;    /* protocol type (IP, ARP, RARP, etc) */
};

/* IP Header */
struct ipheader
{
    unsigned char iph_ihl : 4,       // IP header length
        iph_ver : 4;                 // IP version
    unsigned char iph_tos;           // Type of service
    unsigned short int iph_len;      // IP Packet length (data + header)
    unsigned short int iph_ident;    // Identification
    unsigned short int iph_flag : 3, // Fragmentation flags
        iph_offset : 13;             // Flags offset
    unsigned char iph_ttl;           // Time to Live
    unsigned char iph_protocol;      // Protocol type
    unsigned short int iph_chksum;   // IP datagram checksum
    struct in_addr iph_sourceip;     // Source IP address
    struct in_addr iph_destip;       // Destination IP address
};

void got_packet(u_char *args, const struct pcap_pkthdr *header, const u_char *packet)
{
    struct ethheader *eth = (struct ethheader *)packet;

    if (ntohs(eth->ether_type) == 0x0800)
    { // 0x0800 is IP type
        struct ipheader *ip = (struct ipheader *)(packet + sizeof(struct ethheader));

        int64_t timestamp_sec = header->ts.tv_sec; // Extracting seconds
        int64_t timestamp_us = header->ts.tv_usec; // Extracting micro seconds

        // Create a JSON object
        struct json_object *json_obj = json_object_new_object();

        // Add packet information to the JSON object
        json_object_object_add(json_obj, "timestamp_sec", json_object_new_int64(timestamp_sec));
        json_object_object_add(json_obj, "timestamp_us", json_object_new_int64(timestamp_us));

        json_object_object_add(json_obj, "source_ip", json_object_new_string(inet_ntoa(ip->iph_sourceip)));
        json_object_object_add(json_obj, "destination_ip", json_object_new_string(inet_ntoa(ip->iph_destip)));

        const char *protocol;
        switch (ip->iph_protocol)
        {
        case IPPROTO_TCP:
            protocol = "TCP";
            break;
        case IPPROTO_UDP:
            protocol = "UDP";
            break;
        case IPPROTO_ICMP:
            protocol = "ICMP";
            break;
        default:
            protocol = "others";
            break;
        }
        json_object_object_add(json_obj, "protocol", json_object_new_string(protocol));

        // Print or store the JSON object as needed
        printf("%s\n", json_object_to_json_string(json_obj));

        FILE *json_file = fopen("./temp_json/packet_data.json", "a"); // Open the file in append mode
        if (json_file)
        {
            fprintf(json_file, "%s\n", json_object_to_json_string(json_obj));
            fclose(json_file);
            // Clean up allocated memory
            json_object_put(json_obj);
        }
    }
}

int main()
{
    pcap_t *handle;
    char errbuf[PCAP_ERRBUF_SIZE];

    // Step 1: Open live pcap session on NIC with name br-****
    handle = pcap_open_live("enp0s3", BUFSIZ, 1, 1000, errbuf);

    // Step 3: Capture packets
    pcap_loop(handle, -1, got_packet, NULL);

    pcap_close(handle); // Close the handle
    return 0;
}

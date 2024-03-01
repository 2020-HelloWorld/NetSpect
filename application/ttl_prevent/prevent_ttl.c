#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>
#include <linux/sysfs.h>
#include <linux/fs.h>
#include <linux/slab.h>
#include <linux/ip.h>
#include <linux/in.h>
// #include <linux/tcp.h>
// #include <linux/udp.h>
// #include <linux/icmp.h>
#include <linux/if_ether.h>
#include <linux/inet.h>
#include <linux/string.h>

// Define the maximum number of allowed IP addresses
#define MAX_ALLOWED_IPS 100

// Declare a Netfilter hook to handle packet filtering
static struct nf_hook_ops pre_routing_hook;

// Declare a kernel object for sysfs interaction
static struct kobject *my_module_kobj;

// Name of the sysfs attribute file
// static const char *sysfs_file = "allowed_ips";

// Array to store the list of allowed IP addresses
static struct
{
    u32 src_ip;
    u32 dst_ip;
    unsigned long max_ttl;
} allowed_ip_list[MAX_ALLOWED_IPS];

// Number of allowed IP addresses in the list
static int num_allowed_ips = 0;

// Pre-routing hook function to filter incoming packets
static unsigned int pre_routing_hook_function(void *priv, struct sk_buff *skb, const struct nf_hook_state *state)
{
    struct iphdr *iph;
    u32 src_ip, dst_ip;
    unsigned int ihl;

    iph = ip_hdr(skb);

    // Get source and destination IP addresses from the packet
    src_ip = iph->saddr;
    dst_ip = iph->daddr;

    for (int i = 0; i < num_allowed_ips; i++)
    {
        // printk(KERN_INFO "Packet Allowed,%d\n",src_ip);
        // Check if the source and destination IP addresses match any entry in the allowed list
        if (src_ip == allowed_ip_list[i].src_ip && dst_ip == allowed_ip_list[i].dst_ip)
        {
            // Wait for the specified time
            if (iph->ttl > allowed_ip_list[i].max_ttl)
            {
                allowed_ip_list[i].max_ttl = iph->ttl;
            }
            else
            {
                iph->ttl = allowed_ip_list[i].max_ttl;
            }

            ihl = iph->ihl; // IHL (Internet Header Length) in 32-bit words

            // Calculate the checksum for the IP header
            iph->check = 0; // Clear the checksum field
            iph->check = ip_fast_csum((unsigned char *)iph, ihl);

            printk(KERN_INFO "Packet Allowed with src as %pI4 dst as %pI4\n ***********", &(iph->saddr), &(iph->daddr));
            return NF_ACCEPT;
        }
    }

    return NF_ACCEPT;
}

// Sysfs attribute store function to add IP addresses to the allowed list
static ssize_t allowed_ips_store(struct kobject *kobj, struct kobj_attribute *attr, const char *buf, size_t count)
{
    u32 src_ip, dst_ip;
    char src_ip1[16]; // Assuming IPv4 addresses, so 15 characters for each
    char dest_ip2[16];
    unsigned long wait_time;

    if (num_allowed_ips >= MAX_ALLOWED_IPS)
    {
        return -ENOMEM;
    }
    printk(KERN_INFO "Received input: %.*s", (int)count, buf);

    // Parse the source and destination IP addresses from the input buffer

    if (sscanf(buf, "%15s %15s %lu", src_ip1, dest_ip2, &wait_time) == 3)
    {
        printk(KERN_INFO "IP1: %s\n", src_ip1);
        printk(KERN_INFO "IP2: %s\n", dest_ip2);

        in4_pton(src_ip1, -1, (u8 *)&src_ip, '\0', NULL);
        in4_pton(dest_ip2, -1, (u8 *)&dst_ip, '\0', NULL);

        allowed_ip_list[num_allowed_ips].src_ip = src_ip;
        allowed_ip_list[num_allowed_ips].dst_ip = dst_ip;
        allowed_ip_list[num_allowed_ips].max_ttl = wait_time;
        num_allowed_ips++;
        return count;
    }
    else
    {
        return -EINVAL; // Input format is invalid
    }
}

// static ssize_t myvariable_show(struct kobject *kobj, struct kobj_attribute *attr, char *buf)
//  {
//  return sprintf(buf, "%d\n", myvariable);

//  }

// Define a sysfs attribute for the allowed IP addresses
static struct kobj_attribute allowed_ips_attribute = __ATTR(allowed_ips, 0660, NULL, allowed_ips_store);

// Module initialization function
static int __init mymodule_init(void)
{
    // Create a sysfs directory for the module
    my_module_kobj = kobject_create_and_add("my_module", kernel_kobj);
    if (!my_module_kobj)
        return -ENOMEM;

    // Create the sysfs attribute for allowed IP addresses
    if (sysfs_create_file(my_module_kobj, &allowed_ips_attribute.attr))
    {
        kobject_put(my_module_kobj);
        return -ENOMEM;
    }

    // Register the pre-routing hook
    pre_routing_hook.hook = pre_routing_hook_function;
    pre_routing_hook.pf = NFPROTO_IPV4;
    pre_routing_hook.hooknum = NF_INET_POST_ROUTING;
    pre_routing_hook.priority = NF_IP_PRI_FIRST;
    nf_register_net_hook(&init_net, &pre_routing_hook);

    return 0;
}

// Module exit function
static void __exit mymodule_exit(void)
{
    // Unregister the pre-routing hook
    nf_unregister_net_hook(&init_net, &pre_routing_hook);

    // Remove the sysfs attribute and directory
    sysfs_remove_file(my_module_kobj, &allowed_ips_attribute.attr);
    kobject_put(my_module_kobj);
}

// Module initialization and exit points
module_init(mymodule_init);
module_exit(mymodule_exit);

// Module information
MODULE_LICENSE("GPL");
MODULE_AUTHOR("Your Name");
MODULE_DESCRIPTION("Kernel module for dynamic packet filtering based on allowed source and destination IP addresses");
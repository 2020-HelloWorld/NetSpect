#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>
#include <linux/ip.h>
#include <linux/tcp.h>
// #include <linux/skbuff.h>
// #include <linux/byteorder/generic.h>

static struct nf_hook_ops hook1;

unsigned int printTCPTimestamps(void *priv, struct sk_buff *skb, const struct nf_hook_state *state)
{
    if (!skb)
        return NF_ACCEPT;

    struct iphdr *iph = ip_hdr(skb);

    if (iph->protocol == IPPROTO_TCP)
    {
        struct tcphdr *tcph = tcp_hdr(skb);

        // Check if the SYN flag is set.
        // if (!tcph->syn) {
        //     return NF_ACCEPT;
        // }

        // Check for TCP options.
        int tcphdrlen = tcph->doff * 4;
        // int tcp_hdr_len_copy=tcphdrlen ;
        if (tcphdrlen > sizeof(struct tcphdr))
        {
            unsigned char *tcp_options = (unsigned char *)(tcph) + sizeof(struct tcphdr);

            // Loop through the TCP options to find the TCP timestamp option.
            int optlen, kind;
            while (tcphdrlen > sizeof(struct tcphdr))
            {
                kind = tcp_options[0];

                if (kind == 8)
                {
                    if (tcphdrlen >= 10)
                    {
                        __be32 *tsval_ptr = (__be32 *)(tcp_options + 2);
                        __be32 *tsecr_ptr = (__be32 *)(tcp_options + 6);

                        __u32 tsval = ntohl(*tsval_ptr);
                        __u32 tsecr = ntohl(*tsecr_ptr);

                        printk(KERN_INFO "*** TCP timestamps: %u %u ", tsval, tsecr);

                        if (tsval != 0)
                        {
                            tsval = tsval | 1;
                            *tsval_ptr = htonl(tsval);
                        }

                        if (tsecr != 0)
                        {
                            tsecr = tsecr | 1;
                            *tsecr_ptr = htonl(tsecr);
                        }

                        // printk(KERN_INFO "***OLD csum: %x\n", tcph->check);
                        // tcph->check = 0;  // Clear the checksum field for re-calculation

                        // unsigned int tcplen;
                        // tcplen = skb->len - iph->ihl - 14;
                        // // tcph->check = 0;
                        // tcph->check = tcp_v4_check(tcplen, iph->saddr, iph->daddr, csum_partial((char *)tcph, tcplen, 0));
                        // // tcph->check =csum_tcpudp_magic(iph->saddr, iph->daddr, tcp_hdr_len_copy, IPPROTO_TCP, 0);
                        printk(KERN_INFO "***New csum: %x\n", tcph->check);
                        // skb->ip_summed = CHECKSUM_UNNECESSARY;

                        printk(KERN_INFO "*** Updated TCP timestamps: %u %u\n", tsval, tsecr);
                        break;
                    }
                }

                optlen = tcp_options[1];
                if (optlen < 2)
                {
                    break;
                }

                tcp_options += optlen;
                tcphdrlen -= optlen;
            }
        }
        else
        {
            printk(KERN_INFO "*** No TCP options found.\n");
        }
    }

    return NF_ACCEPT;
}

int registerFilter(void)
{
    printk(KERN_INFO "Registering filters.\n");

    hook1.hook = printTCPTimestamps;
    hook1.hooknum = NF_INET_POST_ROUTING;
    hook1.pf = PF_INET;
    hook1.priority = NF_IP_PRI_FIRST;
    nf_register_net_hook(&init_net, &hook1);

    return 0;
}

void removeFilter(void)
{
    printk(KERN_INFO "The filters are being removed.\n");
    nf_unregister_net_hook(&init_net, &hook1);
}

module_init(registerFilter);
module_exit(removeFilter);

MODULE_LICENSE("GPL");

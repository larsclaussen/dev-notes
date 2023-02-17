# DNS

Resolve domain names, IPv4 and IPv6 addresses, DNS records, and services.

```shell
systemd-resolve --status
```


Show open ports and their processes

```shell
netstat -tulpen
```


## Ubuntu/Debian resolv.conf

Add permanent DNS nameservers by extending resolv.conf.

The resolv.conf file will be overwritten on each boot so you cannnot edit it directly.
Instead, edit one of the two files that is used to create the resolv.conf file, the head or base file.
If you want your additional entries to be written to the top of the `resolv.conf ` file, edit the head file.


```shell
sudo vim /etc/resolvconf/resolv.conf.d/head
```

## wlan

Get the name of the wlan you're connected to.

```shell
iwgetid -r
```

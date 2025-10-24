### Static IP Configuration

Configured a static IP using **Netplan** to ensure consistent network identity.

**Network Details:**
- **Interface:** `enp0s3`
- **Static IP:** `192.168.1.114/24`
- **Gateway:** `192.168.1.1`
- **DNS:** `192.168.1.1` (via router)

---

```yaml
# Netplan configuration for static IP
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      dhcp4: no
      addresses:
        - 192.168.1.114/24
      gateway4: 192.168.1.1
      nameservers:
        addresses: [192.168.1.1]
```
[Configuration File](../configs/netplan/00-installer-config.yaml)

## 1. Deploy Ubuntu Server 22.04 LTS

#### Installation Steps:
1. Download Ubuntu Server 22.04 LTS ISO from official website
2. Create bootable USB or mount ISO in VM
3. Boot from installation media
4. Follow installation wizard:
   - Select language and keyboard layout
   - Choose "Ubuntu Server" 
   - Set up initial user account
   - Install OpenSSH server when prompted
   - Complete installation and reboot
  

## 2. Configure Hostname

```bash
# Set hostname
sudo hostnamectl set-hostname prod-web-01

# Verify
hostname

# Update /etc/hosts
sudo nano /etc/hosts

127.0.0.1       localhost
127.0.1.1       prod-web-01
```

### Installation 

```bash
sudo apt install ufw
sudo ufw status 
```

### Enable IPv6

```bash
sudo nano /etc/default/ufw
IPv6=yes
```

### Configuration 

```bash
sudo ufw default allow outgoing
sudo ufw default deny incoming

sudo ufw allow 2222/tcp
sudo ufw allow http
sudo ufw allow https

sudo ufw enable
sudo ufw status
```

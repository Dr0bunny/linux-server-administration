### Installing Apache 

```bash
sudo apt update
sudo apt upgrade

sudo apt install apache2

# check if apache server running
sudo systemctl status apache2
```

---

### Create Simple Website

```bash
# create directory for our webite
sudo mkdir /var/www/company.net/html

sudo nano index.html
echo "I'm running this website on an Ubuntu Server !" > /var/www/company.net/html/index.html

# changes the ownership of 'company.net' directory
sudo chown -R www-data:www-data /var/www/company.net/html/
```

---

### Virtual Host Setup

```bash

```

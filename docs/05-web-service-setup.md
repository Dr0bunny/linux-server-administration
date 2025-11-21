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
echo "I'm running this website on an Ubuntu Server !" > /var/www/company.net/html/index.html

# changes the ownership of 'company.net' directory to low privileged user
sudo chown -R www-data:www-data /var/www/company.net/html/
```

---

### Virtual Host Setup

```bash
sudo nano /etc/apache2/sites-available/company.local.conf
```

[Read the intro](configs/apache2/company.net.conf)

### Install python

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
sudo apt install libapache2-mod-wsgi-py3
```

### Create app folder 

```bash
sudo mkdir -p /var/www/company.net/app
sudo chown developer:developer /var/www/company.net/app
```

### Create venv for python and Install flask 

```bash
python3 -m venv venv
source venv/bin/activate

pip3 install flask 
```

### Update company.net.conf file

```bash
<VirtualHost *:80>
    ServerName company.net
    ServerAlias company.net
    ServerAdmin webmaster@company.net
    
    # WSGI Configuration for Flask
    WSGIDaemonProcess flaskapp python-home=/var/www/company.net/app/venv python-path=/var/www/company.net/app
    WSGIProcessGroup flaskapp
    WSGIScriptAlias / /var/www/company.net/app/app.wsgi

    <Directory /var/www/company.net/app>
        Require all granted
    </Directory>

    ErrorLog /var/www/company.net/logs/error.log
    CustomLog /var/www/company.net/logs/access.log combined
</VirtualHost>
```
 

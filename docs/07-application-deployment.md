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
 

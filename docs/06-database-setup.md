### Installation 

```bash
sudo apt install mysql-server

## check mysql service are running and enabled
sudo systemctl status mysql  
```

### Configure security settings 

```bash
sudo mysql_secure_installation

VALIDATE PASSWORD COMPONENT # press y and choose the password policy you want
Remove anonymous users # press y
Disallow root login remotely # press y
Remove test database and access to it # press y
Reload privilege tables now # press y
```

make a stronge password for root user

```mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'put your password here';
```

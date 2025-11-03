### User Account Creation
 
```bash
# Create users with home directories
sudo useradd -m -s /bin/bash webadmin
sudo useradd -m -s /bin/bash dbadmin
sudo useradd -m -s /bin/bash developer
sudo useradd -m -s /bin/bash auditor

# Set initial passwords
sudo passwd webadmin
sudo passwd dbadmin
sudo passwd developer
sudo passwd auditor
```
---

### Sudo Access Configuration

```bash
# Web admin - can manage web services only
webadmin ALL=(ALL) /usr/bin/systemctl start apache2, /usr/bin/systemctl stop apache2, /usr/bin/systemctl restart apache2, /usr/bin/systemctl status apache2, /usr/bin/systemctl start nginx, /usr/bin/systemctl stop nginx, /usr/bin/systemctl restart nginx, /usr/bin/systemctl status nginx

# Database admin - can manage database services only
dbadmin ALL=(ALL) /usr/bin/systemctl start mysql, /usr/bin/systemctl stop mysql, /usr/bin/systemctl restart mysql, /usr/bin/systemctl status mysql, /usr/bin/systemctl start postgresql, /usr/bin/systemctl stop postgresql, /usr/bin/systemctl restart postgresql, /usr/bin/systemctl status postgresql

# Developer - read-only access to service status and logs
developer ALL=(ALL) /usr/bin/systemctl status *, /bin/journalctl
```

---

### Auditor Read-Only Access

```bash
sudo usermod -aG adm auditor
```

---

### Password Policy Implementation

```bash
# Installed Password Quality Library
sudo apt install libpam-pwquality -y
```

```bash
# Configured Password Complexity
nano /etc/security/pwquality.conf

minlen = 12          # Minimum 12 characters
dcredit = -1         # At least 1 digit
ucredit = -1         # At least 1 uppercase letter
lcredit = -1         # At least 1 lowercase letter
ocredit = -1         # At least 1 special character
minclass = 3         # Minimum 3 character classes
maxrepeat = 3        # Maximum 3 repeated characters
```

```bash
# Configured Password Aging
nano /etc/login.defs

PASS_MAX_DAYS   90   # Password expires after 90 days
PASS_MIN_DAYS   1    # Must wait 1 day before changing password
PASS_WARN_AGE   14   # Warn user 14 days before expiration
```

```bash
# Applied to Existing Users
sudo chage -M 90 -m 1 -W 14 webadmin
sudo chage -M 90 -m 1 -W 14 dbadmin
sudo chage -M 90 -m 1 -W 14 developer
sudo chage -M 90 -m 1 -W 14 auditor
```

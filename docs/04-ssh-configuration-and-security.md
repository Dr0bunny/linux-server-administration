### SSH Key-Based Authentication

```powershell
# Generated ED25519 Key Pair (Windows Client)
ssh-keygen -t ed25519 -C "ubuntu@gmail.com"
```

---

### Deployed Public Keys to All Users

```powershell
# Copied public key to each user account
type C:\Users\$env:USERNAME\.ssh\id_ed25519.pub | ssh webadmin@192.168.1.114 "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"

# Repeated for dbadmin, developer, and auditor
```

---

### SSH Configuration Hardening

```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup
```

```bash
nano /etc/ssh/sshd_config

# Change default port (reduces automated attacks)
Port 2222

# Disable root login
PermitRootLogin no

# Disable password authentication (keys only)
PasswordAuthentication no
PubkeyAuthentication yes

# Disable empty passwords
PermitEmptyPasswords no

# Limit authentication attempts
MaxAuthTries 3
```

---

### Validated and Applied Configuration:

```bash
# Test for syntax errors
sudo sshd -t

# Restart SSH service
sudo systemctl restart sshd

# Verify SSH is listening on new port
sudo ss -tulpn | grep :2222
```

---

### Fail2Ban Installation & Configuration

```bash
sudo apt install fail2ban -y
```

```bash
nano /etc/fail2ban/jail.local

[sshd]
enabled = true
port = 2222
filter = sshd
logpath = /var/log/auth.log
maxretry = 3        # Allow 3 failed attempts
bantime = 3600      # Ban for 1 hour
findtime = 600      # Within 10 minutes
```

```bash
# Enabled Service
sudo systemctl start fail2ban
sudo systemctl enable fail2ban

# Verify SSH jail is active
sudo fail2ban-client status sshd
```

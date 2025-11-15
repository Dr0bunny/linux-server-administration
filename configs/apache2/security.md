```bash
cd /etc/apache2/conf-available
sudo nano security.conf
```
```bash 
# minimize the exposure of server information
ServerTokens Prod 

# disables the display of server information like the server version number
ServerSignature Off

# it prevent cross-site tracing (XST) attacks
TraceEnable Off

# security headers 
Header always set X-Frame-Options "SAMEORIGIN"
Header always set X-Content-Type-Options "nosniff"
Header always set X-XSS-Protection "1; mode=block"
Header always set Content-Security-Policy "frame-ancestors 'self';"
```

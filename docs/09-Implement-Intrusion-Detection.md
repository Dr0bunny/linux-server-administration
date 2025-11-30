### Installing and Configuring AIDE

```bash
sudo apt install aide -y
sudo aide --config /etc/aide/aide.conf --init
sudo cp /var/lib/aide/aide.db.new /var/lib/aide/aide.db
```

### Testing if it work 

```bash
echo '#test' | sudo tee -a /etc/hosts
sudo aide --config /etc/aide/aide.conf --check
```

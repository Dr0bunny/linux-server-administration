# Linux Server Administration

A comprehensive hands-on project documenting the deployment, configuration, and hardening of a production-ready Ubuntu Server. This project demonstrates essential system administration skills with a strong focus on security best practices.

## Project Overview

This repository documents my journey in learning Linux server administration through practical implementation. Each task is completed with security in mind, following industry best practices and the principle of least privilege.

**Target Audience:** System administrators, DevOps engineers, security professionals, and anyone learning Linux server management.

## Technology Stack

- **Operating System:** Ubuntu Server 22.04 LTS
- **Virtualization:** Oracle VirtualBox
- **Network Configuration:** Netplan
- **Security Tools:** Fail2Ban, UFW 
- **Authentication:** OpenSSH with ED25519 key-based authentication

##  Project Status

### Phase 1: Initial Setup & User Management
- Server Deployment
- Network Configuration
- User Access Control
- SSH Hardening

### Phase 2: Service Management 
- Web Server Setup (Apache/Nginx)
- Database Server (MySQL/PostgreSQL)
- Application Deployment
- Firewall Configuration
- Service Hardening

### Phase 3: Monitoring & Maintenance (Upcoming)
- Log Management
- System Monitoring
- Backup & Recovery
- Automation Scripts

##  Implemented Security Features

### SSH Hardening
-  Custom port configuration (changed from default port 22 to 2222)
-  Key-based authentication only (password authentication disabled)
-  Root login disabled
-  Fail2Ban configured for brute-force protection
-  Maximum authentication attempts limited to 3

### User Access Management
-  Role-based user accounts (webadmin, dbadmin, developer, auditor)
-  Principle of least privilege applied
-  Sudo access configured per role
-  Read-only auditor account for security monitoring

### Password Security
-  Minimum 12 characters required
-  Complexity requirements enforced (uppercase, lowercase, digits, special characters)
-  90-day password expiration policy
-  Password quality checking with PAM

### Network Security
-  Static IP configuration for consistent access
-  UFW firewall enabled and configured
-  Only necessary ports exposed


##  Learning Outcomes

Through this project, I have gained practical experience in:

- **Linux System Administration**
  - Server deployment and configuration
  - User and permission management
  - Service management with systemd
  
- **Network Configuration**
  - Static IP configuration with Netplan
  - Firewall rules and network security
  - SSH remote administration

- **Security Hardening**
  - SSH security best practices
  - Password policy enforcement
  - Intrusion prevention with Fail2Ban
  - Security audit and verification

- **Documentation Skills**
  - Technical writing
  - Creating reproducible configurations
  - Knowledge sharing


**User Accounts:**
| Username | Role | Sudo Access | Purpose |
|----------|------|-------------|---------|
| webadmin | Web Administrator | Web services only | Manage Apache/Nginx |
| dbadmin | Database Administrator | Database services only | Manage MySQL/PostgreSQL |
| developer | Developer | Read-only system access | Development and testing |
| auditor | Security Auditor | No sudo (read-only via groups) | Security monitoring and audits |





**Disclaimer:** This repository is for educational purposes. Always follow your organization's security policies and compliance requirements in production environments.

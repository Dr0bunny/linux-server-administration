#!/usr/bin/python3
import sys
import logging

logging.basicConfig(stream=sys.stderr)

# Add your app directory to Python path
sys.path.insert(0, "/var/www/company.net/app")

from app import app as application

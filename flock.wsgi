#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/flock/")

from flock import app as application
application.secret_key = 'x\xc3QYm\x03\xabv\xfa\x88:\xf9"\xba\xbf\x7f|\xe9{\xc6$\xf3\\a'

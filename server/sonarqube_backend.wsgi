#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from python import app as application

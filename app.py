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

script = 'curl ipinfo.io'
run = os.popen(script).readlines()
run

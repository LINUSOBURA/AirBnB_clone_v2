#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack"""

import os
from datetime import datetime

from fabric.api import *


def do_pack():
    versions_folder = "versions"
    try:
        os.makedirs(versions_folder)
    except:
        pass
    now = datetime.now()
    date = now.strftime("%Y%m%d%H%M%S")
    local(f"tar -cvzf versions/web_static_{date}.tgz web_static")

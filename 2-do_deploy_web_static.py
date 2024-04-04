#!/usr/bin/python3
"""
abric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function do_deploy
"""

import os
from datetime import datetime

from fabric.api import *

env.hosts = ['3.85.177.85', '18.206.192.69']


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    local("sudo mkdir -p versions")
    now = datetime.now()
    date = now.strftime("%Y%m%d%H%M%S")
    local(f"tar -cvzf versions/webstatic_{date}.tgz web_static")


def do_deploy(archive_path):
    """ Deploying the archive to web servers """
    """ Returns False if the file at the path archive_path doesn’t exist """
    if not archive_path or not os.path.exists(archive_path):
        return False

    arch_name = archive_path.split('/')[-1]
    arch_name_ntgz = arch_name.split('.')[0]

    try:
        """ Upload the archive to the /tmp/ directory of the web server """
        put(archive_path, f"/tmp/{arch_name}")

        run(f"mkdir -p /data/web_static/releases/{arch_name_ntgz}/")
        """ Uncompress the archive """
        run(f"tar -xzvf /tmp/{arch_name} -C\
            /data/web_static/releases/{arch_name_ntgz}/")
        """ Delete the archive from the web server """
        run(f"rm /tmp/{arch_name}")

        run(f"mv /data/web_static/releases/{arch_name_ntgz}/web_static/*\
            /data/web_static/releases/{arch_name_ntgz}")

        run(f"rm -rf /data/web_static/releases/{arch_name_ntgz}/web_static")
        """ Delete the symbolic link /data/web_static/current """
        run("rm -rf /data/web_static/current")
        """ Create a new the symbolic link /data/web_static/current """
        run(f"ln -s /data/web_static/releases/{arch_name_ntgz}/\
            /data/web_static/current")
    except Exception as e:
        return False

    return True

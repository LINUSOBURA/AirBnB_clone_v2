#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack"""

import os
from datetime import datetime

from fabric.api import *

env.hosts = ['3.85.177.85', '18.206.192.69']


def do_pack():
    versions_folder = "versions"
    try:
        os.makedirs(versions_folder)
    except:
        pass
    now = datetime.now()
    date = now.strftime("%Y%m%d%H%M%S")
    local(f"tar -cvzf versions/webstatic_{date}.tgz web_static")


def do_deploy(archive_path):
    if not archive_path or not os.path.exists(archive_path):
        return False

    arch_name = archive_path.split('/')[-1]
    arch_name_ntgz = arch_name.split('.')[0]

    try:
        put(archive_path, f"/tmp/{arch_name}")

        run(f"mkdir -p /data/web_static/releases/{arch_name_ntgz}/")

        run(f"tar -xzvf /tmp/{arch_name} -C /data/web_static/releases/{arch_name_ntgz}/"
            )

        run(f"rm /tmp/{arch_name}")

        run(f"mv /data/web_static/releases/{arch_name_ntgz}/web_static/* /data/web_static/releases/{arch_name_ntgz}"
            )

        run(f"rm -rf /data/web_static/releases/{arch_name_ntgz}/web_static")

        run("rm -rf /data/web_static/current")

        run(f"ln -s /data/web_static/releases/{arch_name_ntgz}/ /data/web_static/current"
            )
    except:
        return False

    return True

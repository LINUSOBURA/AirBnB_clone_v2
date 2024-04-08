#!/usr/bin/python3
"""
abric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function do_deploy
"""

import os
from datetime import datetime

from fabric.api import *

env.hosts = ["3.85.177.85", "18.206.192.69"]


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    local("sudo mkdir -p versions")
    now = datetime.now()
    date = now.strftime("%Y%m%d%H%M%S")
    local("tar -cvzf versions/web_static_{}.tgz web_static".format(date))


def do_deploy(archive_path):
    """ Deploying the archive to web servers

    Returns False if the file at the path archive_path doesn’t exist """
    if not os.path.exists(archive_path):
        return False

    arch_name = archive_path.split('/')[-1]
    arch_name_ntgz = '/data/web_static/releases/' + "{}".format(
        arch_name.split('.')[0])

    try:
        """ Upload the archive to the /tmp/ directory of the web server """
        put(archive_path, '/tmp/{}'.format(arch_name))

        run('mkdir -p {}/'.format(arch_name_ntgz))
        """ Uncompress the archive """
        run("tar -xzvf /tmp/{} -C {}/".format(arch_name, arch_name_ntgz))
        """ Delete the archive from the web server """
        run('rm /tmp/{}'.format(arch_name))

        run('mv {}/web_static/* {}/'.format(arch_name_ntgz, arch_name_ntgz))

        run('rm -rf {}/web_static'.format(arch_name_ntgz))
        """ Delete the symbolic link /data/web_static/current """
        run('rm -rf /data/web_static/current')
        """ Create a new the symbolic link /data/web_static/current """
        run('ln -s {}/ /data/web_static/current'.format(arch_name_ntgz))
        return True
    except Exception:
        return False

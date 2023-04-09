#!/usr/bin/python3
from fabric.api import run, put, env
import os

env.hosts = [
    '3.94.211.128',
    '52.91.123.252'
]
# env.user = 'ubuntu'
# env.key = '/home/trevor/.ssh/school'


def do_deploy(archive_path):
    """ A script that deploys static files to a web server"""
    if not os.path.exists(archive_path):
        return False
    try:
        filename = archive_path.rsplit('/', 1)[-1]
        base = filename.split('.')[0]

        put(archive_path, f'/tmp/{filename}')
        run("mkdir -p /data/web_static/releases/{}/".format(base))
        run("tar -zxvf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename, base))
        run("rm -rf /tmp/{}".format(filename))
        run("rsync -a /data/web_static/releases/{}/web_static/*\
             /data/web_static/releases/{}/".format(base, base))
        run("rm -rf /data/web_static/releases/{}/web_static".format(base))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(base))
        return True
    except Exception as e:
        return False

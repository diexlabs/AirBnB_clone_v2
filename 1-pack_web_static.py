#!/usr/bin/python3
from datetime import datetime
from fabric.api import local


def do_pack():
    '''packs a folder into an archive file'''
    d = datetime.now()
    filename = f'web_static_{d.strftime("%Y%m%d%H%M%S")}.tgz'

    try:
        local("mkdir -p versions")
        run = local(f"tar -cvzf versions/{filename} web_static/")

        return f'versions/{filename}'
    except Exception:
        return None

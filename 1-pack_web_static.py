#!/usr/bin/python3
from datetime import datetime
from fabric.api import local


def do_pack():
    '''packs a folder into an archive file'''
    d = datetime.now()
    filename = f'web_static_{d.strftime("%Y%m%d%H%M%S")}.tgz'

    try:
        local("mkdir -p versions")

        print(f'Packing web_static to versions/{filename}')
        run = local(f"tar -cvzf versions/{filename} web_static")

        if run.failed:
            return None
        return f'versions/{filename}'
    except Exception:
        return None

#!/usr/bin/python3
'''packs web_static folder into an archive'''

import os
import tarfile
from datetime import datetime
from fabric.context_managers import lcd
from fabric.operations import local

def do_pack():
    '''packs a folder into an archive file'''
    d = datetime.now()
    filename = f'web_static_{d.strftime("%Y%m%d%H%M%S")}.tgz'
    source = './web_static'

    if not os.path.exists('versions/'):
        os.mkdir('versions')

    if not os.path.exists('web_static'):
        return None

    print(f'Packing web_static to versions/{filename}')
    run = local(f"tar -cvzf versions/{filename} web_static")
    
    if run.failed:
        return None
    else:
        return filename

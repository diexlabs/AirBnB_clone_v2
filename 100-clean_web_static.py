#!/usr/bin/python3
"""Deletes all unnecessary archives"""
from fabric.api import run, local, lcd, cd, env
import os


env.hosts = ["3.94.211.128", "52.91.123.252"]
env.user = 'ubuntu'
env.key = "~/.ssh/school"


def do_clean(number=0):
    """prune the archive
    deleting out of date files
    """
    number = 1 if int(number) <= 0 else int(number)
    files = sorted(os.listdir("versions"))
    n = min(number, len(files))
    with lcd("."):
        for f in files[:len(files) - n]:
            local("rm -f versions/{}".format(f))

    with cd("/data/web_static/releases"):
        files = sorted(run("ls -At").split())
        n = min(number, len(files))
        for f in files[:len(files) - n]:
            if f.startswith("web_static"):
                run("rm -rf {}".format(f))

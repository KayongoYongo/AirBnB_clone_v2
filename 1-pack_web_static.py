#!/usr/bin/python3
"""A fabric script to create an archive file"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """A time stamp object to show the current time an object was created"""
    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    """We are creating a string.
    It represents the name of the compressed archive that we are creating."""
    file_path = "versions/web_static_{}.tgz".format(time_stamp)

    try:
        """create a directory called versions"""
        local("mkdir -p versions")

        """create an archive file"""
        local("tar -cvzf {} web_static/".format(file_path))

        """create a compressed archive of the "web_static" directory"""
        local("tar -czvf {} web_static".format(file_path))

        """Generate file path if generated correctly"""
        return file_path

    except Exception as e:
        """If the file generation was not successful"""
        return None

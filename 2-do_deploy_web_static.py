#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""


from fabric.api import run, env, put
from os.path import exists

env.hosts = ['34.234.193.62', '100.25.161.6']
env.key_filename = '~/.ssh/school'
env.user = 'ubuntu'


def do_deploy(archive_path):
    """A function to deploy code and decompress it"""

    """If file patch at archive path does not exist"""
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Get the file name without extension
        filename = archive_path.split("/")[-1]
        name = filename.split(".")[0]

        # Uncompress the archive to the folder on the web server
        run("sudo mkdir -p /data/web_static/releases/{}/".format(name))
        run("sudo tar -xzf /tmp/{} \
            -C /data/web_static/releases/{}/".format(filename, name))

        # Delete the archive from the web server
        run("sudo rm /tmp/{}".format(filename))

        # Move the content of the decompressed folder to its parent folder
        run("sudo mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(name, name))

        # Remove the now empty folder
        run("sudo rm -rf /data/web_static/releases/{}/web_static".format(name))

        # Delete the symbolic link /data/web_static/current from the web server
        run("sudo rm -rf /data/web_static/current")

        # Create a new the symbolic link on the web server
        run("sudo ln -s /data/web_static/releases/{}/ \
            /data/web_static/current".format(name))

        # Print new version deployed if successful and return true
        print("New version deployed!")
        return True

    except Exception as e:
        # Return false if the operation was ussucsseful
        return False

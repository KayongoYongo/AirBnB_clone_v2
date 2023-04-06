#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""


from datetime import datetime
from fabric.api import run, env, put, local
from os.path import exists

env.hosts = ['34.234.193.62', '100.25.161.6']
env.key_filename = '~/.ssh/school'
env.user = 'ubuntu'


def do_pack():
    """Archives the static files."""
    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")

    file_path = "versions/web_static_{}.tgz".format(time_stamp)

    try:
        # create a directory called versions
        local("mkdir -p versions")

        # create an archive file"""
        local("tar -cvzf {} web_static/".format(file_path))

        # create a compressed archive of the "web_static" directory"""
        local("tar -czvf {} web_static".format(file_path))

        # Generate file path if generated correctly"""
        return file_path

    except Exception as e:
        # If the file generation was not successful"""
        return None


def do_deploy(archive_path):
    # implementation of do_deploy function here
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


def deploy():
    """call do_pack and get the path of the created archive
    """
    archive_path = do_pack()

    # if archive creation was unsuccessful, return False
    return do_deploy(archive_path) if archive_path else False

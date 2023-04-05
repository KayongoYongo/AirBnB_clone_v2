#!/usr/bin/env bash
#Sets up a web server for deployment by ngin

#Install ngingx if not already installed
sudo apt-get update
sudo apt-get install -y nginx

#Create the directories even if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

#create a fake HTML file with simple content
echo "Holberton School" > /data/web_static/releases/test/index.html

#Create a symbolic link. If it exists, it should be deleted and recreated.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#Change the owner and the group of the data folder
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

#update nginx configuration
sudo printf "location /hbnb_static {
    alias /data/web_static/current/;
}\n" | sudo tee /etc/nginx/sites-available/default >/dev/null

#Restart nginx
sudo service nginx restart

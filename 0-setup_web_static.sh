#!/usr/bin/env bash
# Preparing web servers for deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx

#creating directories and files
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo "<h1>Testing Deployment</h1>" > /data/web_static/releases/test/index.html

#Creating symbolic link
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current

#Changing ownership
sudo chown -R ubuntu:ubuntu /data/

#inserting ne location into nginx configuration server block

sudo sed -i '15 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

service nginx restart

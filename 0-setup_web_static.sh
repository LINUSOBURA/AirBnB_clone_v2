#!/usr/bin/env bash
# Preparing web servers for deployment of web_static

apt-get update
apt-get -y install nginx

#creating directories and files
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<h1>Testing Deployment</h1>" > /data/web_static/releases/test/index.html

#Creating symbolic link
ln -sfn /data/web_static/releases/test/ /data/web_static/current

#Changing ownership
chown -R ubuntu:ubuntu /data/

#inserting ne location into nginx configuration server block

sed -i '15 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

service nginx restart
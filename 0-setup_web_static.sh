#!/usr/bin/env bash
# sets up a web server for deployment
#+ of static files

sudo apt-get update -y && sudo apt-get install nginx -y;

root=/data/web_static;

mkdir -p "$root/shared";
mkdir -p "$root/releases/test";
echo 'Hello World' > "$root/releases/test/index.html";

ln -sf -T "$root/releases/test/" "$root/current";

sudo chown -R ubuntu:ubuntu /data

nginxFile=/etc/nginx/sites-available;

for config in web default
do
	file="$nginxFile/$config";
	if [ -e "$file" ]
	then
		# remove hbnb_static location if it exitst
		sed -i '/^\s*location \/hbnb_static/,/}/d' "$nginxFile/$config";

		sed -i "/^\s*location \/ {/i \\\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}" "$nginxFile/$config";
	fi
done

nginx -s reload;

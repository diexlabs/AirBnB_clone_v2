# sets up static files serving on a server

# Nginx configuration file
$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 http://cuberule.com/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

$static_dir = ['/data','/data/web_static',
  '/data/web_static/releases','data/web_static/shared',
  '/data/web_static/releases/test'
]

package {'nginx':
  ensure   => 'present',
  provider => 'apt'
}

-> file {$static_dir:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0750'
}

-> file {'/data/web_static/releases/test/index.html':
  ensure  => 'file',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0750',
  content => 'Hello World',
}

-> tidy {'/data/web_static/current': }

-> file {'/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/'
}

-> exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

-> file {'/var/www':
  ensure => 'directory'
}

-> file {'/var/www/html':
  ensure => 'directory'
}

-> file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Holberton School'
}

-> file { '/var/www/html/404.html':
  ensure  => 'present',
  content => 'Ceci n\'est pas une page\n'
}

-> file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf
}

-> exec {'nginx -s reload':
  path => '/etc/init.d/'
}

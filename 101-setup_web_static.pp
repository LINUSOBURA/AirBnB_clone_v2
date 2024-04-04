# web_server_setup.pp

# Package installation
package { 'nginx':
  ensure => installed,
}

# Firewall rule
firewall { 'Allow Nginx HTTP':
  port   => 80,
  proto  => tcp,
  action => accept,
}

# Directory structure
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => 'directory',
}

# HTML index file creation
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n",
}

# Symbolic link creation
file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  force   => true,
  require => File['/data/web_static/releases/test/index.html'],
}

# Ownership
file { '/data':
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# Nginx configuration
file_line { 'nginx_location_config':
  path    => '/etc/nginx/sites-enabled/default',
  line    => '        location /hbnb_static { alias /data/web_static/current/; }',
  match   => 'listen 80 default_server',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Nginx service restart
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File_line['nginx_location_config'],
}

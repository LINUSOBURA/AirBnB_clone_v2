# Define a Puppet class for setting up web servers for deployment of web_static
class web_server_setup {

  # Update package repositories
  exec { 'apt-update':
    command => '/usr/bin/apt-get update',
    path    => '/usr/bin',
    before  => Package['nginx'],
  }

  # Install nginx package
  package { 'nginx':
    ensure  => installed,
    require => Exec['apt-update'],
  }

  # Creating directories and files
  file { '/data/web_static/releases/test/':
    ensure => directory,
  }

  file { '/data/web_static/shared/':
    ensure => directory,
  }

  file { '/data/web_static/releases/test/index.html':
    ensure  => file,
    content => '<h1>Testing Deployment</h1>',
  }

  # Creating symbolic link
  file { '/data/web_static/current':
    ensure => link,
    target => '/data/web_static/releases/test/',
    force  => true,
  }

  # Changing ownership
  file { '/data/':
    ensure  => directory,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    recurse => true,
  }

  # Inserting new location into nginx configuration server block
  file_line { 'nginx-hbnb-static':
    path    => '/etc/nginx/sites-available/default',
    line    => "        location /hbnb_static {\n\talias /data/web_static/current;\n\t}",
    match   => "^\\s*server_name",
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  # Restart nginx service
  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File_line['nginx-hbnb-static'],
  }
}

# Apply the web_server_setup class
include web_server_setup

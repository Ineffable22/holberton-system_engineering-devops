# Add a custom HTTP header with Puppet
exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

file_line { 'redirection':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=hdZUCjAQaGw permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World',
}

file_line { 'add_header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $HOSTNAME;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

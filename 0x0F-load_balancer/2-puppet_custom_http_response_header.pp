# Add a custom HTTP header with Puppet
exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

exec { 'apt-get-upgrade':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-upgrade'],
}

package { 'nginx':
  ensure => installed,
}


file_line { 'redirection':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=hdZUCjAQaGw permanent;',
}

file_line { 'add_header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server {',
  line   => "add_header X-Served-By ${HOSTNAME};",
}

file { '/var/www/html/index.html':
  content => 'Hello World',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

#!/usr/bin/env pup
# Configures SSH Replacing strings
file { '/etc/ssh/ssh_config':
  ensure => present,
}
file_line { 'Replace a line to /etc/ssh/ssh_config':
  path  => '/etc/ssh/ssh_config',
  line  => '    IdentityFile ~/.ssh/school',
  match => '^IdentityFile.*$',
}
file_line { 'Append a line to /etc/ssh/ssh_config':
  path  => '/etc/ssh/ssh_config',
  line  => '    PasswordAuthentication no',
  match => '^PasswordAuthentication.*$',
}

# Change the OS configuration so that it is possible to login with
# the holberton user and open a file without any error message.
exec { 'hard/soft':
  command => 'sed -i "s/5/50/" /etc/security/limits.conf; \
  sed -i "s/4/40/" /etc/security/limits.conf;',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

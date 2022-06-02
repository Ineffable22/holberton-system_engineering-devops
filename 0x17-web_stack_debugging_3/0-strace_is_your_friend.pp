# Repair error of configuration
exec { 'repair_server':
  provider => shell,
  command  => 'sed -i "s/class-wp-error.phpp/class-wp-error.php/g" /var/www/html/wp-settings.php',
  before   => Exec['restart_apache'],
}

exec { 'restart_apache':
  provider => shell,
  command  => 'sudo service apache2 restart',
}

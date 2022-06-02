# Repair error of configuration
exec { 'repair_server':
  provider => shell,
  command  => 'sudo sed -i "s/class-wp-error.phpp/class-wp-error.php/g" /var/www/html/wp-settings.php',
}

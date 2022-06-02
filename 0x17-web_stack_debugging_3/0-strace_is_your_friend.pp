# Repair error of configuration
exec { 'repair_server':
  command => 'sudo sed -i "s/class-wp-error.phpp/class-wp-error.php/g" /var/www/html/wp-settings.php',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

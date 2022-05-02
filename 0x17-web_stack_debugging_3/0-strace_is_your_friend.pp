# Correct name spelling error in wp-settings.php file
exec { 'modify_file':
  command => "sed -i 's|class-wp-locale.phpp|class-wp-locale.php|g' /var/www/html/wp-settings.php",
  path    => '/bin',
}

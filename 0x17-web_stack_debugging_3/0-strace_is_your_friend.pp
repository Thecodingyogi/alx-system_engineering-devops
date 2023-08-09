# Puppet code to fix a bug wp-sttings.php

exec {
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

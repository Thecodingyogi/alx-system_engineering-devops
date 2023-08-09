# Puppet code to fix a bug wp-sttings.php

exec { 'fix the php extension issue':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

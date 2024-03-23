# install_flask.pp

# Ensure python3-pip package is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask',
  path    => ['/usr/bin'],
  unless  => '/usr/bin/pip3 show Flask',
  require => Package['python3-pip'],
}

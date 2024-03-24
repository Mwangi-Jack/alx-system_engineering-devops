# using puppet to configure a client server

$file_content = file('/etc/ssh/sshd_config')

file_line {'config line':
  path    => '/etc/ssh/sshd_config',
  line    => '#   PasswordAuthentication no',
  match   => '^PasswordAuthentication no'
  ensure  => present,
  require => File['/etc/ssh/sshd_config'],
}

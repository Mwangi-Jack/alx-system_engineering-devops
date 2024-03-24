#!/usr/bin/pup
# Install a specific versioin of flask
package { 'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3'
}

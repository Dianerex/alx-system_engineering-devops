# Define a package resource to install pip3
package { 'python3-pip':
  ensure => installed,
}

# Define an exec resource to install Flask version 2.1.0 using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  creates => '/usr/local/lib/python3.x/dist-packages/flask', # Adjust the path as needed
  require => Package['python3-pip'], # Make sure pip3 is installed first
}

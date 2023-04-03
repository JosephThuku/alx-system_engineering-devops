# Install Nginx
class { 'nginx': }

# Define custom HTTP response header
file { '/etc/nginx/conf.d/custom-header.conf':
  content => "add_header X-Served-By $::hostname;",
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure => running,
  enable => true,
  require => File['/etc/nginx/conf.d/custom-header.conf'],
}


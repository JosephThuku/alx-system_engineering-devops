# Puppet script that fixes too many files opened error

exec {'fix ulimit':
  command => "sed -i 's/15/4096/g' /etc/default/nginx",
  path    => '/bin',
}

exec { 'nging restart':
    path    => '/etc/init.d',
    command => 'nginx restart'
}
# Bash script to change the OS configuration so that it is possible to login and open a file without any error message.

exec { 'fix user-limit':
  command => "sed -i 's/nofile 5/nofile 21000/g' -i 's/nofile 4/nofile 16000/g' /etc/security/limits.conf",
  path    => '/bin',
}

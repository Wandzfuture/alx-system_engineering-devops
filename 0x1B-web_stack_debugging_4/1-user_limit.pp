# Changes the OS configuration to login with the holberton
# user and open a file without any error messages

exec { 'OS security config':
  command => 'sed -i "s/^holberton.*$/holberton    hard    nofile    65535\nholberton    soft    nofile    65535/" /etc/security/limits.conf',
  path    => '/usr/bin:/bin:/usr/sbin:/sbin',
}

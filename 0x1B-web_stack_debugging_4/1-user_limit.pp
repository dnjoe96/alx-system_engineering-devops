# Change the ulimit value for holberton user

exec { 'modify_hard_limit':
  command => "sed -i 's|holberton hard nofile .*|holberton hard nofile 5000|g' /etc/security/limits.conf",
  path    => '/bin',
}

exec { 'modify_soft_limit':
  command => "sed -i 's|holberton soft nofile .*|holberton soft nofile 5000|g' /etc/security/limits.conf",
  path    => '/bin',
}

# install puppet-lint version 2.1.1
package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem',
}

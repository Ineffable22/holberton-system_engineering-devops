#!/usr/bin/env pup
# This manifest kills a process named killmenow.
exec { 'pkill':
  command => 'pkill killmenow',
  path    => '/usr/local/bin/:/bin/',
}

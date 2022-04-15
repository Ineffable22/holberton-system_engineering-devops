#!/usr/bin/env pup
# This manifests 
package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem'
  require  => 'https://rubygems.org',
}

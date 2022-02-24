#!/usr/bin/env ruby
# The challenge from Guillaume Plessis, Vice President of Infrastructure at TextMe, was accepted.
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')

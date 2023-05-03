#!/usr/bin/env ruby
#A Ruby script that accepts one argument and pass it to a aregular expression

puts ARGV[0].scan(/hb?tn/).join

#!/usr/bin/env ruby
# This Ruby script takes a command-line argument and uses a regular expression to find all occurrences
# of exactly 10 digits at the beginning (^) and end ($) of the input string.
# It then joins all the matches found in the input string and prints them out.
puts ARGV[0].scan(/^\d{10,10}$/).join

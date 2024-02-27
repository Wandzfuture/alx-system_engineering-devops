#!/usr/bin/env ruby
# This Ruby script takes a command-line argument and uses a regular expression to find all occurrences
# of zero or more uppercase letters (A-Z).
# It then joins all the matches found in the input string and prints them out.
puts ARGV[0].scan(/[A-Z]*/).join

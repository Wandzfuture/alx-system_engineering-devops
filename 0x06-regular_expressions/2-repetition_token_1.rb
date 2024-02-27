#!/usr/bin/env ruby
# This Ruby script takes a command-line argument and uses a regular expression to find all occurrences
# of the pattern "h", followed by an optional "b", followed by an optional "t", and ending with "n".
# It then joins all the matches found in the input string and prints them out.
puts ARGV[0].scan(/hb?t?n/).join

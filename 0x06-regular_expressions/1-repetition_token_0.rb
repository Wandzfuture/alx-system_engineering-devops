#!/usr/bin/env ruby
# This Ruby script takes a command-line argument and uses a regular expression to find all occurrences
# of the pattern "hbt" followed by 2 to 5 instances of the letter "t", followed by the letter "n".
# It then joins all the matches found in the input string and prints them out.
puts ARGV[0].scan(/hbt{2,5}n/).join

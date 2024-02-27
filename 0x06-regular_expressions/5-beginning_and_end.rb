#!/usr/bin/env ruby
# This Ruby script takes a command-line argument and uses a regular expression to find all occurrences
# of the pattern starting with "h", followed by any character except a newline, and ending with "n".
# The ^ and $ anchors ensure that the pattern matches the entire input string.
# It then joins all the matches found in the input string and prints them out.
puts ARGV[0].scan(/^h.n$/).join

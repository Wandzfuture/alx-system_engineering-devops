#!/usr/bin/env ruby
# This Ruby script takes a command-line argument and uses a regular expression to find all occurrences
# of the pattern "[from:", followed by any characters (non-greedy), followed by "] [to:", followed by
# any characters (non-greedy), followed by "] [flags:", followed by any characters (non-greedy), and
# ending with "]".
# It then joins all the matches found in the input string, separating them with commas, and prints them out.
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")

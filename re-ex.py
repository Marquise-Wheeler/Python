#!/usr/bin/python3
# This is an example of how to use re for pattern searching from the Python3 Library book.

import re

pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print('Found "{}"\nin "{}"\nfrom {} to ("{}")'.format(
    match.re.pattern, match.string, s, e, text[s:e]))



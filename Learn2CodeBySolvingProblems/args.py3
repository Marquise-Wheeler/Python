# This first line is the shebang it includes the path
#!/usr/bin/python3

import sys

print("you passed in", len(sys.argv), "arguments(s)")
print("those arguments are: ", str(sys.argv))

print("hello", sys.argv[1])


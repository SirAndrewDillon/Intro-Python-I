"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
from sys import platform as _platform

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE

for i in sys.argv[0]:
  print(i)

# Print out the OS platform you're using:
# YOUR CODE HERE

print(f"OS platform: {sys.platform}")

# Print out the version of Python you're using:
# YOUR CODE HERE

print(f"System Version is: {sys.version}")

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE

print(f"CUrrent Process ID: {os.getpid()}")

# Print the current working directory (cwd):
# YOUR CODE HERE

print(f"Current Dir is {os.getcwd()}")

# Print out your machine's login name
# YOUR CODE HERE

print(f"is {os.getlogin()}")
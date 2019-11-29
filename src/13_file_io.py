"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

f = open("foo.txt", "r")
data = f.read()
print(data)
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

f = open("bar.txt", "w")
f.write("Testing\n")
f.write("line 2\n")
f.write("Line 3\n")
f.close()
content = ["This is the first line\n",
           "This is the second line\n", "This is the third line\n"]
for line in content:
        f.write(line)

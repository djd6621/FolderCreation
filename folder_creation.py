import os
import sys

# enter name of text file with names in first system parameter
f = open(sys.argv[1], 'r')
for x in f:
    x = x.rstrip()
    # enter location for folders in second system parameter
    os.mkdir(sys.argv[2] + "/" + x)

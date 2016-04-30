

import sys
from subprocess import call

input_file_template = 'my_inputs.template'
input_file = 'my_inputs.txt'


print 'hi from test_driver'
print sys.argv

# Run dprepro to get right value into the file my_inputs.txt
call(['dprepro', sys.argv[1], input_file_template, input_file])

# Read the input file
f = open(input_file, 'r')
val = float( f.read() )
print 'read from file:', val

# Run the model


myfile = open(sys.argv[2], 'w')
myfile.write( str(10*val) )



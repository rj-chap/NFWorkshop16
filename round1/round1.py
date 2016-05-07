#!/usr/bin/env python
import sys
import os
import re

# First argument should be the input file (most likely "irc_privmsg.txt")
file = sys.argv[1]

# Second argument should be the output filename (try something like "irc_decoded.txt")
output_file = sys.argv[2]

outputdata = []

with open(str(file), 'r') as flow:

	for line in flow.readlines():
		if re.search('PRIVMSG', line):

			parsed_line = line.split(':')
			strip_line = parsed_line[-1].strip()


			try:
				outputdata.append(str(line + '+++ Decoded ROT13: ' + str(strip_line).decode('rot13') + '\n'))
				continue
			except:
				pass
		else:
			outputdata.append(str(line))

with open(output_file, 'wb+') as f:
    for line in outputdata:
        f.write(line)

print "Done!  See %s." % (output_file)

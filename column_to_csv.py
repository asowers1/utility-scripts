import sys
import re

func = 1

def addQuotes( str ):
	matches = re.match( '^".*"$', str )
	if matches == None:
		return '"' + str + '"'
	return str

def addCommas( str ):
	matches = re.match( '^".*"$', str )
	if matches == None:
		return str + ','
	return str

# Iterate over standard input. NOTE - this isn't line-buffered, don't try using
# this script interactively...

for line in sys.stdin:

	# Remove trailing linefeed.
	line = line.strip()

	# Split the line into parts separated by commas.
	parts = line.split( ',' )
	
	execute = False

	# Add quotes to each part that doesn't have quotes already.
	if (func == 0):
		newParts = map( addQuotes, parts )
		execute = True
	elif (func == 1):
		newParts = map( addCommas, parts )
		execute = True

	if (execute):
		# Concatenate the parts back to a single line.
		concatParts = ','.join( newParts )
		# And print it.
		print concatParts


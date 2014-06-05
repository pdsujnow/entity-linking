#! /usr/bin/env python2.7

import fileinput
import json
import string

for line in fileinput.input():
	row = json.loads(line.decode("latin-1").encode("utf-8"))
	
	mid = row['mention.id']
	text = row['mention.text']

	# get the caputal letters
	abbr = [c for c in text if c in string.uppercase]

	print json.dumps({
		"mention_id" : int(mid),
		"value" : "".join(abbr)
	})

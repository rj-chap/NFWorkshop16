#!/usr/bin/env python

def reverse(plaintext):

	alphabet = {'a': 'z',
				'b': 'y',
				'c': 'x',
				'd': 'w',
				'e': 'v',
				'f': 'u',
				'g': 't',
				'h': 's',
				'i': 'r',
				'j': 'q',
				'k': 'p',
				'l': 'o',
				'm': 'n',
				'n': 'm',
				'o': 'l',
				'p': 'k',
				'q': 'j',
				'r': 'i',
				's': 'h',
				't': 'g',
				'u': 'f',
				'v': 'e',
				'w': 'd',
				'x': 'c',
				'y': 'b',
				'z': 'a'}

	decoded = ""

	#Convert each letter to corresponding letter in the reverse alphabet
	for character in plaintext.lower():
		if character in alphabet:
			character = alphabet[character]
		decoded += character

	return decoded

decode_us = ["Wrw blf ivnvnyvi gl hsldvi zmw kfg lm xovzm fmwvidvzi uli WvuXlm?",
			 "Nln sld wrw blf tvg lm Ofpv'h xlnkfgvi?...zmw bvh.",
			 "Nln'h szev vbvh rm gsv yzxp lu gsvri svzwh...zmw z gdvoev bvzi lowh kzhhdliw rh vzhb gl tfvhh.",
			 "Bvzs R tfvhh hrmxw rg'h qfhg rorpvzorvmh."]

for decode_me in decode_us:
	print decode_me
	print reverse(decode_me) + "\n"

#!/usr/bin/python3

import random
import string

def generate_word( length ):

        VOWELS = "aeiou"
        CONSONANTS = "".join( set( string.ascii_lowercase ) - set( VOWELS ) )
        word = ""
        for i in range(length):
                if i % 2 == 0:
                        word += random.choice(CONSONANTS)
                else:
                        word += random.choice(VOWELS)
        return word

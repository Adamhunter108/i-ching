from ichingmath import Construct_Hexagram
from hexagram_key import Trigrams, Hex_Meaning
from hex_interpretation import hexagram_interpretations
import random
from random import choice


# coder input (for testing): 

# myHexagram = Construct_Hexagram()
# myHexagram.addToss("h", "t", "t")
# myHexagram.addToss("h", "h", "h")
# myHexagram.addToss("t", "h", "t") 
# myHexagram.addToss("t", "t", "t") 
# myHexagram.addToss("h", "t", "h") 
# myHexagram.addToss("t", "t", "t") 
# myHexagram.loopThroughTosses()
# print(myHexagram.getHexagram())
# print(myHexagram.getTrigram())


# user input:
def user_input():
	myHexagram = Construct_Hexagram()
	print("\nFirst Toss:")
	myHexagram.addToss(input("coin 1: "), input("coin 2: "), input("coin 3: "))
	print("\nSecond Toss:")
	myHexagram.addToss(input("coin 1: "), input("coin 2: "), input("coin 3: "))
	print("\nThird Toss:")
	myHexagram.addToss(input("coin 1: "), input("coin 2: "), input("coin 3: "))
	print("\nFourth Toss:")
	myHexagram.addToss(input("coin 1: "), input("coin 2: "), input("coin 3: "))
	print("\nFifth Toss:")
	myHexagram.addToss(input("coin 1: "), input("coin 2: "), input("coin 3: "))
	print("\nFinal Toss:")
	myHexagram.addToss(input("coin 1: "), input("coin 2: "), input("coin 3: "))
	myHexagram.loopThroughTosses()
	print('\n' + myHexagram.getHexagram())
	print(myHexagram.getTrigram() + '\n')
	# needs interpretation


# randomized input
def rando_hex():
	randomTrigram = choice(list(Trigrams.items()))
	randomHexagram  = randomTrigram + randomTrigram
	trigram_values = list(Trigrams.values())
	trigram_keys = list(Trigrams.keys())
	def getRandoTrigram(trigram_value):
		trigram = choice(trigram_value)
		line = trigram_keys[trigram_values.index(trigram)]
		for li in line:
			print(li)
		return trigram
	upper = getRandoTrigram(trigram_values)
	lower = getRandoTrigram(trigram_values)
	hex_value = Hex_Meaning[upper, lower]
	myHexagram = (f"Upper: {upper}\nLower: {lower}\nHexagram Value: {hex_value}\n" + hexagram_interpretations[hex_value])
	print(myHexagram)


def instructions():
	print("""
To consult with the Book of Changes:
Take 3 ordinary coins as similar as possible.  Think about a question that you would like guidance with.
Shake and toss all 3 coins at the same time.  Input whether they come up heads or tails.  
You may type 'heads', 'tails' or abbreviate to 'h' or 't'.
You will be prompted to do 6 tosses total. Your hexagram will be constructed.  There are 64 unique
hexagrams and each one has a value that can be independently researched and studied further.
(Google your hexagram value for more information)""")
	start()

def start():
	print("""
	☯ ☯ ☯ ☯ ☯ ☯ ☯ ☯ ☯ ☯ ☯ ☯ ☯ ☯ ☯ ☯ ☯ ☯ ☯ ☯ ☯ ☯

		Choose your path:
	Type 'm' for manual input. 
	Type 'a' for automatic computer generated tosses.
	Type 'i' for instructions.
	""")
	manual_or_auto = input("Manual, Auto or Instructions? ")
	if manual_or_auto == 'm':
		user_input()
	elif manual_or_auto == 'i':
		instructions()
	else:
		rando_hex()

print("""
		Welcome to the I Ching.	""")
start()
print("""
	                .
	         .............##
	      .................####
	    ...........###......#####
	   ...........#####......#####
	  .............###......#######
	 ......................#########
	 .....................##########
	.................################
	 ..........#####################
	 .........######################
	  .......######...#############
	   .....######.....###########
	    .....######...###########
	      ....#################
	         ..#############
	    		#

""")
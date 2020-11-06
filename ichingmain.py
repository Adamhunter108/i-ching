from ichingmath import Construct_Hexagram
from hexagram_key import Trigrams, Hex_Meaning
from hex_interpretation import hexagram_interpretations
import random
from random import choice


# user input:

# myHexagram = Construct_Hexagram()
# myHexagram.addToss(input("> "), input("> "), input("> "))
# myHexagram.addToss(input("> "), input("> "), input("> "))
# myHexagram.addToss(input("> "), input("> "), input("> "))
# myHexagram.addToss(input("> "), input("> "), input("> "))
# myHexagram.addToss(input("> "), input("> "), input("> "))
# myHexagram.addToss(input("> "), input("> "), input("> "))
# myHexagram.loopThroughTosses()
# print(myHexagram.getHexagram())
# print(myHexagram.getTrigram())


# coder input:

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


# randomized input

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

myHexagram = (f"Upper: {upper}\nLower: {lower}\nHexagram Value: {hex_value}")
print(myHexagram)


# Hexagram interpretations:

# if "1" in myHexagram:
# 	print(hexagram_interpretations["1"])
# if "2" in myHexagram:
# 	print(hexagram_interpretations["2"])
# if "3" and not "0" in myHexagram:
# 	print(hexagram_interpretations["3"])
# if "4" in myHexagram:
# 	print(hexagram_interpretations["4"])


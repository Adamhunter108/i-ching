from ichingmath import Construct_Hexagram
from hexagram_key import Trigrams, Hex_Meaning
from hex_interpretation import hexagram_interpretations
import random


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

myHexagram = Construct_Hexagram()
myHexagram.addToss("h", "t", "t")
myHexagram.addToss("h", "h", "h")
myHexagram.addToss("t", "h", "t") 
myHexagram.addToss("t", "t", "t") 
myHexagram.addToss("h", "t", "h") 
myHexagram.addToss("t", "t", "t") 
myHexagram.loopThroughTosses()
print(myHexagram.getHexagram())
print(myHexagram.getTrigram())


# Hexagram interpretations:

if "1" in myHexagram.getTrigram():
	print(hexagram_interpretations["1"])


# # randomized input

# randomTrigram = random.choice(list(Trigrams.items()))
# randomHexagram  = randomTrigram + randomTrigram
# print("Your automatic computer generated divinatory Hexagram is:\n" + str(randomHexagram)

# trigram_values = list(Trigrams.values())
# trigram_keys = list(Trigrams.keys())

# upper_trigram = choice(trigram_values)
# lower_trigram = choice(trigram_values)

# upper_lines = trigram_keys[trigram_values.index(upper_trigram)]
# lower_lines = trigram_keys[trigram_values.index(lower_trigram)]

# hex_value = Hex_Meaning[upper_trigram, lower_trigram]

# for u_line in upper_lines:
# 	print(u_line)
# for l_line in lower_lines:
# 	print(l_line)

# print("Upper: " + upper_trigram)
# print("Lower: " + lower_trigram)

# print("Hexagram Value: " + hex_value)
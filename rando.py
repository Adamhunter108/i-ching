from ichingmath import Construct_Hexagram
from hexagram_key import Trigrams, Hex_Meaning
from hex_interpretation import hexagram_interpretations
import random
from random import choice

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

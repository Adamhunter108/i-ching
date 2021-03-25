from hexagram_key import Trigrams, Hex_Meaning
from hex_interpretation import *


odd = "_____________"
even = "_____   _____"

class Construct_Hexagram:

	tosses = []
	diagram = []

	#setter
	def addToss(self, coin_a, coin_b, coin_c):
		self.tosses.append([coin_a, coin_b, coin_c])
	#getter
	def getTosses(self):
		return self.tosses

	def calcToss(self, toss):
		if "h" in toss:
			return 3
		else: 
		 	return 2

	def getHexagram(self):		
		return "\n".join(self.diagram)

	def getTrigram(self):
		upper = tuple(self.diagram[3:])
		lower = tuple(self.diagram[:3])
		return "Upper: "+ Trigrams[upper] + '\nLower: '+Trigrams[lower] + '\nHexagram Value: '+ Hex_Meaning[Trigrams[upper],Trigrams[lower]] +'\nHexagram Interpretation: ' + hexagram_interpretations[Hex_Meaning[Trigrams[upper],Trigrams[lower]]]


	def loopThroughTosses(self): 
		for i in reversed(self.tosses): 
			value = 0 
			for j in i:
				value += self.calcToss(j) 
			if value == 6 or (value % 2 != 0 and value != 9):  
				self.diagram.append(odd)
			else:
				self.diagram.append(even)

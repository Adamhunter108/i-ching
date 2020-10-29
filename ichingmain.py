from ichingmath import Construct_Hexagram
from hexagram_key import Trigrams
from hexagram_key import Hex_Meaning


# user input

# myHexagram = Construct_Hexagram()
# myHexagram.addToss(input("> "), input("> "), input("> "))
# myHexagram.addToss(input("> "), input("> "), input("> "))
# myHexagram.addToss(input("> "), input("> "), input("> "))
# myHexagram.addToss(input("> "), input("> "), input("> "))
# myHexagram.addToss(input("> "), input("> "), input("> "))
# myHexagram.addToss(input("> "), input("> "), input("> "))
# myHexagram.loopThroughTosses()
# print(myHexagram.getHexagram())

# coder input

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
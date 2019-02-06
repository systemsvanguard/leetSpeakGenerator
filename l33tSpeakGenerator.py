# l33tSpeakGenerator.py

"""
Title: L33t Code Generator 
Purpose: Takes an input string of normal English text from end-user, and generates fantastic L33t Code!
Coder: Ryan Hunter | GitHub handle: SystemsVanguard | ryan@RyanHunter.org dated 2019-Feb-05
"""

# <!--- Start -->
def convert2L33t(myString):
	l33tcode = (
		(('a', 'A'), '4'),
		(('e', 'E'), '3'),		
		(('i', 'I'), '1'),
		(('o', 'O'), '0'),		
		(('s', 'S'), '5'),
		(('t', 'T'), '7'),
		(('b', 'B'), '5'),
		(('d', 'D'), '5'),
		)
	for symbols, replaceStr in l33tcode:
		for symbol in symbols:
			myString = myString.replace(symbol, replaceStr)
	return myString

print(" ")
print("Python L33T Code Generator App")
print("Type in some English text, and watch in amazement as we translate it to L33t Code!")
print(" ")
userNormalText = input("Type your text please. : ")
print("L33t Translation -->  ", convert2L33t(userNormalText))

# <!--/ End -->

a = input("enter a value")
if(a.isalpha()):
  b = "consonant"
  if(a == "a" or a == "e" or a == "i" or a == "o" or a == "u"or a == "A" or a == "E" or a == "I" or a == "O" or a == "U"):
    b = "Vowel"
else:
  b = "invalid"
print(b)

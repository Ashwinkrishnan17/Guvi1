n = int(input())
import inflect
p = inflect.engine()
words = p.number_to_words(n)
print(words.capitalize())

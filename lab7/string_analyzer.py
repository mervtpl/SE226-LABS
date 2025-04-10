from string_package import *

str=input("enter a sentence")
print(manipulate.remove_puntiuation(str))
print(manipulate.capitalize_words(str))
print(manipulate.reverse_string(str))
print(stats.word_count(str))
print(stats.count_characters(str))
print(stats.average_word_length(str))
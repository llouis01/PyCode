# program to make proper capitalization on text from input. Py3.6
# useful when working with lots of strings that are improperly capitalized

text_to_correct = input("Enter text to correct: ")

def CorrectCap(text_to_correct):
    proper_cap = text_to_correct.capitalize() # to capitalize 1st letter of words in text.
    print (proper_cap)

CorrectCap(text_to_correct)

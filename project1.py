# Ex. 24: Write expressions for finding all words in text6 that meet the conditions listed below. 
#         The result should be in the form of a list of words: ['word1', 'word2', ...].
#           a. Ending in ise
#           b. Containing the letter z
#           c. Containing the sequence of letters pt
#           d. Having all lowercase letters except for an initial capital (i.e., titlecase)

from nltk.book import *

w_ise = [w for w in text6 if w.endswith('ise')]         # If a word in text6 ends with ise, put the word in a list named w_ise.
w_z = [w for w in text6 if 'z' in w]                    # If a word in text6 contains z, put the word in a list named w_z.
w_pt = [w for w in text6 if 'pt' in w]                  # If a word in text6 contains pt, put the word in a list named w_pt.
w_titlecase = [w for w in text6 if w.istitle()]         # If a word in text6 is titlecase, put the word in a list named w_titlecase.

# Below is where I print the lists.
# The f-strings allow me to print words and variables at the same time.
# I used \n to add line breaks to make the output more readable for myself.

print(f'\nWords in text6 that end in ise:\n{w_ise}\n')
print(f'Words in text6 that contain the letter z:\n{w_z}\n')
print(f'Words in text6 that contain the sequence of letters pt:\n{w_pt}\n')
print(f'Words in text6 that are titlecase:\n{w_titlecase}')

#--------------------------------------------------------------------------

# Ex. 25: Define sent to be the list of words ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore'].
#         Now write code to perform the following tasks:
#           a. Print all words beginning with sh
#           b. Print all words longer than four characters

sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']

w_sh = [w for w in sent if w.startswith("sh")]         # If a word in sent starts with sh, put the word in a list named w_sh.
w_four = [w for w in sent if len(w) > 4]               # If the length of a word in sent is larger than 4, put the word in a list named w_four.

# Now I'm printing the lists.
# The f-strings allow me to print words and variables at the same time.
# I used \n to add line breaks to make the output more readable for myself.

print(f'\nWords in sent that begin with sh:\n{w_sh}\n')
print(f'Words in sent that are longer than four characters:\n{w_four}')

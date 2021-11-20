#18. Write a program to print the 50 most frequent bigrams (pairs of adjacent words) of a text, omitting bigrams that contain stopwords.

#README:
#This program takes any text file you designate and generate the 50 most frequent bigrams from that file.
#Instruction: In your terminal, run the script by adding the filename of the text to the end of your command-line argument.
#e.g.: python3 project2.py sample.txt

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import sys
import re

#This parses the command-line arguments, takes the second argument, which is the filename of the text, and assigns it to the variable "filename".
if len(sys.argv) == 2:
    filename = sys.argv[1]

#In case the users run the script without specifying the text file, this enables them to still input the filename after the program has started.
if len(sys.argv) == 1:
    filename = input("Type in the filename and press enter: ")

#This reads the file and tokenizes the text string using NLTK.
textfile = open(filename)
inputtext = textfile.read()
inputtext = word_tokenize(inputtext)
textfile.close()

def fifty_most_frequent_bigrams(text):
    text_without_stopword = [word for word in text
    if word.isalpha() #Getting rid of non-alphabetical characters
    and not word.lower() in stopwords.words("english")] #Excluding words that exist in the NLTK stopword corpus
    all_bigrams = nltk.bigrams(text_without_stopword) #Generating bigrams
    frequent_bigrams = nltk.FreqDist(all_bigrams) #Generating frequency distribution
    return frequent_bigrams.most_common(50) #Keeping the top 50 most common bigrams

#This takes the tokenized text and pass it through the above program
output_list = fifty_most_frequent_bigrams(inputtext)

#This turns the output list into a string so that it can be printed into a text file.
output_str = str(output_list)

#This uses regex to identify the boundaries of the bigrams and replace them with line breaks to make the output more readable.
output_str_lines = re.sub(r'(\[\()|(\), \()|(\)])', '\\n', output_str, 0, re.MULTILINE)

#This creates a new text file with filename derived from the original filename.
#The backward slicing cuts out ".txt".
fileout = open(f'{filename[:-4]}_output.txt', 'w')

#This writes an intro line and the output bigrams into the new text file.
fileout.write(f'The 50 most frequent bigrams in {filename}:\n')
for line in output_str_lines:
    fileout.write(line)
fileout.close()

#This prompts the users to check the result in the new text file.
print(f'The 50 most frequent bigrams in the text are stored in {filename[:-4]}_output.txt')

###########################################################################################

#19. Write a program to create a table of word frequencies by genre, like the one given in 1 for modals. 
#Choose your own words and try to find words whose presence (or absence) is typical of a genre. Discuss your findings.

#README:
#This program lets users input their choice of words and creates a table of word frequencies by genre
#using the user's words and the genres available in the Brown Corpus.

import nltk
from nltk.corpus import brown

#Letting users choose the words for counting
user_words = input("Type in your words, separate them with a space (e.g., report monster classroom): ")

#Splitting the string that the user typed in and turn it into a list of words
user_words = user_words.split()

cfd = nltk.ConditionalFreqDist(
    (genre, word) #Setting the two categories
    for genre in brown.categories() #Defining "genre" as all the genres available in the Brown Corpus
    for word in brown.words(categories=genre)) #Defining "words" as all the words in the Brown Corpus's genres
cfd.tabulate(samples=user_words) #Creating a table with the words input by the user as samples

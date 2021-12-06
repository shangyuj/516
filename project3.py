# This program converts British spellings to American spellings in a text file.

import re

# Let users specify the filename and assign it to the variable "filename"
filename = input("Please type in the filename of the text (extension included): ")

# Open the text file, read the content, assign the content to the variable "text", and close the file
textfile = open(filename)
text = textfile.read()
textfile.close()

# Convert -gramme to -gram
text = re.sub(r"gramme", r"gram", text, 0, re.MULTILINE | re.IGNORECASE)

# Convert -our to -or, avoid matching -our that is proceeded by just one letter, like "tour"
text = re.sub(r"(\w{2,})our", r"\1or", text, 0, re.MULTILINE | re.IGNORECASE)

# Convert -logue to -log, avoid matching the standalone word "logue"
text = re.sub(r"\Blogue\b", r"log", text, 0, re.MULTILINE | re.IGNORECASE)
text = re.sub(r"\Blogued\b", r"logged", text, 0, re.MULTILINE | re.IGNORECASE)
text = re.sub(r"\Blogues\b", r"logs", text, 0, re.MULTILINE | re.IGNORECASE)
text = re.sub(r"\Bloguing\b", r"logging", text, 0, re.MULTILINE | re.IGNORECASE)

# Convert -ise to -ize, proceeded by the letter c, d, g, l, m, n, r, s, t, or v
# Avoid matching -ise that is proceeded by just one or two letters, like "rise" and "arise"
text = re.sub(r"(\w{3,})([cdglmnrstv])ise", r"\1\2ize", text, 0, re.MULTILINE | re.IGNORECASE)
text = re.sub(r"(\w{3,})([cdglmnrstv])ising", r"\1\2izing", text, 0, re.MULTILINE | re.IGNORECASE)

# Convert -isation to -ization
text = re.sub(r"isation", r"ization", text, 0, re.MULTILINE | re.IGNORECASE)

textfile_out = open(f'{filename[:-4]}_Americanized.txt', "w")
for line in text:
    textfile_out.write(line)
textfile_out.close()

print(f'The output is saved in "{filename[:-4]}_Americanized.txt"')

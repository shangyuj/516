# This program converts British spellings to American spellings in a text file.

import re

filename = input("Please type in the filename of the text (extension included): ")

textfile = open(filename)
text = textfile.read()
textfile.close()

# Convert -gramme to -gram
text = re.sub(r"gramme", "gram", text, 0, re.MULTILINE | re.IGNORECASE)

# Convert -our to -or, avoid matching words like "tour"
text = re.sub(r"(\w{2,})our", r"\1or", text, 0, re.MULTILINE | re.IGNORECASE)

# Convert -logue to -log
text = re.sub(r"(\w{2,})logue\b", r"\1log", text, 0, re.MULTILINE | re.IGNORECASE)
text = re.sub(r"(\w{2,})logued\b", r"\1loged", text, 0, re.MULTILINE | re.IGNORECASE)
text = re.sub(r"(\w{2,})logues\b", r"\1logs", text, 0, re.MULTILINE | re.IGNORECASE)
text = re.sub(r"(\w{2,})loguing\b", r"\1loging", text, 0, re.MULTILINE | re.IGNORECASE)

# Convert -ise to -ize, proceeded by the letter c, d, g, l, m, n, r, s, t, or v, avoid words like "rise"
text = re.sub(r"(\w{2,})([cdglmnrstv])ise", r"\1\2ize", text, 0, re.MULTILINE | re.IGNORECASE)
text = re.sub(r"(\w{2,})([cdglmnrstv])ising", r"\1\2izing", text, 0, re.MULTILINE | re.IGNORECASE)

# Convert -isation to -ization
text = re.sub(r"(\w{2,})isation", r"\1ization", text, 0, re.MULTILINE | re.IGNORECASE)

textfile_out = open(f'{filename[:-4]}_Americanized.txt', "w")
for line in text:
    textfile_out.write(line)
textfile_out.close()

print(f'The output is saved in "{filename[:-4]}_Americanized.txt"')

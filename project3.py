import re

filename = input("Please type in the filename of the text (extension included): ")

textfile = open(filename)
text = textfile.read()
textfile.close()

text = re.sub(r"(\w{2,})([cdglmnrstv])ise", "\\1\\2ize", text, 0, re.MULTILINE | re.IGNORECASE)
text = re.sub(r"(\w{2,})([cdglmnrstv])ising", "\\1\\2izing", text, 0, re.MULTILINE | re.IGNORECASE)

text = re.sub(r"(\w{2,})our", "\\1or", text, 0, re.MULTILINE | re.IGNORECASE)

text = re.sub(r"(\w{2,})isation", "\\1ization", text, 0, re.MULTILINE | re.IGNORECASE)

text = re.sub(r"gramme", "gram", text, 0, re.MULTILINE | re.IGNORECASE)

text = re.sub(r"(\w{2,})logue\b", "\\1log", text, 0, re.MULTILINE | re.IGNORECASE)
text = re.sub(r"(\w{2,})logued\b", "\\1loged", text, 0, re.MULTILINE | re.IGNORECASE)
text = re.sub(r"(\w{2,})logues\b", "\\1logs", text, 0, re.MULTILINE | re.IGNORECASE)
text = re.sub(r"(\w{2,})loguing\b", "\\1loging", text, 0, re.MULTILINE | re.IGNORECASE)

textfile_out = open(f'{filename[:-4]}_Americanized.txt', "w")
for line in text:
    textfile_out.write(line)
textfile_out.close()

print(f'The output is saved in {filename[:-4]}_Americanized.txt')
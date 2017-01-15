import re
import random

p = open('C:\\Users\\Martin\\Desktop\\laptext.txt')
process = p.read()
regexMatch = re.findall('([A-Z][^\.!?]*[\.!?])', process, re.I)
p.close()

output = open('outputText.txt', 'w')
sentences = random.sample(regexMatch, len(regexMatch))

for i in range(0, len(sentences)):
    if len(sentences[i]) < 140:
        output.write(sentences[i] + "\n")
    else:
        pass

output.close()

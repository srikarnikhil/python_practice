#The basic outline of this problem is to read the file, look for integers using the re.findall(),
# looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and
# summing up the integers.

import re

filename = input('Enter file name: ')
filehandle = open(filename)
total = 0
for line in filehandle:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        total = total + int(number)
print(total)


#The basic outline of this problem is to read the file, look for integers using the re.findall(),
# looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and
# summing up the integers.

import re
filename=input('Enter file name:')
filehandle=open(filename)
total=sum([int(number) for number in  re.findall('[0-9]+',filehandle.read())])
print('sum of all the numbers in the file ',filename,'is :',total)
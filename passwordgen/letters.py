alphl = []      #alphabet lowercase
alphu = []      #same, but upper
num = []        #0 to 9
other = []      
numofother = [33,35,36,37,38,44,46,63]      #other chars in ascii


for i in range(97,123):     #97 to 122 are the lowercase letters in ascii
    alphl.append(chr(i))        #append the letters to the list

#for j in range(65,91):      #65 to 90 are the uppercase letters in ascii
#    alphu.append(chr(j))        #append the letters to the list

for k in range(len(alphl)):     #for each lower letter, turns into upper, then add
    alphu.append(alphl[k].upper())

for l in range(48,58):      #48 to 57 are the numbers
    num.append(chr(l))

for m in range(len(numofother)):        #numofother are the numbers of 
    other.append(chr(numofother[m]))    #other char in ascii

import random
import letters as lt
import functions as fun

numascii = []   #creates a list where the numbers in ascii will be
passw = []      #password will be stored here
separator = "_______________________________________________________"


table1 = [lt.alphl,lt.alphu,lt.num,lt.other]        #list of lists, with other chars
table2 = [lt.alphl,lt.alphu,lt.num]     #list of lists, without other chars

for i in range(48,58):      #numbers in the ascii table
    numascii.append(i)


print("\nPASSWORD GENERATOR!!\n")


passlen = fun.fpasslen()       #is the length of the password

specialchar = fun.table(passlen)       #equals 1 is user wants special chars, and 0 if doesn't

def main(passw):

    if not specialchar:        #without other
        for j in range(1,passlen+1):   
            passw.append(random.choice(random.choice(table2)))
        passw = "".join(passw)
        return passw
        
    elif specialchar:      #with other
        for j in range(1,passlen+1):   
            passw.append(random.choice(random.choice(table1)))
        passw = "".join(passw)
        return passw

print("\n{}".format(separator))

passw = main(passw)  
print("your password is:\n{}\n".format(passw))

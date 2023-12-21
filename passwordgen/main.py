import random
import letters as lt
import functions as fun

numascii = []   #creates a list where the numbers in ascii will be
passw = []      #password will be stored here
table_with_other = []       #table with other chars will be stored here
table_without_other = []    #table without other chars will be stored here
separator = "_______________________________________________________"

#init the lists, with values in it
fun.init_numascii(numascii)
fun.init_with_others(table_with_other)
fun.init_without_others(table_without_other)


print("\nPASSWORD GENERATOR!!\n")


passlen = fun.fpasslen()       #gets the length of the password

specialchar = fun.table(passlen)       #true if user wants special chars

def main(passw):

    if not specialchar:        #without other
        for j in range(1,passlen+1):   
            passw.append(random.choice(random.choice(table_without_other)))
        passw = "".join(passw)
        return passw
        
    elif specialchar:      #with other
        for j in range(1,passlen+1):   
            passw.append(random.choice(random.choice(table_with_other)))
        passw = "".join(passw)
        return passw

print("\n{}".format(separator))

passw = main(passw)  
print("your password is:\n{}\n".format(passw))

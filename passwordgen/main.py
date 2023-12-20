import random
import letters as lt


numascii = []
passw = []      #password
separator = "_______________________________________________________"


table1 = [lt.alphl,lt.alphu,lt.num,lt.other]        #list of lists, with other
table2 = [lt.alphl,lt.alphu,lt.num]     #list of lists, without other



for i in range(48,58):      #numbers in the ascii table
    numascii.append(i)


print("\nPASSWORD GENERATOR!!\n")

def fpasslen():        #checks if passlen is a valid number
    print("\n{}".format(separator))
    print("first, you must type how long your password will be\n")
    while True:
        passlen = input("type how long your password will be:       ").strip()
        if passlen != "0" and passlen.isdigit() == True :
            break
        else:
            print("{} is not valid!\n".format(passlen))
            continue
    return passlen

passlen = int(fpasslen())       #is the length of the password

def table():        #checks if user wants to use special chars
    print("\ndone! your password will have {} chars!".format(passlen))
    print("\n{}".format(separator))
    print("\nnow, you have to choose if it will use special chars.")
    while True:
        b = input("type 1 if you want to use special chars, and 2 if you don't:     ")
        if b.isdigit()== True:
            if int(b)==1:
                print("\nyou want to use special chars!")
                return 1
            if int(b)==2:
                print("\nyou don't want to use special chars!")
                return 0
            else:
                print("\nyou didn't chose 1 or 2!")
                continue
        else:
            print("\nyou must type separator number!")
            continue

t=table()       #equals 1 is user wants special chars, and 0 if doesn't

def main():
    passw = []

    if t == 0:        #without other
        for j in range(1,passlen+1):   
            passw.append(random.choice(random.choice(table2)))
        passw = "".join(passw)
        return passw
        
    elif t == 1:      #with other
        for j in range(1,passlen+1):   
            passw.append(random.choice(random.choice(table1)))
        passw = "".join(passw)
        return passw

print("\n{}".format(separator))
truepass = main()
print("your password is:\n{}\n".format(truepass))

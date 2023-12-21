import letters as lt



separator = "_______________________________________________________"

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
    return int(passlen)   

def table(passlen):        #checks if user wants to use special chars
    print("\ndone! your password will have {} chars!".format(passlen))
    print("\n{}".format(separator))
    print("\nnow, you have to choose if it will use special chars.")
    while True:
        b = input("type 1 if you want to use special chars, and 2 if you don't:     ")
        if b.isdigit()== True:
            if int(b)==1:
                print("\nyou want to use special chars!")
                return True
            if int(b)==2:
                print("\nyou don't want to use special chars!")
                return False
            else:
                print("\nyou didn't chose 1 or 2!")
                continue
        else:
            print("\nyou must type separator number!")
            continue

def init_numascii(numascii):

    for i in range(48,58):      #numbers in the ascii table
        numascii.append(i)

def init_with_others(table):

    for i in lt.alphl:
        table.append(i)

    for i in lt.alphu:
        table.append(i)

    for i in lt.other:
        table.append(i)

    for i in lt.num:
        table.append(i)

def init_without_others(table):

    for i in lt.alphl:
        table.append(i)

    for i in lt.alphu:
        table.append(i)

    for i in lt.num:
        table.append(i)        
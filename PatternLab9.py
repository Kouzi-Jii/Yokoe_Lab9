#Asks for input form user
base = int(input("Please enter how many rows: "))
#Adding Needed Variables
cons = 1
num = 1
#Start of the Loop
while num <= base:
    spcer = 1 #Another Variable needed for the loops
    while spcer <= num:
        print(cons, end=" ")
        cons += 1
        spcer += 1
    print()
    num += 1
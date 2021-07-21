def FileSwap():
    fileName = input("Enter Your File: ")
    fileName2 = input("Enter Your Second File: ")
    count = 0
    with open(fileName,'r') as file:
        a = file.read()
    with open(fileName2,'r') as file2:
        b = file2.read()
    with open(fileName,'w') as file:
        file.write(b)
    with open(fileName2,'w') as file2:
        file2.write(a)
FileSwap()
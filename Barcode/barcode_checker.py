def barcodeChecker(barcode):
    if len(barcode) != 12: #Checks the length of the barcode
        return False
    elif not barcode.isnumeric(): #Checks if there are any non numeric elements in the barcode
        return False
    
    evenC=0
    oddC=0
    
    for i in range(11): #Following loop seperates the barcode elements into 2 groups
        x= int(barcode[i])
        if i%2 == 0: 
            oddC = oddC + x
        else:
            evenC = evenC + x
            
    even_lastd = evenC % 10 #Takes the last digit of the even group
    odd_lastd = oddC % 10 #Takes the last digit of the odd group
    y=((3*odd_lastd)%10 +even_lastd) % 10 #Formula for barcode last digit checking
    
    if 10-y == int(barcode[11]): #Checks if the number from the formula matches the last digit of the barcode we are given
        return True
    return False

inpf = open("barcodes.txt")
outf = open("output.txt", "w+")

for string in inpf.readlines():
    barcode = string.strip() #Seperates the barcodes in the input file
    if barcodeChecker(barcode): #If the barcode checker returns true, it is a valid barcode, if not, invalid barcode
        print(f"{barcode} is a valid 10-digits barcode", file = outf)
    else:
        print(f"{barcode} is an invalid 10-digits barcode", file = outf)

inpf.close()
outf.close()
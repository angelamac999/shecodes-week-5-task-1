# Week 5 Task 1

# Your task is to implement the algorithms to calculate and validate check digits for different kinds of barcodes.

# You must calculate and validate the check digit for:

# - Credit Cards

# - GTIN-13 Product Codes


evennum= 0
oddnum =0
evensum = []
oddsum = []
doubleevennum = []



def checkcc(string):
    for indexitem in range(len(ccnumberstring)):
        if indexitem %2 ==0:
            evennum =int(ccnumberstring[indexitem]) *2
            if evennum > 9:
                doubleevennum.append(evennum)
                evenadd= sum(doubleevennum) # problem - this is adding up all the numbers over 9 
                evensum.append(evenadd)
            else:
                evensum.append(evennum)
        else:
            oddnum = int(ccnumberstring[indexitem])
            oddsum.append(oddnum)
        
    print('this is the evensum', evensum)
    print('this is the odd sum', oddsum)
    print('this is the doubleevennum', doubleevennum)

    totaleven = sum(evensum)
    totalodd = sum(oddsum)
    total = totaleven + totalodd

    if total %10 == 0:
        print ('This is a valid credit card')
    else:
        print ("This is not a valid credit card")

ccnumberstring = input('enter the credit card you would like to check, ')
checkcc("ccnumberstring")




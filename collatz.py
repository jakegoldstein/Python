import random 
randNum = int(input("Number:\n"))
def collatz(num):
    num = randNum
    
    while num != 1:
        if num % 2 == 0:
            evenDo= num / 2
            num= evenDo
            
            print (str(evenDo))
        elif num % 2 == 1:
            oddDo=  3 * num + 1
            print (str(oddDo))
            num = oddDo

collatz(1)

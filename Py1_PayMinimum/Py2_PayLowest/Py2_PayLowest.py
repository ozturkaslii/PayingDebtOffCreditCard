#Lowest Payment
balance = 3926
annualInterestRate = 0.2
unpaidBalance = 0
monthlyInterestRate = annualInterestRate/12.0
month = 0
payment = 10

#Loop will work till balance negative
isBalanceNeg = False

while not isBalanceNeg:
    #when loop starts over, balance should be set by the first balance.
    lastBalance = balance
    for i in range(1, 13):
        unpaidBalance = lastBalance - payment
        lastBalance = round((unpaidBalance + monthlyInterestRate*unpaidBalance), 2)         
        if(i == 12):
            #check if the balance is lower than zero at 12. month
            if(lastBalance > 0):
                #when balance is higher than zero, payment should be incerased by 10.
                payment += 10
                isBalanceNeg = False
            else:
                #when balance is negative, we found our answer and we should leave the loop by setting isBalanceNeg to true.
                isBalanceNeg = True
    
print("Lowest Payment: "+ str(payment))
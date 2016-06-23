#Paying the minimum creadit card debt##
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

unpaidBalance = 0
monthlyInterestRate = annualInterestRate/12.0

month = 1
payment = 0
paymentTotal = 0

for i in range(0,12):
    payment = round(balance*monthlyPaymentRate, 2)
    paymentTotal += payment
    unpaidBalance = balance - payment
    balance = round((unpaidBalance + monthlyInterestRate*unpaidBalance), 2)
    
    print("Month: "+str(month))
    month += 1
    print("Minimum monthly payment: "+ str(payment))
    print("Remaining balance: "+str(balance))

print("Total paid: " + str(paymentTotal))
print("Remaining balance: " + str(balance))
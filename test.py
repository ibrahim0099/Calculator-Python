import math
import pandas


#HPP = input('Enter house purchase price: ')
#DP = input('Enter down payment:  ')
#IR = input('Enter interest rate (without the % sign):  ')
#MY = input('Enter term of mortgage in years:  ')
#TR = input('Enter tax rate on home (without the % sign):   ')
#HI = input('Enter home insurance (per year):   ')

HPP = 250000
DP = 50000
IR = 3.708
MY = 30
TR = 1.04
HI = 600

LA = HPP - DP
#calculate principle & interest
i = (IR / 12) / 100
nper = MY * 12
row1 = LA * i
row2 = 1 / math.pow(1+i,nper)
row3 = 1 - row2
row4 = row1 / row3
print(row4)

#monthly tax calculation
var1 = (TR * MY) / 100
var2 = var1 * HPP
var3 = var2 / nper
print(var3)

#monthly insurance calculation
tem1 = HI / 12
print(tem1)

# Total Monthly Payment 

Total = row4 + var3 + tem1

GrandTotal = row4 * nper
#print('Data : ' + ' ' + HPP + ' ' + ' ' + DP  + ' ' + IR + ' ' + MY + ' ' + TR + ' ' + HI)

print('________________________________________________________________')
print('   ------------   Monthly Payment Breakdown ------------        ')
print('   Principal and Interest:        $')
print('   Monthly Tax:                   $')
print('   Monthly Insurance:             $')
print('   Total:                         $')
print('   ------------   Monthly Payment Breakdown ------------        ')
print('   By the end of the 30-year period, you would pay ')
print('   in total payments ($200,000.00 would be for the original loan')
print('   amount and $131,729.62 in interest).')

choice = input('Do you want a Detailed Payment Schedule or a Summary Payment Schedule (D or S): ')

if choice == 'D':
    print('________________________________________________________________')
    print('   ------------   Monthly Payment Breakdown ------------        ')


elif choice == 'S':
    print('S')
    

    



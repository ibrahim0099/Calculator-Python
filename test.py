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


# Loan Remaining 
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
print('   Principal and Interest:        $',row4)
print('   Monthly Tax:                   $',var3 )
print('   Monthly Insurance:             $',tem1 )
print('   Total:                         $',Total )
print('   ------------   Monthly Payment Breakdown ------------        ')
print('   By the end of the ' , MY , '-year period, you would pay ')
print('   in total payments (' , LA , 'would be for the original loan')
print('   amount and ' , GrandTotal , 'in interest).')

choice = input('Do you want a Detailed Payment Schedule or a Summary Payment Schedule (D or S): ')

Interest = ((IR / 12) / 100) * LA
Principal = row4 - Interest
Principal_Remaining = LA - Principal
Total_Interest = Interest
if choice == 'D':
    print('________________________________________________________________')
    print('   ------------   Monthly Payment Breakdown ------------        ')  
    print('Year    Month    Principal & Interest     Principal         Interest        Principal Remaining       Total Interest')
    for x in range(MY):
        #x = x + 1
        month = 12
        for y in range(month):
            #y = y + 1 
            print(' ',x+1, '     ',y+1, '        ','{0:.2f}'.format(row4), '                ','{0:.2f}'.format(Principal), '          ','{0:.2f}'.format(Interest), '           ','{0:.2f}'.format(Principal_Remaining), '           ','{0:.2f}'.format(Total_Interest))
            LA = LA - Principal
            Interest = ((IR / 12) / 100) * LA
            Principal = row4 - Interest
            Principal_Remaining = LA - Principal
            Total_Interest = Total_Interest + Interest
            



elif choice == 'S':
    print('________________________________________________________________')
    print('   ------------   Summary Payment Schedule  ------------        ') 
    print('Year              Total Principal                       Total Interest')
    for x in range(MY + 1):
        
        month = 12
        for y in range(month):
            LA = LA - Principal
            Interest = ((IR / 12) / 100) * LA
            Principal = row4 - Interest
            Total_Principal = Total_Principal + Principal
            Total_Interest = Total_Interest + Interest
            Principal_Remaining = LA - Principal
            Total_Interest = Total_Interest + Interest
        
        print(' ',x+1,'              ','{0:.2f}'.format(Total_Principal), '           ','{0:.2f}'.format(Total_Interest))
    

    



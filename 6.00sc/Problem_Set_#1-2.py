# coding=utf-8
# Problem Set 1-2
# 2021_12_24

'''
Paying Debt Off In a Year
Monthly interest rate = Annual interest rate / 12.0
Updated balance each month = Previous balance * (1 + Monthly interest rate) – Minimum monthly payment
'''

the_outstanding_balance_on_the_credit_card = int(raw_input('Enter the outstanding balance on your credit card:'))
annual_interest_rate = float(raw_input('Enter the annual credit card interest rate as a decimal:'))
monthly_interest_rate = annual_interest_rate / 12.0

monthly_payment = 10
month = 0

while the_outstanding_balance_on_the_credit_card >0:
    if month < 12:
        the_outstanding_balance_on_the_credit_card = the_outstanding_balance_on_the_credit_card * (1 + monthly_interest_rate) - monthly_payment
        print float(the_outstanding_balance_on_the_credit_card)
        print int(monthly_payment)
        month += 1
        print int(month)
    if month == 12:
        print 'finish'
        month += 1
        monthly_payment += 10
        print int(monthly_payment)

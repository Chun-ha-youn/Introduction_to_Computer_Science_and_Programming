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

month = 0
updated_balance_each_month = the_outstanding_balance_on_the_credit_card

for monthly_payment in range(10, the_outstanding_balance_on_the_credit_card+10):
    while the_outstanding_balance_on_the_credit_card > 0:
        if month < 12:
            updated_balance_each_month = updated_balance_each_month * (1 + monthly_interest_rate) - monthly_payment
            month += 1
            if updated_balance_each_month < 0:
                print 'RESULT'
                print 'Monthly payment to pay off debt in 1 year:', int(monthly_payment)
                print 'Number of months needed:', int(month)
                print 'Balance:', round(float(updated_balance_each_month), 2)
                break
        elif month == 12:
            month += 1
            if updated_balance_each_month > 0:
                month = 0
                updated_balance_each_month = the_outstanding_balance_on_the_credit_card
                monthly_payment += 10
                if updated_balance_each_month < 0:
                    print 'RESULT'
                    print 'Monthly payment to pay off debt in 1 year:', int(monthly_payment)
                    print 'Number of months needed:', int(month)
                    print 'Balance:', round(float(updated_balance_each_month), 2)
                    break
    break

# coding=utf-8
# Problem Set 1-3
# 2021_12_25

"""
Using Bisection Search to Make the Program Faster
Monthly payment lower bound = Balance / 12.0
Monthly payment upper bound = (Balance * (1 + (Annual interest rate / 12.0)) ** 12.0) / 12.0
"""

the_outstanding_balance_on_the_credit_card = float(raw_input('Enter the outstanding balance on your credit card:'))
annual_interest_rate = float(raw_input('Enter the annual credit card interest rate as a decimal:'))
monthly_interest_rate = annual_interest_rate / 12.0

month = 0
updated_balance_each_month = the_outstanding_balance_on_the_credit_card
monthly_payment = 0.01

while monthly_payment < the_outstanding_balance_on_the_credit_card + 0.01:
    while the_outstanding_balance_on_the_credit_card > 0:
        if month < 12:
            updated_balance_each_month = updated_balance_each_month * (1 + monthly_interest_rate) - monthly_payment
            month += 1
            if updated_balance_each_month < 0:
                print 'RESULT'
                print 'Monthly payment to pay off debt in 1 year:', round(float(monthly_payment), 2)
                print 'Number of months needed:', int(month)
                print 'Balance:', round(float(updated_balance_each_month), 2)
                break
        elif month == 12:
            month += 1
            if updated_balance_each_month > 0:
                month = 0
                updated_balance_each_month = the_outstanding_balance_on_the_credit_card
                monthly_payment += 0.01
            if updated_balance_each_month < 0:
                print 'RESULT'
                print 'Monthly payment to pay off debt in 1 year:', round(float(monthly_payment), 2)
                print 'Number of months needed:', int(month)
                print 'Balance:', round(float(updated_balance_each_month), 2)
                break
    break

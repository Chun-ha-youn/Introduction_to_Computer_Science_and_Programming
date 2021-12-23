# coding=utf-8
# Problem Set 1-1
# 2021_12_21

"""
Paying Off Credit Card Debt
Minimum monthly payment = Minimum monthly payment rate x Balance
(Minimum monthly payment gets split into interest paid and principal paid)
Interest Paid = Annual interest rate / 12 months x Balance
Principal paid = Minimum monthly payment – Interest paid
Remaining balance = Balance – Principal paid
"""

the_outstanding_balance_on_the_credit_card = int(raw_input('Enter the outstanding balance on your credit card:'))
annual_interest_rate = float(raw_input('Enter the annual credit card interest rate as a decimal:'))
minimum_monthly_payment_rate = float(raw_input('Enter the minimum monthly payment rate as a decimal'))

month = 1
total_amount_paid = 0
while month < 13:
    minimum_monthly_payment = round(minimum_monthly_payment_rate * the_outstanding_balance_on_the_credit_card, 2)
    interest_Paid = round(annual_interest_rate / 12 * the_outstanding_balance_on_the_credit_card, 2)
    principal_paid = round(minimum_monthly_payment - interest_Paid, 2)
    remaining_balance = round(the_outstanding_balance_on_the_credit_card - principal_paid, 2)

    print 'Month:', int(month)
    print 'Minimum monthly payment:', float(minimum_monthly_payment)
    print 'Principle paid:', float(principal_paid)
    print 'Remaining balance:', float(remaining_balance)

    the_outstanding_balance_on_the_credit_card = remaining_balance
    total_amount_paid += minimum_monthly_payment
    month += 1

print 'RESULT'
print 'Total amount paid:', float(total_amount_paid)
print 'Remaining balance:', float(remaining_balance)

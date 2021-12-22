#Problem Set 1
#2021_12_21

'''
Paying Off Credit Card Debt
Minimum monthly payment = Minimum monthly payment rate x Balance
(Minimum monthly payment gets split into interest paid and principal paid)
Interest Paid = Annual interest rate / 12 months x Balance
Principal paid = Minimum monthly payment – Interest paid
Remaining balance = Balance – Principal paid
'''

the_outstanding_balance_on_the_credit_card = int(raw_input('Enter the outstanding balance on your credit card:'))
annual_interest_rate = float(raw_input('Enter the annual credit card interest rate as a decimal:'))
minimum_monthly_payment_rate = float(raw_input('Enter the minimum monthly payment rate as a decimal'))
print int(the_outstanding_balance_on_the_credit_card)
print float(annual_interest_rate)
print float(minimum_monthly_payment_rate)
minimum_monthly_payment = minimum_monthly_payment_rate * the_outstanding_balance_on_the_credit_card
print float(minimum_monthly_payment)
interest_Paid = annual_interest_rate / 12 * the_outstanding_balance_on_the_credit_card
principal_paid = minimum_monthly_payment - interest_Paid
remaining_balance = the_outstanding_balance_on_the_credit_card - principal_paid
print float(principal_paid)
print float(remaining_balance)

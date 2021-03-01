# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
initial_extra = 12

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    months = months + 1
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
    	principal = principal - extra_payment
    	total_paid = total_paid + extra_payment
    if principal < 0:
    	principal = 0
    print(f'Total paid ${total_paid:5.2f} Principal ${principal:5.2f} in {months:5d} months')

print(f'Total paid ${total_paid:0.2f} in {months:10d} Months')
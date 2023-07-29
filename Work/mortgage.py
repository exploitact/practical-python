# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_month = 0

extra_payment_start_month = int(input("Enter the Extra Payment Start Month ="))
extra_payment_end_month = int(input("Enter the Extra Payment End Month ="))
extra_payment = float(input("Enter the Extra Payment amount ="))

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    total_month += 1
    while extra_payment_start_month < extra_payment_end_month:
        principal = principal * (1 + rate / 12) - (extra_payment + payment)
        total_paid = total_paid + (extra_payment + payment)
        extra_payment_start_month += 1
        total_month += 1

    print(total_month, total_paid, principal)
    
print('Total paid:', total_paid, "over", total_month, "months")

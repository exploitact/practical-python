# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_month = 0
payment_extra= 3684.11
i = 0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    total_month +=1  
    while i < 12:
        principal = principal * (1+rate/12) - payment_extra
        total_paid = total_paid + payment_extra
        i +=1
        total_month +=1 
   
print('Total paid', total_paid, "over", total_month, "months")
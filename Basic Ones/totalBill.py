# Write a function called get_bill_total() that takes a bill amount and a sales tax percentage and returns the total bill amount, rounded to two decimal places.

def get_bill_total(bill, tax):
    return round(bill*(1+tax/100), 2)


print(get_bill_total(100, 5))

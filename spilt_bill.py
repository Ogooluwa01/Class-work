import math
total_bill = 84.87
no_of_friends = 3.00
amount_each_friends_owes = total_bill / no_of_friends
rounded_spilt_bill = math.ceil(amount_each_friends_owes)
tip = rounded_spilt_bill - amount_each_friends_owes
rounded_spilt_bill_int = int(rounded_spilt_bill)
total_amount_paid = rounded_spilt_bill_int * no_of_friends
total_tip_paid = total_amount_paid-total_bill
                

print("amount each friend owes: ", amount_each_friends_owes)
print("rounded_spilt_bill: ", rounded_spilt_bill)
print("tip:", tip)
print("rounded_spilt_bill_int : ", rounded_spilt_bill_int)
print("total amount paid:",total_amount_paid)
print("total tip paid:",total_tip_paid)

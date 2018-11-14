################################
# orig date: 2018-06-30
# course: Python Basics, Treehouse (pt=290)
# practice with functions, looping, if-then-else, basic data types (str, int, bool)
# also practice with git (init, status, add, config, commit, log, diff) ...

import sys
from datetime import datetime

TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100
# output: calculate tickets_remaining

def calculate_charge(num_tix):
    return (TICKET_PRICE*num_tix+SERVICE_CHARGE)

username = input("Welcome. Please enter username: ")
print("Welcome {}.".format(username))

while tickets_remaining:
    print("="*55)
    print("There are {} available.".format(tickets_remaining))
    print("-   -" * 11)
    now = datetime.now()
    time_now = now.strftime('%-I:%M:%S %p')
    print("The ticket price is ${}.00, as of {} today.".format(TICKET_PRICE, time_now))
    try:
        qty = int(input("How many tickets would you like, {}? ".format(username)))
    except ValueError as err:
        print("Sorry {}. Invalid number. ({}) There are {} available.".format(username, err, tickets_remaining))
        qty = int(input("How many tickets would you like, {}? ".format(username)))
    while qty > tickets_remaining:
        print("Sorry {}. There are not {} available; there are only {} tickets.".format(username, qty, tickets_remaining))
        qty = int(input("How many tickets would you like, {}? ".format(username)))
    while qty <= 0:
        print("Sorry {}. You have entered {}.  Please enter a valid, positive integer.  There are {} tickets available.".format(username, qty, tickets_remaining))
        qty = int(input("How many tickets would you like, {}? ".format(username)))
    print("-   -" * 11)
    print("Service charge: ${}".format(SERVICE_CHARGE))
    amount_due = calculate_charge(qty)
    print("Total: ${}".format(amount_due))

    # prompt user to proceed
    proceed = input("Would you like to proceed with this purchase? (y/N) ".lower())

    if(proceed=="y"):
        print("-   -" * 11)
        print("Tickets purchased.  Thank you!")
        # gather credit card info
        tickets_remaining -= qty
    else:
        print("purchase aborted.")

print("="*55)
print("Thank you for shopping.  There are no more tickets are available.  Have a nice day.")
print("Press any key to exit application.")
input()

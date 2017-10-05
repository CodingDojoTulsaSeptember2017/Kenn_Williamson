''' take number of cent return dict of coin denominations '''
import random

def make_change(cents):
    dollars = cents//100
    cents = cents%100
    half_dollar = cents//50
    cents = cents%50
    quarters = cents//25
    cents = cents%25
    dimes = cents//10
    cents = cents%10
    nickles = cents//5
    cents = cents%5
    pennies = cents
    change = {}
    change["dollars"] = dollars
    change["half_dollar"] = half_dollar
    change["quarters"] = quarters
    change["dimes"] = dimes
    change["nickles"] = nickles
    change["pennies"] = pennies
    return change

for money in range(0,20):
    random_value = int(random.random()*5000)
    print("The random amount is ${}.".format(random_value/100))
    print(make_change(random_value))



final_price = 0
def calculate_total(topping_count, final_price):
    while topping_count != "done":
        topping_count = str(input("Enter your toppings (pepperoni, mushrooms, extra cheese) "
        "Type 'done' if finished: "))
        if topping_count == "pepperoni":
            final_price = final_price + 1
        elif topping_count == "mushrooms":
            final_price = final_price + 1
        elif topping_count == "extra cheese":
            final_price = final_price + 1
        else:
            print("Not in the menu")
    final_price = (final_price* 1.50) + 10.00
    
    return final_price

def main():
    topping_count = str(input("Enter your toppings (pepperoni, mushrooms, extra cheese)" \
    "Type 'done' if finished: "))
    print(calculate_total(topping_count, final_price))

main()
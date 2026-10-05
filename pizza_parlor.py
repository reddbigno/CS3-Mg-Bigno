def calculate_total(topping_count):
    base_pizza_price = 10.00
    total_toppings = topping_count * 1.50
    final_price = total_toppings + base_pizza_price
    
    return final_price


is_topping = True
topping_count = 0
discount = 0

while is_topping:
    
    user_input = input("Choose any topping: \n " +
                       "1. Pepperoni \n" +
                       "2. Mushrooms \n" +
                       "3. Extra Cheese \n" +
                       "Your choice: ")
    
    if user_input == "done":
        break
    
    if user_input == "pepperoni" or user_input == "mushrooms" or user_input == "extra cheese":
        topping_count += 1
        print(user_input, " added to your pizza \n")
    else:
        print("Not in the menu \n")
    
    
    print("Topping Count", topping_count, "\n")


sub_total = calculate_total(topping_count)

user_input = input("Do you have any discount code?: ")

if user_input == "PYTHON20":
    discount = sub_total * 0.20


total_price = sub_total - discount

print("Total toppings: ", topping_count)
print("Subtotal: ", sub_total)
print("Discount: ", discount)
print("Total Price: ", total_price)

def calculate_shipping(cart_total: float, shipping_speed: str) -> float:
    shipping_fee = 0
    if shipping_speed == "express":
        shipping_fee = 20
    elif shipping_speed == "overnight":
        shipping_fee = 35
    elif shipping_speed == "standard" and cart_total >= 100:
        shipping_fee = 0
    elif shipping_speed == "standard" and cart_total < 100:
        shipping_fee = 10
    else:
        print("Not in the shipping speed choices")


    return cart_total + shipping_fee

user_cart_total = int(input("Enter cart total: "))
shipping_speed = input("Enter shipping speed: ")

print("Cart Total:", calculate_shipping(user_cart_total, shipping_speed))

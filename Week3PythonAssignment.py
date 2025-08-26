#Python Week3 Assignment

def calculate_discount(price, discount_percent):
    """
    Calculating the final price after a discount.
    If the discount is less than 20%, then it has to return the originaal price

    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount        
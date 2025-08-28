#Python Week3 Assignment

def calculate_discount(price, discount_percent):
    """
    Calculating the final price after a discount.
    If the discount is less than 20%, then it has to return the originaal price

    """
    #Checking if the discount is 20% or higher
    if discount_percent >= 20.0:
        #Calculating the discount amount
        discount_amount = (discount_percent / 100) * price
        #Calculating the final price
        final_price = price - discount_amount
        return final_price
    else:
        return price

    #Prompting user for the input

    try:
        original_price = float(input("Enter the original price of the item: "))
        discount_percentage = float(input)
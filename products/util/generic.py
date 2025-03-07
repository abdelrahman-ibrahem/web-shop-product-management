

def get_djust_price(default_price, stock_quantity):
    price = float(default_price)
    if stock_quantity < 10:  # Low stock
        price *= 1.10  # Increase price by 10%
    elif stock_quantity > 50:  # High stock
        price *= 0.90  # Decrease price by 10%
    return price
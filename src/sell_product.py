from utils.file_handler import read_json, write_json
from utils.validators import validate_positive_number

def sell_product():
    product_name = input("Enter product name to sell: ")
    products = read_json('data/products.json')

    if product_name not in products:
        print("Product not found.")
        return
    
    # Check available quantity
    available_quantity = products[product_name]['quantity']
    if available_quantity == 0:
        print("Sorry, this product is out of stock.")
        return

    # Input for quantity to sell
    quantity_to_sell = input(f"Enter quantity to sell (max {available_quantity}): ")
    if not validate_positive_number(quantity_to_sell) or int(quantity_to_sell) <= 0:
        print("Invalid quantity. Please try again.")
        return

    quantity_to_sell = int(quantity_to_sell)
    
    if quantity_to_sell > available_quantity:
        print(f"Not enough stock. Only {available_quantity} available.")
        return

    # Update the quantity and record the sale
    products[product_name]['quantity'] -= quantity_to_sell
    sale = {
        "product": product_name,
        "quantity": quantity_to_sell,
        "total": products[product_name]['price'] * quantity_to_sell
    }

    # Update sales data
    sales = read_json('data/sales.json')
    sales.append(sale)
    write_json('data/products.json', products)
    write_json('data/sales.json', sales)

    print(f"Sold {quantity_to_sell} of {product_name} for a total of {sale['total']}!")

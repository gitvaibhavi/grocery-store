from utils.file_handler import read_json, write_json
from utils.validators import validate_non_empty_string, validate_positive_number

def add_product():
    products = read_json('data/products.json')

    # Input for product name
    product_name = input("Enter product name: ")
    if not validate_non_empty_string(product_name):
        print("Invalid product name. Please try again.")
        return
    
    # Input for product price
    product_price = input("Enter product price: ")
    if not validate_positive_number(product_price):
        print("Invalid price. Please enter a valid number greater than 0.")
        return
    
    # Input for product quantity
    product_quantity = input("Enter product quantity: ")
    if not validate_positive_number(product_quantity):
        print("Invalid quantity. Please enter a valid number greater than 0.")
        return
    
    # Adding product to the store
    products[product_name] = {
        "price": float(product_price),
        "quantity": int(product_quantity)
    }

    write_json('data/products.json', products)
    print(f"Product '{product_name}' added successfully!")


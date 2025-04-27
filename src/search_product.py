from utils.file_handler import read_json

def search_product():
    product_name = input("Enter product name to search: ")
    products = read_json('data/products.json')

    if product_name in products:
        details = products[product_name]
        print(f"Product found: {product_name} | Price: {details['price']} | Quantity: {details['quantity']}")
    else:
        print(f"Product '{product_name}' not found.")

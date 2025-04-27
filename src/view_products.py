from utils.file_handler import read_json

def view_products():
    products = read_json('data/products.json')
    if not products:
        print("No products available.")
        return
    
    print("\nAvailable Products:")
    for product_name, details in products.items():
        print(f"{product_name}: Price: {details['price']} | Quantity: {details['quantity']}")

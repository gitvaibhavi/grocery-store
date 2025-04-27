from utils.file_handler import read_json

def generate_sales_report():
    sales = read_json('data/sales.json')
    if not sales:
        print("No sales data available.")
        return

    total_sales = sum(sale['total'] for sale in sales)
    print(f"\nTotal Sales: {total_sales}")
    print("Sales History:")
    
    for sale in sales:
        print(f"{sale['product']} | Quantity: {sale['quantity']} | Total: {sale['total']}")

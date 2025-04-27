from src.add_product import add_product
from src.view_products import view_products
from src.search_product import search_product
from src.sell_product import sell_product
from src.sales_report import generate_sales_report

def main():
    while True:
        print("\nWelcome to the Grocery Store Management System")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Sell Product")
        print("5. Generate Sales Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            sell_product()
        elif choice == "5":
            generate_sales_report()
        elif choice == "6":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

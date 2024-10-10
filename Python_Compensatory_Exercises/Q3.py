products = {}

def add_product(name, price, code):
    if code not in products:
        products[code] = {'name': name, 'price': price}
        print(f"Product {name} added.")
    else:
        print("Error: Product with this unique code already exists.")

def display_products():
    for code, details in products.items():
        print(f"Code: {code}, Name: {details['name']}, Price: {details['price']}")

def remove_product(code):
    if code in products:
        del products[code]
        print(f"Product with code {code} removed.")
    else:
        print("Error: Product not found.")

def edit_product(code):
    if code in products:
        new_name = input("Enter new name: ")
        new_price = float(input("Enter new price: "))
        products[code] = {'name': new_name, 'price': new_price}
        print(f"Product with code {code} has been updated.")
    else:
        print("Error: Product not found.")

def search_product_name(query):
    flag = True
    for code, details in products.items():
        if query in (details['name']):
            flag = False
            print(f"Found - Code: {code}, Name: {details['name']}, Price: {details['price']}")
    if flag:
        print("Product not found.")

def search_product_code(query):
    flag = True
    for code, details in products.items():
        if query in code:
            print(f"Found - Code: {code}, Name: {details['name']}, Price: {details['price']}")
            flag = False
    if flag:
        print("Product not found.")

def display_summary():
    total_products = len(products)
    total_value = sum(details['price'] for details in products.values())
    print(f"Total products: {total_products}, Total value: {total_value}")

def display_help():
    print("Commands: add, display, remove, edit, searchn: search by name, searchc: search by code, summary: details, help, exit")

def main():
    while True:
        command = input("Enter command (add/display/remove/edit/searchn/searchc/summary/help/exit): ").lower()
        
        if command == 'add':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            code = input("Enter product unique code: ")
            add_product(name, price, code)
            
        elif command == 'display':
            display_products()
            
        elif command == 'remove':
            code = input("Enter product unique code to remove: ")
            remove_product(code)
            
        elif command == 'edit':
            code = input("Enter product unique code to edit: ")
            edit_product(code)
            
        elif command == 'searchn':
            query = input("Enter product name to search: ")
            search_product_name(query)

        elif command == 'searchc':
            query = input("Enter product code to search: ")
            search_product_code(query)
            
        elif command == 'summary':
            display_summary()
            
        elif command == 'help':
            display_help()
            
        elif command == 'exit':
            print("Exiting program.")
            break
            
        else:
            print("Invalid command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()
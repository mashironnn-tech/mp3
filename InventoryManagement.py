# ============================================
# MACHINE PROBLEM #2 - INVENTORY MANAGEMENT
# ============================================

from datetime import datetime

inventory = {}
sales_history = []


def add_product():
    print("\n=== ADD PRODUCT ===")

    product_id = input("Enter Product ID: ")

    if product_id in inventory:
        print("Product already exists!")
        return

    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    stock = int(input("Enter Initial Stock: "))

    inventory[product_id] = {
        "name": name,
        "price": price,
        "stock": stock
    }

    print("Product added successfully!")


def update_product():
    print("\n=== UPDATE PRODUCT ===")

    product_id = input("Enter Product ID: ")

    if product_id not in inventory:
        print("Product not found!")
        return

    print("[1] Update Name")
    print("[2] Update Price")
    print("[3] Update Stock")

    choice = input("Enter Choice: ")

    if choice == "1":
        inventory[product_id]["name"] = input("Enter New Name: ")

    elif choice == "2":
        inventory[product_id]["price"] = float(input("Enter New Price: "))

    elif choice == "3":
        inventory[product_id]["stock"] = int(input("Enter New Stock: "))

    else:
        print("Invalid choice!")
        return

    print("Product updated successfully!")


def record_sale():
    print("\n=== RECORD SALE ===")

    product_id = input("Enter Product ID: ")

    if product_id not in inventory:
        print("Product not found!")
        return

    quantity = int(input("Enter Quantity Sold: "))

    if quantity > inventory[product_id]["stock"]:
        print("Not enough stock!")
        return

    inventory[product_id]["stock"] -= quantity

    total = quantity * inventory[product_id]["price"]

    sale_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sales_history.append({
        "product": inventory[product_id]["name"],
        "quantity": quantity,
        "total": total,
        "date": sale_time
    })

    print(f"Sale Recorded! Total = ₱{total:.2f}")


def low_stock_alert():
    print("\n=== LOW STOCK ALERT ===")

    found = False

    for product_id, product in inventory.items():
        if product["stock"] <= 5:
            found = True
            print("-" * 40)
            print(f"ID    : {product_id}")
            print(f"Name  : {product['name']}")
            print(f"Stock : {product['stock']}")

    if not found:
        print("No low stock products.")


def total_inventory_value():
    print("\n=== TOTAL INVENTORY VALUE ===")

    total = 0

    for product in inventory.values():
        total += product["price"] * product["stock"]

    print(f"Total Inventory Value: ₱{total:.2f}")


def search_product():
    print("\n=== SEARCH PRODUCT ===")

    keyword = input("Enter Product ID or Name: ").lower()

    found = False

    for product_id, product in inventory.items():
        if keyword == product_id.lower() or keyword in product["name"].lower():
            found = True
            print("-" * 40)
            print(f"ID    : {product_id}")
            print(f"Name  : {product['name']}")
            print(f"Price : ₱{product['price']:.2f}")
            print(f"Stock : {product['stock']}")

    if not found:
        print("Product not found!")


def view_sales_history():
    print("\n=== SALES HISTORY ===")

    if not sales_history:
        print("No sales history!")
        return

    for sale in sales_history:
        print("-" * 40)
        print(f"Product  : {sale['product']}")
        print(f"Quantity : {sale['quantity']}")
        print(f"Total    : ₱{sale['total']:.2f}")
        print(f"Date     : {sale['date']}")


def view_products():
    print("\n=== PRODUCT LIST ===")

    if not inventory:
        print("No products available!")
        return

    for product_id, product in inventory.items():
        print("-" * 40)
        print(f"ID    : {product_id}")
        print(f"Name  : {product['name']}")
        print(f"Price : ₱{product['price']:.2f}")
        print(f"Stock : {product['stock']}")


while True:
    print("\n" + "=" * 50)
    print("      INVENTORY MANAGEMENT SYSTEM")
    print("=" * 50)
    print("[1] Add Product")
    print("[2] Update Product")
    print("[3] Record Sale")
    print("[4] Low Stock Alert")
    print("[5] Total Inventory Value")
    print("[6] Search Product")
    print("[7] View Sales History")
    print("[8] View Products")
    print("[9] Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        update_product()

    elif choice == "3":
        record_sale()

    elif choice == "4":
        low_stock_alert()

    elif choice == "5":
        total_inventory_value()

    elif choice == "6":
        search_product()

    elif choice == "7":
        view_sales_history()

    elif choice == "8":
        view_products()

    elif choice == "9":
        print("Thank you for using the Inventory System!")
        break

    else:
        print("Invalid choice!")
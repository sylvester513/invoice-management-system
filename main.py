import mysql.connector

# CONNECT TO DATABASE
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="invoice_db"
)

cursor = connection.cursor()


# ================= CUSTOMERS =================
def manage_customers():
    while True:
        print("\n--- CUSTOMER MENU ---")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("5. Back")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")

            sql = "INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, email, phone))
            connection.commit()
            print("Customer added!")

        elif choice == "2":
            cursor.execute("SELECT * FROM customers")
            for row in cursor.fetchall():
                print(row)

        elif choice == "3":
            customer_id = input("Enter Customer ID to update: ")
            new_name = input("New Name: ")

            sql = "UPDATE customers SET name=%s WHERE id=%s"
            cursor.execute(sql, (new_name, customer_id))
            connection.commit()
            print("Customer updated!")

        elif choice == "4":
            customer_id = input("Enter Customer ID to delete: ")

            sql = "DELETE FROM customers WHERE id=%s"
            cursor.execute(sql, (customer_id,))
            connection.commit()
            print("Customer deleted!")

        elif choice == "5":
            break

        else:
            print("Invalid choice")


# ================= PRODUCTS =================
def manage_products():
    while True:
        print("\n--- PRODUCT MENU ---")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Back")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Product Name: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))

            sql = "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, price, stock))
            connection.commit()
            print("Product added!")

        elif choice == "2":
            cursor.execute("SELECT * FROM products")
            for row in cursor.fetchall():
                print(row)

        elif choice == "3":
            product_id = input("Enter Product ID to update: ")
            new_price = float(input("New Price: "))

            sql = "UPDATE products SET price=%s WHERE id=%s"
            cursor.execute(sql, (new_price, product_id))
            connection.commit()
            print("Product updated!")

        elif choice == "4":
            product_id = input("Enter Product ID to delete: ")

            sql = "DELETE FROM products WHERE id=%s"
            cursor.execute(sql, (product_id,))
            connection.commit()
            print("Product deleted!")

        elif choice == "5":
            break

        else:
            print("Invalid choice")


# ================= USERS =================
def manage_users():
    while True:
        print("\n--- USER MENU ---")
        print("1. Add User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Back")

        choice = input("Choose: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            role = input("Role (admin/cashier): ")

            sql = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
            cursor.execute(sql, (username, password, role))
            connection.commit()
            print("User added!")

        elif choice == "2":
            cursor.execute("SELECT * FROM users")
            for row in cursor.fetchall():
                print(row)

        elif choice == "3":
            user_id = input("Enter User ID to update: ")
            new_role = input("New Role: ")

            sql = "UPDATE users SET role=%s WHERE id=%s"
            cursor.execute(sql, (new_role, user_id))
            connection.commit()
            print("User updated!")

        elif choice == "4":
            user_id = input("Enter User ID to delete: ")

            sql = "DELETE FROM users WHERE id=%s"
            cursor.execute(sql, (user_id,))
            connection.commit()
            print("User deleted!")

        elif choice == "5":
            break

        else:
            print("Invalid choice")


# ================= MAIN MENU =================
while True:
    print("\n===== INVOICE MANAGEMENT SYSTEM =====")
    print("1. Manage Customers")
    print("2. Manage Products")
    print("3. Manage Users")
    print("4. Exit")

    main_choice = input("Choose option: ")

    if main_choice == "1":
        manage_customers()

    elif main_choice == "2":
        manage_products()

    elif main_choice == "3":
        manage_users()

    elif main_choice == "4":
        break

    else:
        print("Invalid option")

connection.close()
print("System Closed.")
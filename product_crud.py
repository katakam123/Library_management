import mysql.connector


# ---------------------------------------
# Database Connection
# ---------------------------------------
def connect_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Patel@123",
            database="product_db"
        )

        return connection

    except mysql.connector.Error as e:
        print("Database connection error:", e)
        return None


# ---------------------------------------
# Add Product
# ---------------------------------------
def add_product():
    print("\n--- Add Product ---")

    name = input("Enter Product Name: ").strip()

    if name == "":
        print("Product name cannot be empty.")
        return

    try:
        price = float(input("Enter Product Price: "))
        quantity = int(input("Enter Product Quantity: "))

        if price < 0:
            print("Price cannot be negative.")
            return

        if quantity < 0:
            print("Quantity cannot be negative.")
            return

        connection = connect_database()

        if connection is None:
            return

        cursor = connection.cursor()

        query = """
        INSERT INTO products
        (product_name, price, quantity)
        VALUES (%s, %s, %s)
        """

        values = (name, price, quantity)

        cursor.execute(query, values)

        connection.commit()

        print("Product added successfully!")
        print("Product ID:", cursor.lastrowid)

        cursor.close()
        connection.close()

    except ValueError:
        print("Error: Enter valid price and quantity.")

    except mysql.connector.Error as e:
        print("Database error:", e)


# ---------------------------------------
# View All Products
# ---------------------------------------
def view_products():
    print("\n--- All Products ---")

    connection = connect_database()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        query = """
        SELECT product_id, product_name, price, quantity
        FROM products
        ORDER BY product_id
        """

        cursor.execute(query)

        products = cursor.fetchall()

        if len(products) == 0:
            print("No products found.")
        else:
            print("-" * 70)
            print(
                f"{'ID':<8}"
                f"{'Product Name':<25}"
                f"{'Price':<15}"
                f"{'Quantity':<10}"
            )
            print("-" * 70)

            for product in products:
                print(
                    f"{product[0]:<8}"
                    f"{product[1]:<25}"
                    f"{product[2]:<15}"
                    f"{product[3]:<10}"
                )

            print("-" * 70)

        cursor.close()
        connection.close()

    except mysql.connector.Error as e:
        print("Database error:", e)


# ---------------------------------------
# Search Product
# ---------------------------------------
def search_product():
    print("\n--- Search Product ---")

    try:
        product_id = int(input("Enter Product ID: "))

        connection = connect_database()

        if connection is None:
            return

        cursor = connection.cursor()

        query = """
        SELECT product_id, product_name, price, quantity
        FROM products
        WHERE product_id = %s
        """

        cursor.execute(query, (product_id,))

        product = cursor.fetchone()

        if product:
            print("\nProduct Found")
            print("----------------------")
            print("Product ID :", product[0])
            print("Product Name:", product[1])
            print("Price       :", product[2])
            print("Quantity    :", product[3])
        else:
            print("Product not found.")

        cursor.close()
        connection.close()

    except ValueError:
        print("Error: Product ID must be a number.")

    except mysql.connector.Error as e:
        print("Database error:", e)


# ---------------------------------------
# Update Product
# ---------------------------------------
def update_product():
    print("\n--- Update Product ---")

    try:
        product_id = int(input("Enter Product ID to update: "))

        connection = connect_database()

        if connection is None:
            return

        cursor = connection.cursor()

        # Check whether product exists
        cursor.execute(
            "SELECT * FROM products WHERE product_id = %s",
            (product_id,)
        )

        product = cursor.fetchone()

        if product is None:
            print("Product not found.")
            cursor.close()
            connection.close()
            return

        print("\nEnter new product details")

        name = input("Enter Product Name: ").strip()
        price = float(input("Enter Product Price: "))
        quantity = int(input("Enter Product Quantity: "))

        if name == "":
            print("Product name cannot be empty.")
            return

        if price < 0:
            print("Price cannot be negative.")
            return

        if quantity < 0:
            print("Quantity cannot be negative.")
            return

        query = """
        UPDATE products
        SET product_name = %s,
            price = %s,
            quantity = %s
        WHERE product_id = %s
        """

        values = (name, price, quantity, product_id)

        cursor.execute(query, values)

        connection.commit()

        print("Product updated successfully!")

        cursor.close()
        connection.close()

    except ValueError:
        print("Error: Enter valid product details.")

    except mysql.connector.Error as e:
        print("Database error:", e)


# ---------------------------------------
# Delete Product
# ---------------------------------------
def delete_product():
    print("\n--- Delete Product ---")

    try:
        product_id = int(input("Enter Product ID to delete: "))

        connection = connect_database()

        if connection is None:
            return

        cursor = connection.cursor()

        # Check whether product exists
        cursor.execute(
            "SELECT product_name FROM products WHERE product_id = %s",
            (product_id,)
        )

        product = cursor.fetchone()

        if product is None:
            print("Product not found.")
            cursor.close()
            connection.close()
            return

        confirm = input(
            f"Are you sure you want to delete '{product[0]}'? (y/n): "
        ).lower()

        if confirm == "y":
            query = "DELETE FROM products WHERE product_id = %s"

            cursor.execute(query, (product_id,))

            connection.commit()

            print("Product deleted successfully!")

        else:
            print("Delete operation cancelled.")

        cursor.close()
        connection.close()

    except ValueError:
        print("Error: Product ID must be a number.")

    except mysql.connector.Error as e:
        print("Database error:", e)


# ---------------------------------------
# Main Menu
# ---------------------------------------
def main():
    while True:

        print("\n================================")
        print("     PRODUCT CRUD APPLICATION")
        print("================================")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            print("Thank you for using Product CRUD Application!")
            break

        else:
            print("Invalid choice. Please try again.")


# ---------------------------------------
# Start Program
# ---------------------------------------
if __name__ == "__main__":
    main()
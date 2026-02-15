import mysql.connector
from mysql.connector import Error
import random
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "billa"),
            database=os.getenv("DB_NAME", "ai_db"),
            port=int(os.getenv("DB_PORT", "3306"))
        )
        return connection
    except Error as e:
        print("Error connecting to MySQL:", e)
        return None


def create_tables():
    connection = get_connection()
    if connection is None:
        return

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            price FLOAT
        )
    """)


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_id INT,
            quantity INT,
            sale_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            price_at_sale FLOAT,
            discount_percent FLOAT,
            day_of_week INT,
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()
    print("Tables created successfully!")


def random_date():
    start = datetime(2025, 1, 1)
    end = datetime(2026, 1, 1)
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))


def populate_market_data():
    connection = get_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()

       
        cursor.execute("DELETE FROM orders")
        cursor.execute("DELETE FROM products")
        cursor.execute("ALTER TABLE products AUTO_INCREMENT = 1")
        cursor.execute("ALTER TABLE orders AUTO_INCREMENT = 1")
        cursor.execute("UPDATE products SET price =30000 WHERE name LIKE '%Laptop%'")

       
        categories = {
            "Electronics": ["Phone", "Laptop", "Tablet", "Headphones", "Camera", "Smartwatch"],
            "Home": ["Sofa", "Table", "Chair", "Lamp", "Curtains", "Bed"],
            "Fashion": ["Shirt", "Jeans", "Shoes", "Jacket", "Watch", "Sunglasses"],
            "Fitness": ["Dumbbell", "Yoga Mat", "Treadmill", "Cycle", "Kettlebell"],
            "Books": ["Python Book", "AI Guide", "Math Book", "Notebook", "Planner"],
            "Kitchen": ["Mixer", "Toaster", "Cooker", "Knife Set", "Blender"],
            "Kids": ["Toy Car", "Puzzle", "Doll", "Lego Set", "Story Book"],
            "Office": ["Printer", "Mouse", "Keyboard", "Desk", "Whiteboard"],
            "Outdoor": ["Tent", "Backpack", "Flashlight", "Sleeping Bag", "Boots"],
            "Health": ["Thermometer", "BP Monitor", "Sanitizer", "Mask", "Vitamins"]
        }

        products_to_add = []
        for _ in range(150):
            category = random.choice(list(categories.keys()))
            item = random.choice(categories[category])
            name = f"{category} {item} Model {random.randint(100,999)}"
            price = round(random.uniform(5, 2000), 2)
            if "Laptop" in name:
                price += 20000
            products_to_add.append((name, price))

        cursor.executemany(
            "INSERT INTO products (name, price) VALUES (%s, %s)",
            products_to_add
        )

        
        cursor.execute("SELECT id FROM products")
        product_ids = [row[0] for row in cursor.fetchall()]

      
        orders_to_add = []

        for _ in range(150):
            product_id = random.choice(product_ids)
            sale_time = random_date()
            weekday = sale_time.weekday()

            if weekday >= 5:
                quantity = random.randint(3, 8)
                discount = random.uniform(5, 20)
            else:
                quantity = random.randint(1, 4)
                discount = random.uniform(0, 10)

            if random.random() < 0.1:
                quantity += random.randint(5, 10)
                discount += random.uniform(20, 40)

            price = round(random.uniform(10, 2000), 2)
            

            orders_to_add.append((
                product_id,
                quantity,
                sale_time,
                price,
                round(discount, 2),
                weekday
            ))

        cursor.executemany("""
            INSERT INTO orders 
            (product_id, quantity, sale_time, price_at_sale, discount_percent, day_of_week)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, orders_to_add)

        connection.commit()
        print("150 Products + 150 ML-ready sales records inserted!")

    except Error as e:
        print("Error inserting data:", e)
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    create_tables()
    populate_market_data()

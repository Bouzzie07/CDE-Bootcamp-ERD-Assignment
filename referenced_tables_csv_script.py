from faker import Faker
from faker_food import FoodProvider
import csv
import random

# Initialize Faker and add the FoodProvider
fake = Faker()
fake.add_provider(FoodProvider)

# Number of records to generate
num_outlets = 50
num_customers = 100
num_ingredients = 50
num_suppliers = 20
num_orders = 100
num_stocks = 50

# Read address IDs from the addresses.csv file
address_ids = []
with open('addresses.csv', mode='r') as addresses_file:
    csv_reader = csv.reader(addresses_file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        address_ids.append(row[0])

# Open Restaurant Outlets CSV file for writing
with open('outlets.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['outlet_id', 'name', 'address', 'email_address', 'phone_number', 'address_id'])
    
    for item in range(num_outlets):
        outlet_id = fake.unique.random_int(min=1, max=100)
        name = fake.company()
        address = fake.street_address()
        contact_number = fake.phone_number()
        email_address = fake.email()
        address_id = random.choice(address_ids)
        
        # Write the row for each outlet
        writer.writerow([outlet_id, name, address, email_address, contact_number, address_id])

print("Outlet CSV generated with valid address IDs.")

# Supplier Table
with open('suppliers.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['supplier_id', 'name', 'address', 'email_address', 'phone_number', 'address_id', 'date_created'])

    for item in range(num_suppliers):  # Move this inside the with block
        supplier_id = fake.unique.random_int(min=1, max=100)
        name = fake.company()
        address = fake.street_address()
        contact_number = fake.phone_number()
        email_address = fake.email()
        address_id = random.choice(address_ids)
        date_created = fake.date_this_year()
        
        # Write the row for each supplier
        writer.writerow([supplier_id, name, address, email_address, contact_number, address_id, date_created])

print("suppliers.csv generated with valid address IDs.")


# Customer Table
with open('customers.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['customer_id', 'first_name', 'last_name', 'address', 'email_address', 'phone_number', 'address_id', 'date_created'])
    
    for item in range(num_customers):
        customer_id = fake.unique.random_int(min=1, max=10000)
        first_name = fake.first_name()
        last_name = fake.last_name()
        address = fake.street_address()
        phone_number = fake.phone_number()
        email_address = fake.email()
        address_id = random.choice(address_ids)
        date_created = fake.date_this_year()
        
        # Write the row for each customer
        writer.writerow([customer_id, first_name, last_name, address, email_address, phone_number, address_id, date_created])

print("customers.csv generated with valid address IDs.")




# Orders Table
# Read IDs from the customers, restaurant outlets, payments, and deliveries CSVs
customer_ids = []
restaurant_outlet_ids = []
payment_ids = []
delivery_ids = []

# Read customer IDs
with open('customers.csv', mode='r') as customers_file:
    csv_reader = csv.reader(customers_file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        customer_ids.append(row[0])

# Read restaurant outlet IDs
with open('outlets.csv', mode='r') as outlets_file:
    csv_reader = csv.reader(outlets_file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        restaurant_outlet_ids.append(row[0])

# Read payment IDs
with open('payments.csv', mode='r') as payments_file:
    csv_reader = csv.reader(payments_file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        payment_ids.append(row[0])

# Read delivery IDs
with open('deliveries.csv', mode='r') as deliveries_file:
    csv_reader = csv.reader(deliveries_file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        delivery_ids.append(row[0])

# Orders Table
order_statuses = ['Completed', 'Pending', 'Canceled', 'Processing']

with open('orders.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['id', 'customer_id', 'restaurant_outlet_id', 'order_date', 'total_amount', 'status', 'payment_id', 'delivery_id', 'dining_option'])
    
    for item in range(num_orders):
        order_id = fake.unique.random_int(min=1, max=10000)
        customer_id = random.choice(customer_ids)
        restaurant_outlet_id = random.choice(restaurant_outlet_ids)
        order_date = fake.date_this_year()
        total_amount = round(random.uniform(10.0, 500.0), 2)
        status = random.choice(order_statuses)
        payment_id = random.choice(payment_ids)
        delivery_id = random.choice(delivery_ids)
        dining_option = random.choice(['Eat-in', 'Take-out', 'Online'])
        
        # Write the row for each order
        writer.writerow([order_id, customer_id, restaurant_outlet_id, order_date, total_amount, status, payment_id, delivery_id, dining_option])

print("orders.csv generated with valid IDs.")


# Create Stock Table
# Read ingredient and menu item IDs
ingredient_ids = []
menu_item_ids = []

# Read ingredient IDs
with open('ingredients.csv', mode='r') as ingredients_file:
    csv_reader = csv.reader(ingredients_file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        ingredient_ids.append(row[0])

# Read menu item IDs
with open('menu_items.csv', mode='r') as menu_items_file:
    csv_reader = csv.reader(menu_items_file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        menu_item_ids.append(row[0])

# Stock Table
with open('stocks.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['id', 'ingredient_id', 'menu_item_id', 'quantity_used', 'unit_measure', 'reorder_level', 'date'])
    
    for item in range(num_stocks):
        stock_id = fake.unique.random_int(min=1, max=10000)
        ingredient_id = random.choice(ingredient_ids)
        menu_item_id = random.choice(menu_item_ids)
        quantity_used = fake.random_int(min=1, max=100)
        unit_measure = ('g')
        reorder_level = fake.random_int(min=10, max=100)
        date = fake.date_this_year()
        
        # Write the row for each stock entry
        writer.writerow([stock_id, ingredient_id, menu_item_id, quantity_used, unit_measure, reorder_level, date])

print("stocks.csv generated with valid IDs.")

# Create Junction table between Outlet & Menu Item to determine optional and core food.
# Read outlets and menu items data
outlet_ids = []
with open('outlets.csv', mode='r') as outlets_file:
    csv_reader = csv.reader(outlets_file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        outlet_ids.append(row[0])

menu_items = []
with open('menu_items.csv', mode='r') as menu_items_file:
    csv_reader = csv.reader(menu_items_file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        menu_items.append({'menu_item_id': row[0], 'is_core': row[5]})  # Assuming the is_core column is the 6th column


with open('outlet_menu_services.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['outlet_id', 'menu_item_id', 'is_optional'])

    # Add core items to all outlets
    for menu_item in menu_items:
        if menu_item['is_core'] == 'True':  # If it's a core item
            for outlet_id in outlet_ids:
                writer.writerow([outlet_id, menu_item['menu_item_id'], 'False'])

    # Randomly assign optional items to some outlets
    for menu_item in menu_items:
        if menu_item['is_core'] == 'False':  # If it's an optional item
            for outlet_id in outlet_ids:
                # Randomly decide if the item will be in this outlet
                if random.choice([True, False]):
                    writer.writerow([outlet_id, menu_item['menu_item_id'], 'True'])

print("outlet_menu_services.csv file created")

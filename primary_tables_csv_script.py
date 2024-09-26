from faker import Faker
from faker_food import FoodProvider
import csv
import random

# Initialize Faker and add the FoodProvider
fake = Faker()
fake.add_provider(FoodProvider)

# Number of records to generate
num_dining_option = 10


# Payment Table
dining_option = ['Eat In', 'Take Out', 'Online']
dining_options = []
for item in range(num_dining_option):
    payment = {
        'id': fake.unique.random_int(min=1, max=10000),
        'dining_option': random.choice(payment_methods)
    }
    dining_options.append(dining_option)

# Delivery Table
delivery_options = ['Standard', 'Express', 'Pickup']
deliveries = []
for item in range(num_deliveries):
    delivery = {
        'id': fake.unique.random_int(min=1, max=10000),
        'delivery_option_name': random.choice(delivery_options),
        'description': fake.text(max_nb_chars=50)
    }
    deliveries.append(delivery)

# Menu_item Table
menu_items = []
for item in range(num_menu_items):
    menu_item = {
        'id': fake.unique.random_int(min=1, max=10000),
        'name': fake.dish(),
        'description': fake.dish_description(),
        'price': round(random.uniform(5.0, 50.0), 2),
        'availability': random.choice([True, False]),
        'is_it_core': random.choice([True, False]),
        'date_created': fake.date_this_year(),
        'date_updated': fake.date_this_year()
    }
    menu_items.append(menu_item)

# Promotion Table
promotions = []
for item in range(num_promotions):
    promotion = {
        'id': fake.unique.random_int(min=1, max=10000),
        'name': fake.catch_phrase(),
        'description': fake.text(max_nb_chars=100),
        'start_date': fake.date_this_year(),
        'end_date': fake.date_between(start_date='+1d', end_date='+1y')
    }
    promotions.append(promotion)

# Write all data to respective CSV files
def write_to_csv(data, filename):
    if data:
        with open(filename, mode='w') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

# Save each table to a CSV file
# Write to a CSV file
write_to_csv(addresses, 'addresses.csv')
write_to_csv(payments, 'payments.csv')
write_to_csv(deliveries, 'deliveries.csv')
write_to_csv(menu_items, 'menu_items.csv')
write_to_csv(promotions, 'promotions.csv')

print("Generated all data and saved to CSV files.")

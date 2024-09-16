```Case Study: Fufu Republic```
**Overview:**
<p>Fufu Republic is a popular restaurant chain in Nigeria with multiple outlets nationwide. While the
core menu is standardized, some items vary by location (e.g., the Agege branch may sell
Chinese Rice, while the Lekki branch might not). Customers can order online through the
website or visit outlets for dine-in or take-out.</p>

**Payment Methods:**
The restaurant accepts:
● Cash
● Debit card payments via Nomba POS terminals at outlets
● Online payments processed through gateways like Nomba Web Checkout, Paystack,
Interswitch etc.

**Challenges:**
1. Inventory Management:
Variations in customer demand and menu items across branches make it challenging to
maintain optimal stock levels.
2. Customer Experience:
The restaurant aims to improve the customer experience by offering personalized
promotions based on purchasing behavior.

**Objective:**
Fufu Republic wants to leverage data to:
● Understand sales trends across locations, payment methods, and dining options
(dine-in, take-out, online).
● Manage stock levels efficiently, reducing waste and ensuring availability.
● Enhance customer experience by analyzing purchasing habits and tailoring promotions
accordingly.

**Task**
As a recently hired data engineer at Fufu Republic, you have been tasked with developing a
dimensional model to address the business's needs for data-driven decision-making.
1. Map out the necessary entities, relationships and constraints: This should be a
model (Any degree of abstraction is okay)

***Entities***
- Restaurant-outlet: id, name, address, contact_number, email_address
- Customer: id, first_name, last_name, phone_number, email_address, date_created, address
- Payment: id, payment_method, description
- Delivery: id, delivery_option_name, description
- Menu_item: id, name, description, price, availability, is_it_core?, ingredient_id, date_created, date_updated
- Ingredient: id, name, description, supplier_id, cost, quantity
- Dining option: eat-in, take-out, online
- Supplier: id, company_name, phone_number, email, address, date_created
- Promotion: id, name, description, start_date, end_date
- Orders: id, customer_id, restaurant_outlet_id, Order_date, total_amount, status, payment_id, delivery_id, dining_option
- Stock: id, ingredient_id, menu_item_id, quantity_used, unit_measure, reorder_level, date


***Relationships***
- Here are the relationships and cardinalities between the entities:
1. Restaurant-outlet can have many orders (one-to-many)
2. A Customer can places many orders (one-to-many).
3. Payment is used in many orders (one-to-many).
4. Delivery is associated with many orders (one-to-many).
5. Menu_item contains many Ingredients / Ingredient is used in many Menu_items (many-to-many). Hence a junction table will be needed here to reference menu_item table and ingredient table
7. Supplier supplies many ingredients (one-to-many).
8. Promotion can be applied to many orders (one-to-many).
9. Orders can include many menu_items (many-to-many). Hence a junction table will be needed here to reference orders table and menu_item table
10. Each outlet's inventory (stock) tracks ingredients (many-to-one).
11. Each outlet's stock tracks menu_items depleting the ingredients (many-to-one).
12. Dining option is associated with many orders (one-to-many).


***Constraints***
- Unique IDs: Each entity must have a unique identifier.
- Foreign Keys: Ensure referential integrity between related tables and should not be null in orders table, stocks table most especially.
- Domain Constraints: Attributes like dining_option, payment_method should conform to predefined values to avoid human error.
- Business rule should apply to the core food services and optional food services

2. Create a dimensional model:
○ Identify a business process of your choice
In relation to one of the challenges;
Inventory Management for Menu Planning: this involves  tracking ingredient inventory, ensuring ingredients are available for preparation of menu items, managing stock levels, and optimizing ingredient usage based on menu item demand. With proper reporting in place using data analysis tool; it will help FuFu Republic to track the frequency usage (daily, weekly, monthly) of ingredients based on popular demand, create a target for notification for re-ordering putting into consideration the duration of delivery from the suppliers.

○ List the business question under the business process you selected
- How much of each ingredient is used for each menu item?
- What are the current stock levels of ingredients required for menu items?
- How often do we run out of ingredients needed for popular menu items?
- What is the cost impact of ingredient shortages or excess inventory?
- How accurate are our forecasts for ingredient needs based on menu item sales?
- How quick is the supply delivery time?

○ Identify the grain, dimensions and fact.
Grain: One row per usage of ingredient in menu item preparation. This consists of the ingredient, quantity used, related menu-item, unit-measure, cost

Dimensions:
Menu_item: id, name, description, price, availability, is_it_core?, ingredient_id, date_created, date_updated
Ingredient: id, name, description, supplier_id, cost
Supplier: id, company_name, phone_number, email, address, date_created
Date: id, date, year, month, day

Fact:
stock table: id, ingredient_id, menu_item_id, quantity_used, quantity_remaining, reorder_level, date

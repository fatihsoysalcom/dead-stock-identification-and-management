import datetime

def identify_dead_stock(inventory, days_threshold=365):
    """Identifies items in inventory that haven't been sold for a specified period."""
    dead_stock_items = []
    today = datetime.date.today()

    for item_id, item_data in inventory.items():
        last_sale_date = item_data.get('last_sale_date')

        if last_sale_date:
            # Convert string date to date object for comparison
            last_sale_dt = datetime.datetime.strptime(last_sale_date, '%Y-%m-%d').date()
            days_since_last_sale = (today - last_sale_dt).days

            # If days since last sale exceed the threshold, it's dead stock
            if days_since_last_sale > days_threshold:
                dead_stock_items.append({
                    'id': item_id,
                    'name': item_data['name'],
                    'days_since_sale': days_since_last_sale,
                    'quantity': item_data['quantity']
                })
        else:
            # If there's no sale date recorded and quantity > 0, it's potentially dead stock
            # This assumes items are added to inventory with a sale date upon first sale
            if item_data['quantity'] > 0:
                 dead_stock_items.append({
                    'id': item_id,
                    'name': item_data['name'],
                    'days_since_sale': 'N/A (No sales recorded)',
                    'quantity': item_data['quantity']
                })
    return dead_stock_items

def manage_dead_stock(dead_stock_items):
    """Provides basic management suggestions for identified dead stock."""
    print("\n--- Dead Stock Management Suggestions ---")
    if not dead_stock_items:
        print("No dead stock identified. Great job!")
        return

    for item in dead_stock_items:
        print(f"\nItem ID: {item['id']}, Name: {item['name']}, Quantity: {item['quantity']}")
        print(f"  - Days since last sale: {item['days_since_sale']}")
        print("  Suggestions:")
        print("    1. Consider a significant discount or clearance sale.")
        print("    2. Bundle with popular items.")
        print("    3. Donate or dispose if unsalvageable.")
        print("    4. Analyze why it became dead stock (e.g., poor purchasing, market changes).")

# --- Example Usage ---

# Sample inventory data (simulating a small business inventory)
# 'last_sale_date' is crucial for identification
inventory_data = {
    'SKU001': {'name': 'Summer Dress', 'quantity': 10, 'last_sale_date': '2022-07-15'},
    'SKU002': {'name': 'Winter Scarf', 'quantity': 5, 'last_sale_date': '2023-01-20'},
    'SKU003': {'name': 'Old Gadget Model X', 'quantity': 3, 'last_sale_date': '2021-11-01'},
    'SKU004': {'name': 'Trendy T-Shirt', 'quantity': 20, 'last_sale_date': '2023-10-01'},
    'SKU005': {'name': 'Seasonal Decor', 'quantity': 8, 'last_sale_date': '2022-12-10'},
    'SKU006': {'name': 'New Arrival Shoes', 'quantity': 15, 'last_sale_date': datetime.date.today().strftime('%Y-%m-%d')},
    'SKU007': {'name': 'Unsold Item', 'quantity': 2, 'last_sale_date': None} # Item with no sale history
}

# Define the threshold for dead stock (e.g., 365 days = 1 year)
days_to_consider_dead = 365

print(f"Identifying dead stock with a threshold of {days_to_consider_dead} days...")

# Identify dead stock items
identified_dead_stock = identify_dead_stock(inventory_data, days_to_consider_dead)

if identified_dead_stock:
    print("\n--- Identified Dead Stock Items ---")
    for item in identified_dead_stock:
        print(f"- ID: {item['id']}, Name: {item['name']}, Quantity: {item['quantity']}, Days since last sale: {item['days_since_sale']}")

    # Suggest management strategies
    manage_dead_stock(identified_dead_stock)
else:
    print("\nNo dead stock found based on the current threshold.")

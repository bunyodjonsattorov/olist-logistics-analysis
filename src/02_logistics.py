"""
Logistics Analysis - Order Status and Revenue
"""

import pandas as pd

# Load data
orders_df = pd.read_csv("data/olist_orders_dataset.csv")
items_df = pd.read_csv("data/olist_order_items_dataset.csv")

# Combine orders and items
combined_df = pd.merge(orders_df, items_df, on='order_id')

# Revenue by order status
revenue_by_status = combined_df.groupby('order_status')['price'].sum().sort_values(ascending=False)

print("\n=== REVENUE BY ORDER STATUS ===")
print(revenue_by_status)
print(f"\nTotal Revenue: R$ {revenue_by_status.sum():,.2f}")
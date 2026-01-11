"""
Olist E-commerce Data Exploration
================================
Initial exploration of the Olist order items dataset.
Analyzes seller performance, pricing patterns, and data structure.

Author: Bunyodjonsattorov
Date: 2026-01-11
"""

import pandas as pd

# Load the dataset
print("Loading dataset...")
data = pd.read_csv("data/olist_order_items_dataset.csv")
df = pd.DataFrame(data)

# 1. Dataset Overview
print("\n=== DATASET OVERVIEW ===")
print(f"Dataset shape: {df.shape}")
print(f"Total rows: {df.shape[0]:,}, Total columns: {df.shape[1]}")
print("\nFirst 5 rows:")
print(df.head())

# 2. High-Value Items Analysis (Price > R$100)
print("\n=== HIGH-VALUE ITEMS ANALYSIS ===")
price_filter = df[df["price"] > 100]
print(f"Items with price > R$100: {len(price_filter):,}")
print(f"Percentage of total: {(len(price_filter) / len(df) * 100):.2f}%")

# 3. Top 5 Sellers by Total Revenue
print("\n=== TOP 5 SELLERS BY REVENUE ===")
top_sellers = df.groupby("seller_id")["price"].sum().sort_values(ascending=False)
print(top_sellers.head(5))
print(f"\nTop seller total revenue: R$ {top_sellers.iloc[0]:,.2f}")

print("\n✅ Analysis complete!")

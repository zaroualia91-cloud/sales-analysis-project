import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('sales_data.csv')

# 1. Total sales
total_sales = df['Total_Sales'].sum()
print(f"Total Sales: ${total_sales}")

# 2. Sales by Category
category_sales = df.groupby('Category')['Total_Sales'].sum()
print("\nSales by Category:")
print(category_sales)

# 3. Sales by Region
region_sales = df.groupby('Region')['Total_Sales'].sum()
print("\nSales by Region:")
print(region_sales)

# 4. Top Product
top_product = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
print("\nTop Products:")
print(top_product)

# Simple visualization
category_sales.plot(kind='bar', title='Sales by Category')
plt.ylabel('Total Sales ($)')
plt.savefig('sales_by_category.png')
print("\nChart saved!")

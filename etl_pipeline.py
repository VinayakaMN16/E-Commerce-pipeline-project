import pandas as pd

customers = pd.read_csv("Data/olist_customers_dataset.csv")
orders = pd.read_csv("Data/olist_orders_dataset.csv")
products = pd.read_csv("Data/olist_products_dataset.csv")
payments = pd.read_csv("Data/olist_order_payments_dataset.csv")
order_items = pd.read_csv("Data/olist_order_items_dataset.csv")

print("Customers:", customers.shape)
print("Orders:", orders.shape)
print("Products:", products.shape)
print("Payments:", payments.shape)
print("Order Items:", order_items.shape)

print(customers.isnull().sum())
print(orders.isnull().sum())

print("Customers Duplicates:",
      customers.duplicated().sum())

print("Orders Duplicates:",
      orders.duplicated().sum())

print("Products Duplicates:",
      products.duplicated().sum())

print("Payments Duplicates:",
      payments.duplicated().sum())

print("Order Items Duplicates:",
      order_items.duplicated().sum())
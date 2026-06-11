import pandas as pd

customers = pd.read_csv(
    "Data/olist_customers_dataset.csv"
)
orders = pd.read_csv(
    "Data/olist_orders_dataset.csv"
)
order_items = pd.read_csv(
    "Data/olist_order_items_dataset.csv"
)
payments = pd.read_csv(
    "Data/olist_order_payments_dataset.csv"
)
products = pd.read_csv(
    "Data/olist_products_dataset.csv"
)

fact_sales = pd.merge(
    orders,
    customers,
    on="customer_id",
    how="left"
)

fact_sales = pd.merge(
    fact_sales,
    order_items,
    on="order_id",
    how="left"
)

fact_sales = pd.merge(
    fact_sales,
    payments,
    on="order_id",
    how="left"
)

fact_sales = pd.merge(
    fact_sales,
    products,
    on="product_id",
    how="left"
)

print(fact_sales.shape)

fact_sales.to_csv(
    "Data/fact_sales.csv",
    index=False
)

print("Fact Sales Created Successfully")

print("\nColumns:")
print(fact_sales.columns.tolist())

print("\nTotal Orders:")
print(fact_sales["order_id"].nunique())

print("\nTotal Customers:")
print(fact_sales["customer_id"].nunique())

print("\nTotal Revenue:")
print(round(fact_sales["payment_value"].sum(), 2))
# app.py
import pandas as pd

def read_data(file_path):
    """Reads CSV data from the given file path."""
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        raise RuntimeError(f"Error reading the CSV file: {e}")

def compute_monthly_revenue(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.to_period('M')
    df['revenue'] = df['product_price'] * df['quantity']
    monthly_revenue = df.groupby('month')['revenue'].sum().reset_index()
    monthly_revenue['month'] = monthly_revenue['month'].astype(str)  # Convert period to string
    return monthly_revenue

def compute_product_revenue(data):
    """Computes total revenue for each product."""
    data['revenue'] = data['product_price'] * data['quantity']
    product_revenue = data.groupby('product_name')['revenue'].sum().reset_index()
    return product_revenue

def compute_customer_revenue(data):
    """Computes total revenue for each customer."""
    data['revenue'] = data['product_price'] * data['quantity']
    customer_revenue = data.groupby('customer_id')['revenue'].sum().reset_index()
    return customer_revenue

def top_customers_by_revenue(customer_revenue, top_n=10):
    """Identifies the top N customers by revenue generated."""
    top_customers = customer_revenue.sort_values(by='revenue', ascending=False).head(top_n).reset_index(drop=True)
    return top_customers

def main(file_path):
    data = read_data(file_path)
    monthly_revenue = compute_monthly_revenue(data)
    product_revenue = compute_product_revenue(data)
    customer_revenue = compute_customer_revenue(data)
    top_customers = top_customers_by_revenue(customer_revenue)
    
    return {
        'monthly_revenue': monthly_revenue,
        'product_revenue': product_revenue,
        'customer_revenue': customer_revenue,
        'top_customers': top_customers
    }

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python app.py <path_to_orders.csv>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    result = main(file_path)
    print("Monthly Revenue:")
    print(result['monthly_revenue'])
    print("\nProduct Revenue:")
    print(result['product_revenue'])
    print("\nCustomer Revenue:")
    print(result['customer_revenue'])
    print("\nTop Customers:")
    print(result['top_customers'])

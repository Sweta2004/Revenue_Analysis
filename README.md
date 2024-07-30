# Problem Statement

You have been given a dataset of customer orders from an online store. The data is in a CSV file `orders.csv` with the following columns:

- `order_id`: Unique identifier for each order
- `customer_id`: Unique identifier for each customer
- `order_date`: Date when the order was placed
- `product_id`: Unique identifier for each product
- `product_name`: Name of the product
- `product_price`: Price of the product
- `quantity`: Quantity of the product ordered

Your task is to write a Python program that performs the following tasks:

1. **Compute the total revenue generated by the online store for each month in the dataset.**
2. **Compute the total revenue generated by each product in the dataset.**
3. **Compute the total revenue generated by each customer in the dataset.**
4. **Identify the top 10 customers by revenue generated.**



# My Task

**My Task** is a containerized application designed for processing and analyzing revenue data from a CSV file. It provides details on:

- Monthly revenue
- Product revenue
- Customer revenue
- Top customers based on spending

The application is built using Docker to ensure a consistent development and testing environment.

## Prerequisites

Before you start, ensure you have the following installed:

- **Docker**: For containerizing the application.
- **Docker Compose**: For managing multi-container Docker applications.

## Getting Started

Follow these steps to set up and run the application:

# Docker Overview
Docker is used to containerize the application, ensuring a consistent environment across different machines. Here's how Docker is used in this project:

## Dockerfile
Defines the image for the application, including all dependencies required to run app.py.
## Dockerfile.test
Defines the image for running tests, including all necessary dependencies.
## docker-compose.yml
Manages multi-container setups, including:
### app: The main application container.
### test: The container for running tests.
### postgres: The PostgreSQL database service.

##Commands

### Build Docker Images:
```sh
docker compose build
```
This command builds the Docker images defined in the Dockerfiles.

### Running the Application:
```sh
docker compose up app
```
This command starts the application container.

### Running Tests:
```sh
docker compose up test
```
This command starts the test container.

### Stopping and Cleaning Up:
```sh
docker compose down
```
This command stops and removes all containers defined in the docker-compose.yml file.

## PostgreSQL Integration
The application uses PostgreSQL for data management. The docker-compose.yml file includes PostgreSQL as a service, along with the application and test services. 

## Troubleshooting
If you encounter issues:
- **Docker Daemon Issues:** Ensure Docker Desktop is running.
- **Permission Problems:** Run Docker commands as administrator or adjust permissions.
- **Build Failures:** Check Dockerfile for correct dependencies.


## Key Files
- **Dockerfile:** Defines the application image build.
- **Dockerfile.test:** Defines the test image build.
- **docker-compose.yml:** Docker Compose configuration.
- **requirements.txt:** Lists Python packages needed for the app.
- **app.py:** Contains the main application logic.
- **test_app.py:** Contains the test cases for the application.


# app.py

## 1. Importing Pandas
- **import pandas as pd**: We use Pandas, a powerful library for handling data, to read and analyze the CSV file.

## 2. Reading the Data
- **read_data(file_path)**: This function takes the path to our CSV file and loads the data into a Pandas DataFrame. If something goes wrong (like if the file isn’t found), it raises an error.

## 3. Calculating Monthly Revenue
- **compute_monthly_revenue(df)**: This function figures out how much revenue we made each month. It does this by:
  - Converting the order dates into a format that Pandas can work with.
  - Extracting just the month from these dates.
  - Calculating the revenue for each order (price times quantity).
  - Summing up the revenue for each month and converting the month column into a readable format.

## 4. Calculating Revenue by Product
- **compute_product_revenue(data)**: This function calculates the total revenue for each product. It groups the data by product name and sums up the revenue for each.

## 5. Calculating Revenue by Customer
- **compute_customer_revenue(data)**: This function calculates how much revenue each customer has generated. It groups the data by customer ID and sums up their revenue.

## 6. Finding Top Customers
- **top_customers_by_revenue(customer_revenue, top_n=10)**: This function identifies the top customers based on their total revenue. It sorts the customers by revenue in descending order and picks the top N (default is 10) customers.

## 7. Putting It All Together
- **main(file_path)**: This function orchestrates everything. It:
  - Reads the data from the CSV file.
  - Calculates monthly revenue, product revenue, and customer revenue.
  - Finds the top customers by revenue.
  - Returns all these results in a structured format.

## 8. Running the Script
- **Command-Line Execution**: If you run this script directly from the command line, it expects one argument: the path to the CSV file. It then processes the file and prints out:
  - Monthly revenue
  - Revenue by product
  - Revenue by customer
  - The top customers by revenue
 
## 9. PostgreSQL Integration
-**Database Setup:** PostgreSQL is used for storing and managing the revenue data.
The PostgreSQL service is defined in the docker-compose.yml file.

This script helps in analyzing revenue data by breaking it down into meaningful insights such as monthly trends, product performance, customer contributions, and identifying top customers.

# test_app.py

## How `test_app.py` Works with `app.py`

1. **Imports Functions**:
   - `test_app.py` imports functions from `app.py` so it can test them.

2. **Defines Tests**:
   - It creates specific tests for each function, checking if they give the right results.

3. **Provides Sample Data**:
   - `test_app.py` uses example data to test the functions.

4. **Compares Results**:
   - It runs the functions with the sample data and compares the actual output to the expected results.

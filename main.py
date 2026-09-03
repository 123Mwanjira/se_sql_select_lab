# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")

employee_data = pd.read_sql("""SELECT * FROM employees""", conn)

print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")



# STEP 2
df_first_five = pd.read_sql("""
SELECT employeeNumber, lastName
FROM employees
""", conn)

print("---------------------Step 2---------------------")
print(df_first_five)
print("-------------------End Step 2-------------------")

# STEP 3
df_five_reverse = pd.read_sql("""
SELECT lastName, employeeNumber
FROM employees
""", conn)

print("---------------------Step 3---------------------")
print(df_five_reverse)
print("-------------------End Step 3-------------------")

# STEP 4
df_alias = pd.read_sql("""SELECT lastName, employeeNumber AS ID
FROM employees
""", conn)

print("---------------------Step 4---------------------")
print(df_alias)
print("-------------------End Step 4-------------------")

df_executive = pd.read_sql("""
SELECT jobTitle,
       CASE
           WHEN jobTitle = "President" THEN "Executive"
           WHEN jobTitle = "VP Sales" THEN "Executive"
           WHEN jobTitle = "VP Marketing" THEN "Executive"
           ELSE "Not Executive"
       END AS role
FROM employees
""", conn)

print("---------------------Step 5---------------------")
print(df_executive)
print("-------------------End Step 5-------------------")

# STEP 6
df_name_length = pd.read_sql("""
SELECT LENGTH(lastName) AS name_length
FROM employees
""", conn)

print("---------------------Step 6---------------------")
print(df_name_length)
print("-------------------End Step 6-------------------")


# STEP 7
df_short_title = pd.read_sql("""
SELECT SUBSTR(jobTitle, 1, 2) AS short_title
FROM employees
""", conn)

print("---------------------Step 7---------------------")
print(df_short_title)
print("-------------------End Step 7-------------------")

order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)

print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")

# STEP 8
sum_total_price = pd.read_sql("""
SELECT ROUND(priceEach * quantityOrdered) AS total_price
FROM orderDetails
""", conn).sum()

print("---------------------Step 8---------------------")
print(sum_total_price)
print("-------------------End Step 8-------------------")

# STEP 9
df_day_month_year = pd.read_sql("""
SELECT orderDate,
       STRFTIME('%d', orderDate) AS day,
       STRFTIME('%m', orderDate) AS month,
       STRFTIME('%Y', orderDate) AS year
FROM orders
""", conn)

print("---------------------Step 9---------------------")
print(df_day_month_year)
print("-------------------End Step 9-------------------")
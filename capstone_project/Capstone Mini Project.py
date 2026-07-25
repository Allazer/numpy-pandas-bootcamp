"""
This project will simulate a real-world data analysis task.

Scenario

You work as a junior data analyst for an online electronics store.

The sales department gives you this NumPy dataset:

"""

import numpy as np

sales = np.array([
    [101, 25000, 5],
    [102, 18000, 3],
    [103, 32000, 7],
    [104, 15000, 2],
    [105, 28000, 6],
    [106, 35000, 8],
    [107, 22000, 4],
    [108, 40000, 9]
])

"""
Each row contains:

Customer ID
Amount Spent (KES)
Items Purchased
"""

# Task 1 - Display the entire dataset.
print(sales)

#Task 2 - Display only the "Amount Spent" column.
print(sales[:, 1])

#Task 3 - Display only customers who spent more than 25,000 KES.
print(sales[sales[ : , 1] >= 25000])

"""
Task 4 - 
Calculate:

Total sales
Average spending
Highest purchase
Lowest purchase
"""

# Total sales
print(sales[: , 1].sum())

# Average Spending
print(sales[: , 1].mean())

# Highest purchase
print(sales[: , 1].max())

# Lowest purchase
print(sales[: , 1].min())

# Task 5 - Increase every customer's spending by 10% 
# Store it in a new array called updated_sales

updated_sales = sales[:, 1] * 1.10

# Task 6 - Display customers who bought more than 5 items.
print(sales[sales[:, -1] > 5])

# Task 7 - Find the customer who spent the most.

# Display the entire row.
print(sales[:,1].argmax())

"""
 Task 8 - 
 Create a new column called

Average Price Per Item

Formula:

Amount Spent / Items Purchased

Append this column to the dataset.

The final dataset should have 4 columns.

 """

avg_price = sales[:,1] / sales[:,2]

avg_price = avg_price.reshape(-1, 1)

np.hstack((sales, avg_price))
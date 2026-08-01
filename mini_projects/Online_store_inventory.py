import pandas as pd

inventory = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Brand": ["Dell", "Logitech", "HP", "Samsung", "Canon"],
    "Price": [950, 25, 45, 300, 180],
    "Stock": [12, 150, 80, 30, 20]
}

df = pd.DataFrame(inventory)


"""
Part A – Understanding the DataFrame

Q1 -How many rows and columns does this DataFrame have?

Q2- How many Series make up this DataFrame?

Q3 - What would df.shape return?

Q4 - What would df.columns display (describe it or write the output)?

Part B – Selecting Columns

Q5 - What is returned by:

df["Brand"]
A. Series
B. DataFrame
Q6

What is returned by:

df[["Brand", "Price"]]
A. Series
B. DataFrame
Q7

Without writing the exact output, explain what this does:

df["Stock"]
Part C – .loc
Q8

What does this return?

df.loc[2]

Describe it in words.

Q9

What value is returned?

df.loc[4, "Brand"]
Q10

What value is returned?

df.loc[0, "Price"]
Part D – .iloc

Remember the column positions:

Position	Column
0	Product
1	Brand
2	Price
3	Stock
Q11

What does this return?

df.iloc[3]
Q12

What value is returned?

df.iloc[1, 0]
Q13

What value is returned?

df.iloc[4, 2]
Part E – Thinking Like a Pandas User

Now imagine we run:

df = df.set_index("Product")

The DataFrame becomes:

Index	Brand	Price	Stock
Laptop	Dell	950	12
Mouse	Logitech	25	150
Keyboard	HP	45	80
Monitor	Samsung	300	30
Printer	Canon	180	20
Q14

Which command correctly returns the Printer row?

df.loc["Printer"]

or

df.loc[4]

Explain why.

"""
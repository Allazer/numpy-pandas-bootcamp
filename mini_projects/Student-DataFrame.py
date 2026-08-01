import pandas as pd

students = {
    "Name": ["Alice", "Bob", "Carol", "David"],
    "Age": [20, 22, 21, 23],
    "Grade": [85, 91, 88, 95],
    "City": ["Nairobi", "Mombasa", "Kisumu", "Nakuru"]
}

df = pd.DataFrame(students)

print(df)
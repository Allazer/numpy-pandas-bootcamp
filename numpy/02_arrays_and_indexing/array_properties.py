import numpy as np

students = np.array([
    [80, 75, 90],
    [65, 88, 92],
    [78, 81, 84]
])

print("Array:")
print(students)

print("\nDimensions:", students.ndim)
print("Shape:", students.shape)
print("Size:", students.size)
print("Data Type:", students.dtype)



# 4 students x 5 subjects (e.g., scores out of 100)
scores = np.array([
    [85, 90, 78, 92, 88],   # Student 1
    [70, 65, 80, 75, 60],   # Student 2
    [95, 88, 92, 85, 90],   # Student 3
    [60, 72, 68, 75, 70]    # Student 4
])

print("Array:\n", scores)
print("\n1. Shape:", scores.shape)
print("2. Dimensions:", scores.ndim)
print("3. Number of elements:", scores.size)
print("4. Data type:", scores.dtype)



"""
3D array
Creating a simple example with 2 classes,
each containing 2 students, each student having 3 marks.
"""

school = np.array([
    [
        [23,54,16],
        [11,33,22]
    ],
    [
        [2,3,6],
        [0,9,2]
    ]
]
    )
print(school)
print("Size:",school.size)
print("Shape:",school.shape)
print("Dimensions:", school.ndim)
print("Data Type:", school.dtype)
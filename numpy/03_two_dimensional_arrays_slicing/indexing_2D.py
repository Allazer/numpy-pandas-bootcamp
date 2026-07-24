import numpy as np

marks = np.array([
    [80, 75, 90],
    [65, 88, 92],
    [78, 81, 84]
])

print("Whole array")
print(marks)

print("\nFirst row:")
print(marks[0])

print("\nSecond row:")
print(marks[1])

print("\nFirst column:")
print(marks[:,0])

print("\nSecond column:")
print(marks[:,1])

print("\nElement at row 2 column 2:")
print(marks[2,2])

print("\nFirst two rows:")
print(marks[:2])

print("\nFirst two columns:")
print(marks[:,:2])

print("\nLast two rows, first two columns:")
print(marks[1:,:2])
import numpy as np
marks = np.array([
    [78, 85, 90, 88],
    [65, 70, 72, 68],
    [90, 92, 94, 96],
    [55, 60, 58, 62],
    [80, 79, 83, 81]
])

#Each row is a student
#columns - Maths, English , Science, History

"""
Part A — Basic Indexing
Display Student 3's marks.
Display all marks for the Science subject.
Display Student 2's English mark.

"""

#1. Display Student 3's marks
print(marks[2])

#2. Display all marks for the Science subject.
print(marks[: , 2])

#3. Display Student 2's English mark.
print(marks[1,1])


"""
Part B — Calculations
Find the total marks for each student.
Find the average mark for each student.
Find the highest mark in the whole class.
Find the lowest mark in the whole class

"""

#4. Find the total marks for each student.
totals = marks.sum(axis=1)
print(totals)

#5. Find the average mark for each student.
avg_student = marks.mean(axis=1)
print(avg_student)

#6. Find the highest mark in the whole class.
print(marks.max())

#7. Find the lowest mark in the whole class
print(marks.min())


"""
Part C — Challenge
Which student scored the highest total marks?
Which subject has the highest average score?
Display only the students whose average mark is 80 or above.

"""

#8. Which student scored the highest total marks?
print(totals.argmax())

#9. Which subject has the highest average score?
avg = marks.mean(axis=0)
print(avg.argmax())

#10 Display only the students whose average mark is 80 or above.
print(marks[avg_student >= 80])

#11. Without using loops
# Add 5 bonus marks to every student's Science score.
totals+=5
print(totals)
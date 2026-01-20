# loop_tasks.py
# This program demonstrates different loop tasks in Python.

# ---------------------------
# Task 2: Print numbers 1-100 using for loop
# ---------------------------
print("Task 2: Numbers 1 to 100")
for i in range(1, 101):
    print(i, end=" ")
print("\n")

# ---------------------------
# Task 3: Countdown timer using while loop
# ---------------------------
print("Task 3: Countdown Timer")
count = 10
while count >= 0:
    print(count, end=" ")
    count -= 1
print("\n")

# ---------------------------
# Task 4: Demonstrate break and continue
# ---------------------------
print("Task 4: Break and Continue")
for i in range(1, 11):
    if i == 5:
        continue  # skip 5
    if i == 9:
        break     # stop at 9
    print(i, end=" ")
print("\n")

# ---------------------------
# Task 5: Iterate over string characters
# ---------------------------
print("Task 5: Iterate over String")
text = "Python"
for char in text:
    print(char, end=" ")
print("\n")

# ---------------------------
# Task 6: Multiplication table
# ---------------------------
print("Task 6: Multiplication Table of 5")
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print()

# ---------------------------
# Task 7: Range with steps
# ---------------------------
print("Task 7: Range with Steps (0 to 20, step 2)")
for i in range(0, 21, 2):
    print(i, end=" ")
print("\n")

# ---------------------------
# Task 8: Combine loop with conditions (Even/Odd)
# ---------------------------
print("Task 8: Even and Odd Numbers")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")
print()

# ---------------------------
# Task 9: Real-world examples
# ---------------------------
print("Task 9: Real-world Examples")

# Example 1: Shopping cart
cart = ["Apple", "Banana", "Milk", "Bread"]
for item in cart:
    print("You bought:", item)

print()

# Example 2: Attendance list
students = ["Asha", "Ravi", "Nikhil"]
for student in students:
    print(student, "is present")


📘 Understanding for Loops in Python + Multiplication Table Generator Project
🔁 What is a for loop?
A for loop in Python is used when you want to repeat an action a fixed number of times or loop through a sequence like a list, string, or range of numbers.

🧩 Basic Syntax:
python
Copy
Edit
for variable in sequence:
    # Code block to execute
📌 Example:
python
Copy
Edit
for i in range(5):
    print(i)
📤 Output:

Copy
Edit
0
1
2
3
4
✅ range(5) generates numbers from 0 to 4.

🛠 Project: Multiplication Table Generator
This simple Python project uses a for loop to generate the multiplication table of a number entered by the user.

📂 File: multiplication_table.py
python
Copy
Edit
# Ask user for a number
num = int(input("Enter a number to generate its multiplication table: "))

# Print the multiplication table from 1 to 10
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
🧪 Sample Output:
css
Copy
Edit
Enter a number to generate its multiplication table: 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
...
7 x 10 = 70
🎯 Learning Goals:
Understand how a for loop iterates through a range

Learn to use user input with int(input())

Practice f-string formatting for clean output

🚀 Try It Yourself:
Change the loop to print up to 20 instead of 10

Add a delay using time.sleep() for each line (requires import time)

Let the user choose the range (e.g., 1 to N)


# 🛒 Basic Shopping Cart (Python CLI)

A simple Python-based command-line shopping cart program built by **Areeb**. This script allows users to add items with their prices to a virtual cart and displays the total bill once they’re done shopping.

## 📋 Features

- Add any number of items with prices
- View all items in your cart
- Get the total price at the end
- Quit anytime using `q`

## 🧠 How It Works

1. The user is prompted to enter the name of an item.
2. Then, they input the price of that item.
3. This process continues until the user enters `'q'`.
4. Once finished, the script:
   - Displays all items and prices
   - Calculates and prints the total cost

## 📂 Sample Run

```bash
Enter item you want to buy (or 'q' to quit): Apple
Enter price of Apple: $2
Enter item you want to buy (or 'q' to quit): Banana
Enter price of Banana: $3
Enter item you want to buy (or 'q' to quit): q

------ Your Cart ------
Apple - $2.00
Banana - $3.00

Your Total Is: $5.00

#Basic shopping cart by Areeb
foods = []
prices = []
total = 0

while True:
    food = input("Enter item u wanna buy: ")
    if food.lower() == "q":
        break 
    else: 
        price = float(input(f"Enter Price of {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("------Your Cart------")
for food in foods:
 print(food)
for price in prices:
 total += price 
#print() for empty line if needed
print(f"Your Total Is: ${total}")
print("-----Cart By Areeb ;)----- ")
 

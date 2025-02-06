# Write your solution here

no_of_items = int(input("How many items:"))

cur_item = 1
items = []
while cur_item <= no_of_items:
  given_item = int(input(f"Item {cur_item}: "))
  items.append(given_item)
  cur_item += 1
print(items)
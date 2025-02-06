# Write your solution here

original_list = []

while True:
  given_item = int(input("New item: "))

  if given_item == 0:
    break

  original_list.append(given_item)
  sorted_list = sorted(original_list)

  print(f"The list now: {original_list}")
  print(f"The list in order: {sorted_list}")

print("Bye!")

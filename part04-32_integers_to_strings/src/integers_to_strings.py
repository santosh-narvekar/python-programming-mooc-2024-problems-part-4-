# Write your solution here
def formatted(floating_numbers_list):
  new_list = []
  index = 0

  while index < len(floating_numbers_list):
    new_list.append(f"{floating_numbers_list[index]:.2f}")
    index += 1
  
  return new_list

if __name__ == "__main__":
  my_list = [1.234, 0.3333, 0.11111, 3.446]
  new_list = formatted(my_list)
  print(new_list)

# Write your solution here
def distinct_numbers(integer_list: list):
  new_list = []

  for number in integer_list:
    if( number  not in new_list ):
      new_list.append(number)
  
  return sorted(new_list)

if __name__ == "__main__":
  my_list = [3, 2, 2, 1, 3, 3, 1]
  print(distinct_numbers(my_list))

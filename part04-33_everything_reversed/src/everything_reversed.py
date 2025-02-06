# Write your solution here
def everything_reversed(string_list):
  new_list = []

  for string in string_list[::-1]:
    new_list.append(string[::-1])
  
  return new_list


if __name__ == "__main__":
  my_list = ["Hi", "there", "example", "one more"]
  new_list = everything_reversed(my_list)
  print(new_list)
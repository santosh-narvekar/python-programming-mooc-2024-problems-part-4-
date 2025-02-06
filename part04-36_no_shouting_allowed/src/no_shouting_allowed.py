# Write your solution here

def no_shouting(string_list:str):
  new_string = []

  for string in string_list:
    if string.isupper() == False :
      new_string.append(string)

  return new_string

if __name__ == "__main__":
  my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
  pruned_list = no_shouting(my_list)
  print(pruned_list)

    

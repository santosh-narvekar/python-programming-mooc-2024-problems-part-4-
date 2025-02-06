# Write your solution here

def all_the_longest(string_list: list):
  longest_length = len(string_list[0])
  new_string = []
  for string in string_list:
    if ( len(string) > longest_length):
      longest_length = len(string)
  
  for string in string_list:
    if ( len(string) == longest_length ):
      new_string.append(string)
  return new_string
  

if __name__ == "__main__":
  my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
  result = all_the_longest(my_list)
  print(result) # ['eleventh']
# Write your solution here
def shortest(string_list: list):
  shortest_length_string = string_list[0]
  
  for string in string_list:
    if ( len(string) < len(shortest_length_string) ):
      shortest_length_string = string

  return shortest_length_string

if __name__ == "__main__":
  my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
  result = shortest(my_list)
  print(result)
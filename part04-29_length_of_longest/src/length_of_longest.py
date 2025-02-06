# Write your solution here
def length_of_longest(string_list: list):
  longest_length =  len(string_list[0]) #5

  for string in string_list:
    if ( len(string) > longest_length ):
      longest_length = len(string) #8

  return longest_length

if __name__ == "__main__": 
  my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
  result = length_of_longest(my_list)
  print(result)

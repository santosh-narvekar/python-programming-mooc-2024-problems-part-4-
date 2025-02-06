# Write your solution here
def most_common_character(input_string: str):
  most_count_char = input_string[0] 
  default_count = input_string.count(input_string[0])
 
  for char in input_string:
    if ( input_string.count(char) > default_count ):
      most_count_char = char
      break
   
  return most_count_char

if __name__ == "__main__":
  first_string = "abcdbde"
  print(most_common_character(first_string))

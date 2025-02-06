# Write your solution here
def no_vowels(input_string: str):
  new_string = ""

  for char in input_string:
    if ( char != "a" and char != "e" and char != "i" and char != "o" and char != "u" ):
      new_string += char
 
  return new_string

if __name__ == "__main__":
  my_string = "this is an example"
  print(no_vowels(my_string))
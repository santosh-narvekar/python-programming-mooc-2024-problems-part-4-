# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(input: str):
  if(input == input[::-1]): return True
  return False

while True:
  user_input = input("Please type in a palindrome:")
  
  is_Palindrome = palindromes(user_input)

  if(is_Palindrome): 
    print(f"{user_input} is a palindrome!")
    break

  print("that wasn't a palindrome")
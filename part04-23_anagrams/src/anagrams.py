# Write your solution here
def anagrams(string_1:str,string_2:str):
  sorted_string_1 = sorted(string_1)
  sorted_string_2 = sorted(string_2)

  if(sorted_string_1 == sorted_string_2): return True
  return False

if __name__ == "__main__":
  print(anagrams("python", "java"))
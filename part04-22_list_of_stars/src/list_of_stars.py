# Write your solution here

def list_of_stars(list: list):
  index = 0
  while index < len(list):
    print("*" * list[index])
    index += 1

if __name__ == "__main__":
  list_of_stars([3, 7, 1, 1, 2])
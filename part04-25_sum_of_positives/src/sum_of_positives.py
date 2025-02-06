# Write your solution here
def sum_of_positives(number_list: list):
  sum = 0
  for number in number_list:
    if(number >= 0): sum += number
  return sum

if __name__ == "__main__":
  print(sum_of_positives( [1, -2, 3, -4, 5]))
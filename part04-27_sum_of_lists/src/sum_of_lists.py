# Write your solution here
def list_sum(list_1 : list, list_2:list):
  new_list = []
  index = 0
  
  for value in range(index,len(list_1)):
    value = list_1[index] + list_2[index]
    index += 1
    new_list.append(value)

  return new_list

if __name__ == "__main__":
  a = [1, 2, 3]   
  b = [7, 8, 9]
  print(list_sum(a, b)) 
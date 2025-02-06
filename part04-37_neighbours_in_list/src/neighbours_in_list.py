# Write your solution here
def longest_series_of_neighbours(list: list):

  longest_length_of_neighbours = 0
  index = 0
  temp = 1
  while index < len(list): 
    if ( ( list[index] - list[index + 1] ) ** 2 == 1 ):
      temp += 1 
    else:
      temp = 1 
    
    if( temp >= longest_length_of_neighbours ):
      longest_length_of_neighbours = temp 

    index += 1  
    if( index + 1 == len(list)): break  

  return longest_length_of_neighbours
    
if __name__ == "__main__":
  my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
  print(longest_series_of_neighbours(my_list))


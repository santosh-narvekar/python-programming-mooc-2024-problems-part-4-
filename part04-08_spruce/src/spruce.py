# Write your solution here
# You can test your function by calling it within the following block
def spruce(size):
    print("a spruce!")
    cur_row = 0
    while cur_row <= size:
        if(cur_row == size): 
            print(" " * (cur_row - 1),end="")
            print( "*" * 1)
            break
       
        # 5 - 1 = 4 5 - 2 = 3 3 - 3 = 0
        print(" " * ( (size - cur_row) - 1 ) , end="")
        print("*" * (( cur_row + 1 ) + cur_row))
        
        cur_row += 1


if __name__ == "__main__":
    spruce(5)
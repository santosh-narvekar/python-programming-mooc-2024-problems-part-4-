# Copy here code of line function from previous exercise
def line(integer,string):
    if(string == ""):
        string = "*"
    
    print(string[0] * integer)

def triangle(size):
    # You should call function line here with proper parameters
    cur_height = 1
    while cur_height <= size:
        line(cur_height,"#")
        cur_height += 1 
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(3)

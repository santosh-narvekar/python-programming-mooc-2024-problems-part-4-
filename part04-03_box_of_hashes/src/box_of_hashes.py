# Copy here code of line function from previous exercise

def line(integer,string):
    if(string == ""):
        string = "*"
    
    print(string[0] * integer)

def box_of_hashes(height):
    # You should call function line here with proper parameters
    current_height = 1 
    while current_height <= height:
        line(10, "#")
        current_height += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)

# Copy here code of line function from previous exercise
def line(integer,string):
    if(string == ""):
        string = "*"
    
    print(string[0] * integer)

def square(size, character):
    # You should call function line here with proper parameters
    length = 1
    while length <= size:    
        line(size, character)
        length += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")
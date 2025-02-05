# Write your solution here
# You can test your function by calling it within the following block
def line(integer,string):
    if(string == ""):
        string = "*"
    
    print(string[0] * integer)

if __name__ == "__main__":
    line(10, "LOL")
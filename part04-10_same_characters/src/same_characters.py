# Write your solution here
# You can test your function by calling it within the following block
def same_chars(profession,index1,index2):
    if ( index1 >= len(profession) or index2 >= len(profession)):
        return False
    
    if ( profession[index1] == profession[index2] ):
        return True
    
    return False

if __name__ == "__main__":
    print(same_chars("programmer", 0, 12))
# Write your solution here
# You can test your function by calling it within the following block
def range_of_list(list: list):
    return max(list) - min(list)
if __name__ == "__main__":
    my_list = [1,2,3,4,5]
    result = range_of_list(my_list)
    print(result)
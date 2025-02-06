# Write your solution here
# You can test your function by calling it within the following block

def mean(list: list):
    index = 0
    sum = 0
    while index < len(list):
        sum += list[index]
        index += 1
    return sum / len(list)
if __name__ == "__main__":
    my_list = [1,2,3,4,5]
    result = mean(my_list)
    print(result)
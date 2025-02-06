# Write your solution here
# You can test your function by calling it within the following block


def first_word(string):
    word = ""
    index = 0
    while string[index] != " ":
        word += string[index]
        index += 1
    return word

def second_word(string):
    word = first_word(string)
    string = string[len(word) + 1:]
    index = 0

    word = ""
    while string[index] != " ":
        word += string[index]
        index += 1
        if(index >= len(string)): break
    return word

def last_word(string):
    index = -1
    word = ""
    while string[index] != " ":
        word += string[index]
        index -= 1
    return word[::-1]

if __name__ == "__main__":
    sentence = "it was"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
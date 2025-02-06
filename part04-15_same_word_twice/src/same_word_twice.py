# Write your solution here

words = []
attempt = 0

while True:
  word = input("Word:")

  if(word in words):
    break

  attempt += 1  
  words.append(word)

print(f"You typed in {attempt} different words")


# Write your solution here
values = []
count = 0

while True:
  print(f"The list is now {values}") # [1,2]
  opr = input("a(d)d, (r)emove or e(x)it:")
  # d d d r d
  if(opr == "x"): #false false faalse
    break

  if(opr == "d"):
    count += 1 # 3
    values.append(count) #[1,2,3]
  
  if( opr == "r" ):
    if(len(values) > 0):
      values.pop(-1) # [1,2]
      count -= 1 # 2
  
  
print("Bye!")
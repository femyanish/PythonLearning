# excercise for looping compile

my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0

for item in my_list:
  counter= counter +item

print(counter)

#range

for _ in range(1,10):
  print(_)

for i in range(1,10,2):
  print (i)

for i in range( 10,1,-1):
  print(i)

for i in range(2):
  print(list(range(1,10)))

# enumerate

for i,num in enumerate(list(range(1,100))):
  if(num == 50):
    print ('The index of 50 is' ,i)


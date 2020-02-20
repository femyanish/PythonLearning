# while loop
#else used only if no break statemnt in while

i = 0
while i<50:
  print (i)
  i=i+1
else:
  print("my work is done")

# use while when you are not sure how many iterations needed otherwise use for loop since its simpler:

while True:
  console = input("say something: ")
  if console == 'bye':
    break

# break,continue and pass can be used in both while and for loops
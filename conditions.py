# learning conditions

user_name = ""
password =""

if user_name and password:
  print("You are able to login")
elif user_name:
  print("Add your password")
else:
  print("add your username and password")

# ternary operators
can_login = "You are able to login" if user_name and password else "add your username and password"

#coding Time

is_magician = True
is_expert = True

if is_magician and is_expert:
  print("You are a master magician")
elif is_magician and not is_expert:
  print("atleast you are getting there")
elif not is_magician:
  print("you need magical powers")






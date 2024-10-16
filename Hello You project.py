name= input("What is your name?:")
age= int(input("What is your age?:"))
live= input("Where do you live?:")
love= input("What do you love to do?:")

string= "Your name is {}, you are {} years old. You live in {} and you love to do {}"
output= string.format(name, age, live, love)

print(output)

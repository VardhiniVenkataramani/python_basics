known_users=["Alice","Bob", "Claire", "Dan", "Emma","Fred","Georgie","Harry"]
print(len(known_users))

while True:
    print("Hi I'm Travis")
    name= input("What is your name?:").strip()

    if name in known_users:
        print("Hello{}!".format(name))
        remove= input("Would you like to delete your name(y/n)?:")

        if remove=="y":
            known_users.remove(name)
            print(known_users)
    else:
        print("name is NOT recognised")
        print(known_users)
        add_me=input("Would you like to be aded to the list?(y/n):")
        if add_me=="y":
            known_users.append(name)
            print(known_users)

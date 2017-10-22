known_users = ['Alice', 'Bob', 'Claire', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry']

while True:
    print('Hi! My name is Mike and I am the SECURITY.')
    name = input('What is your name?: ').strip().capitalize()

    if name in known_users:
        print('Hello ' + name + '!')
        remove = input('Would you like to be removed from the system? (y/n) ').strip().lower()
        if remove == 'y':
            known_users.remove(name)
            print('You have been removed ' + name + '.')
        elif remove == 'n':
            print('Okay! You are still on the list!')
    else:
        print("That's odd... You're not on my list " + name + "!")
        new_name = input('Would you like to be added our guest list? (y/n) ').strip().lower()
        if new_name == 'y':
            known_users.append(name)
            print('You have been added ' + name + '!')
        elif new_name == 'n':
            print('Okay. No problem :(')

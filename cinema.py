#list is [age to see film, amt of seats still available]

films = {
    "Titanic": [3,5],
    "Wizard Of Oz": [18,5],
    "Tarzan": [15,5],
    "Big Boy": [12,5]
}

while True:
    choice = input("What film would you like to watch?: ").strip().title()
    if choice in films:
        age = int(input('How old are you?: ').strip()) # checking user age
        if age >= films[choice][0]:
            tickets_avail = films[choice][1]
            if tickets_avail > 0: #checking to see if tickets available
                print('Enjoy the film!')
                films[choice][1] -= 1 #remove ticket from still available
            else:
                print('Sorry, we are out of tickets for that film...')
        else:
            print('You are too young to see that film!')
    else:
        print("We don't have that film...")

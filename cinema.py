#Mini project as if this were a mini cinema with age restrictions and limited seats.
#You can only see a film if you are old enough and there are seats available.


#list elements are [age minimum to see film, amt of seats still available]

films = {
    "Titanic": [18, 5],
    "Wizard Of Oz": [0,5],
    "Tarzan": [13,5],
    "Rocky": [13,5]
}

while True:
    choice = input("What film would you like to watch (Titanic: R, Rocky: R, Tarzan: PG - 13, or Wizard of Oz: G)?: ").strip().title()
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

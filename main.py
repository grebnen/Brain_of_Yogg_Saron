# Justice Kennedy Module 7-3
# A dictionary for brain of Yogg Saron
# The dictionary links a room to other rooms.
import sys

rooms = {
    'Freya\'s sanctuary of life': {'South': 'Chamber of promises'},
    'Chamber of promises': {'North': 'Freya\'s sanctuary of life', 'East': 'Thorim\'s room'},
    'Thorim\'s room': {'South': 'Freya\'s sanctuary of life', 'West': 'Hodir\'s Chamber'},
    'Hodir\'s Chamber': {'West': 'Brain of Yogg Saron'}
}
items = {
    'Freya\'s sanctuary of life': 'Blossom',
    'Chamber of promises': 'Beacon of Communication',
    'Hodir\'s Chamber': 'Ring',
    'Thorim\'s room': 'Thorim\'s hammer',
    'Brain of Yogg Saron': 'Yogg Saron'

}
state = 'Freya\'s sanctuary of life'
inventory = []


# function
def get_new_state(state, direction):
    new_state = state  # declaring
    for i in rooms:  # loop
        if i == state:  # if
            if direction in rooms[i]:  # if
                new_state = rooms[i][direction]  # assigning new_state

    return new_state  # return


while 1:  # gameplay loop
    print('You are in the ', state)  # printing state
    if state == 'Brain of Yogg Saron':
        print('Battling with Yogg Saron', end='')
        for i in range(50):
            for j in range(1000000):
                pass
            print(".", end='', flush=True)
        print()
        if len(inventory) == 4:
            print('You have defeated Yogg Saron - congratulations')
        else:
            print('Yogg Saron has consumed you, - try again')
        break

    print('Available to you in this room is', items[state])
    print('You currently have', inventory)
    direction = input('Enter item you want OR direction to go OR exit to give up: ')  # asking user
    if direction.lower() == items[state].lower():
        if items[state] not in inventory:
            inventory.append(items[state])
        continue
    direction = direction.capitalize()  # making first character capital remaining lower
    if direction == 'Exit':  # if
        sys.exit(0)  # exit function
    if direction == 'East' or direction == 'West' or direction == 'North' or direction == 'South':  # if
        new_state = get_new_state(state, direction)  # calling function
        if new_state == state:  # if
            print('A great evil is in that direction, quickly try another direction!')  # print
        else:
            state = new_state  # changing state value to new_state
    else: #updated the error messaging to be more descriptive
        itemvals = []
        print()
        print('Invalid Input')
        print('Please enter a valid direction: north, south, east, west')
        print('or')
        print('Enter an item to add to your inventory')       

        for k, v in items.items():
            itemvals.append(v)

        print(', '.join(itemvals))
        print()
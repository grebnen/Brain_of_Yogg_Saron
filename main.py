# Justice Kennedy Module 7-3
# A dictionary for brain of Yogg Saron
# The dictionary links a room to other rooms.
import sys

# A dictionary for brain of Yogg Saron
# The dictionary links a room to other rooms.
rooms = {
    'Freyas sanctuary of life': {'South': 'chamber of promises'},
    'chamber of promises': {'North': 'Freyas sanctuary of life', 'East': 'thorims room'},
    'thorims room': {'South': 'Freyas sanctuary of life', 'West': 'hodirs chamber'},
    'hodirs chamber': {'West': 'Brain of Yogg Saron'}
}

items = {
    'Freyas sanctuary of life': 'Blossom',
    'chamber of promises': 'Beacon of Communication',
    'hodirs chamber': 'Ring',
    'thorims room': 'Thorims hammer',
    'Brain of Yogg Saron': 'Yogg Saron'
}

state = 'Freyas sanctuary of life'
inventory = []

def get_new_state(direction, current_room):
    new_room = current_room

    if direction in rooms[current_room]:
        new_room = rooms[current_room][direction]

    return new_room

def show_status():
    print('You are currently in', state)
    print('Available in this room is', items[state])
    print('You currently have', inventory)
    print('You can move to the following rooms:', ', '.join(list(rooms[state].keys())))

while True:
    show_status()

    if state == 'Brain of Yogg Saron':
        print('Battling with Yogg Saron', end='')
        print()
        if len(inventory) == 4:
            print('You have defeated Yogg Saron - congratulations')
        else:
            print('Yogg Saron has consumed you - try again')
        break

    direction = input('Enter item you want OR direction to go OR exit to give up: ')

    if direction.lower() == items[state].lower():
        if items[state] not in inventory:
            inventory.append(items[state])
        continue

    direction = direction.capitalize()

    if direction == 'Exit':
        sys.exit(0)

    if direction in ['East', 'West', 'North', 'South']:
        new_state = get_new_state(direction, state)
        if new_state == state:
            print('A great evil is in that direction, quickly try another direction!')
        else:
            state = new_state
    else:
        print('Invalid direction!')

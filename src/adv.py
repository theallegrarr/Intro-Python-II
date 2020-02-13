import textwrap
from item import Item
from room import NewRoom
from player import Player
from shutil import get_terminal_size

cols, rows = get_terminal_size()

# Declare all the rooms

item = {
    'gun' : Item('gun', 'A weapon useful against enemeies.'),
    'knife' : Item('knife', 'A weapon useful against enemeies.')
}

room = {
    'outside':  NewRoom("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    NewRoom("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': NewRoom("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   NewRoom("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': NewRoom("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


print(room['outside'].__directions__())

value = """Crilen game, the ultimate mindbending experience"""
  
# Wrap this text. 
wrapper = textwrap.TextWrapper(width=50) 
  
word_list = wrapper.wrap(text=value) 

print("+---------------------------------------------------------+")
# Print each line. 
for element in word_list: 
    print(element) 
print("+---------------------------------------------------------+\n")
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player(input("Your name: "), room['outside'])

room['foyer'].__addItem__(item['gun'])
room['foyer'].__addItem__(item['knife'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
def move(choice):
    """Attempt to move in a cardinal direction or return current room"""
    if choice == 'n':
        movement = player1.room.n_to
    elif choice == 's':
        movement = player1.room.s_to
    elif choice == 'e':
        movement = player1.room.e_to
    elif choice == 'w':
        movement = player1.room.w_to

    if movement == None:
        return player1.room
    else:
        return movement


while True:
    print("\n"*(rows-23), player1.room.name.upper())
    print("\n", player1.room.__directions__(), "\n")
    print(player1.room.description)
    print(player1.room.__getItems__())
    #try:
    choice = input("pick your next room: \n")
    if choice == "q":
        print("quit game!")
        break
    if 'take' in choice or 'get' in choice:
        for x in player1.room.visible_items:
            if choice.split(" ",2)[1] == x.name:
                player1.getItem(x)
                x.on_take()
                player1.room.__dropItem__(x)
    if 'drop' in choice:
        for x in player1.inventory:
            if choice.split(" ",2)[1] == x.name:
                player1.dropItem(x)
                x.on_drop()
                player1.room.__addItem__(x)
    if choice not in ['n', 's', 'e', 'w']:
        if 'take' not in choice and 'get' not in choice and 'drop' not in choice:
            print("pick a valid room name! \n")
            continue
    if choice in ['n', 's', 'e', 'w']:
        movement = move(choice)
        if movement.name == player1.room.name:
            print("Thats your room")
            continue
        else:
            player1.room = movement
    # except:
    #     print(" \n")
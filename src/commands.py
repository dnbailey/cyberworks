from adventurelib import *
from rooms import *
from items import *

#: Movement Commands
#: TODO Change directions to something matching cyberspace
@when('north', direction='north', context='cyber')
@when('south', direction='south', context='cyber')
@when('east', direction='east', context='cyber')
@when('west', direction='west', context='cyber')
def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        current_room = room
        say(f'You go {direction}.')
        look()
    else:
        say("You can't go that way.")

#: Print the current_room based on context
@when('pwd', context='cyber')
@when('look', context='reality')
def look():
    if get_context() == 'reality':
        print(serverRoom)    
    else:
        print(current_room)

#: Switch to cyberworks context
@when('login', context='reality')
def login():
    set_context('cyber')
    say('Welcome to Cyberworks...')
    look()

#: Switch to reality context
@when('logout', context='cyber')
def logout():
    set_context('reality')
    say('Exiting Cyberworks...')
    look()

#: Read mission assignment
@when('read mission', context='reality')
def readMission():
    say("""
    TECK AGENT 02485

    ****************

    A hacker has been distroying nodes in Cyberworks. Fragments of these broken nodes are scattered throughout Cyberworks. In order to trace the vector of the attacks, you must gather at least 6 of the fragments and analyze them. You will need to login and explore Cyberworks in order to find the fragments. Then you will need to bring those fragments back to reality and analyze them.

    Good luck, and remember who pays the bills.
    """)

#: Show inventory
@when('inventory')
def showInventory():
    print('You have:')
    if not inventory:
        print('nothing')
        return
    for item in inventory:
        print(f'* {item}')

#: Place item in inventory
@when('take ITEM', context='cyber')
def take(item):
    obj = current_room.items.take(item)
    if not obj:
        print(f'There is no {item} here.')
    else:
        inventory.add(obj)
        print(f'You take the {obj}.')

#: Place item in Server Room
@when('place ITEM', context='reality')
def place(item):
    obj = inventory.take(item)
    if not obj:
        say(f'You do not have a {item}')
    else:
        say(f'You place the {obj}')
        current_room.items.add(obj)

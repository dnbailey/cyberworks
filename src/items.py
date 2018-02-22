from lib.adventurelib import *
from src.rooms import *

#: Configure bags
Room.items = Bag()
inventory = Bag()

#: Items
broom = Item('a broken broom that is a fragment of a destroyed node', 'broom')
node2.items = Bag({broom})

shell = Item('an oddly shaped shell is a fragment of a destroyed node', 'shell')
node3.items = Bag({shell})

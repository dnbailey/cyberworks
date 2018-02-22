from adventurelib import *

#: Rooms
serverRoom = Room("""
You are in the server room. In front of you there is a terminal where you can login to Cyberworks.
""")

node1 =  Room("""
/// Node 1 ///

This node is a blank cube. The four walls are blinding white and seem both far away and eerily close at the same time. 
""")

node2 = Room("""
/// Node 2 ///
This node is decorated like a medieval castle. There is a broom on the floor.
""")

node3 = Room("""
/// Node 3 ///
This node is a sunny, island beach devoid of all signs of life. There is an odd shaped shell to your left.
""")

#: Connections
node1.north = node2
node2.west = node3

#: Initialize the current_room and context
current_room = node1
set_context('reality')

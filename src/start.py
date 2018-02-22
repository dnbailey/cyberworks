from lib.adventurelib import *

#: Title screen
print(
"""\033[31m
  _____     __                           __      
 / ___/_ __/ /  ___ _____    _____  ____/ /__ ___
/ /__/ // / _ \/ -_) __/ |/|/ / _ \/ __/  '_/(_-<
\___/\_, /_.__/\__/_/  |__,__/\___/_/ /_/\_\/___/
    /___/                                        

\033[0m
Created by \033[1mNathan Bailey\033[0m
\033[31mBuild with AdventureLib\033[0m
""")

#: Intro
say("""
The year is 2049. Reality is an unpleasant and dangerous place to live. In the over-crowded, dirty cites, the wealthy and powerful escape harsh reality by logging in to a virtual playground called Cyberworks. Attacks on Cyberworks are common as hackers try to exploit the rich and powerful. The Tecks are tasked with policing Cyberworks. The servers buzz around you. This is one of the many node server farms of Cyberworks. It is also where you work as a Teck. An unopened mission file sits blinking on your mobile... \n
""")

# Kick the game off
start(help=False)

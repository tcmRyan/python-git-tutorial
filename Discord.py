import discord
import asyncio
from enum import Enum

class MyClient(discord.Client):
    
    def __init__(self):
       #this init function is used to initiliaze our global variables

       self.stagelevel = 0
       self.isMadScientist = False
       self.isAbandonedHouse = False
       self.isCaveExperience = False
       self.isSmallKeyPresent = False
       self.isPasscodePresent = False
       self.aquiredMainKey = False
       self.aquiredMap = False
       self.aquiredMoney = False
       self.goToDoorToEscape = False
       self.discoverdSafe = False
       super().__init__()
       
    
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    #@client.event
    async def on_message(self, message):
        async def vibe_check():
            await message.content.send('Vibe Check! Try again next time')
        async def go_back():
            self.stagelevel = 0
        if message.content.startswith('-annoyJoey'):
            Joey = [x for x in message.guild.members if x.id == 206035591027097601][0]
            await Joey.send("weeb")
            await asyncio.sleep(1)
            await Joey.send('( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)')
        
        if message.content.startswith('exit') and self.stagelevel > 0:
            await message.channel.send('Awe, it\'s a shame you can\'t stay. See you next time!')
            self.stagelevel = 0 
            self.isMadScientist = False
            self.isAbandonedHouse = False
            self.isCaveExperience = False
            self.isSmallKeyPresent = False
            self.isPasscodePresent = False
            self.aquiredMainKey = False
            self.aquiredMap = False
            self.aquiredMoney = False
            self.goToDoorToEscape = False
            self.discoverdSafe = False

        if message.content.startswith('home') & self.stagelevel > 0:
            await message.channel.send('What game would you like to play? Mad Scientist lab (msl), Abonded house office (aho), or cave(c)?')
            self.stagelevel = 1 
            self.isMadScientist = False
            self.isAbandonedHouse = False
            self.isCaveExperience = False
            self.isSmallKeyPresent = False
            self.isPasscodePresent = False
            self.aquiredMainKey = False
            self.aquiredMap = False
            self.aquiredMoney = False
            self.goToDoorToEscape = False
            self.discoverdSafe = False    

        if "hi there" in message.content.lower():
            await message.channel.send('hello')
        
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
        
        if message.content.startswith('!bot'):
            await message.channel.send('You Rang?')
        
        if message.content.startswith('$test'):
            await message.channel.send('waiting...')
            await asyncio.sleep(10)
            await message.author.send('( ͡° ͜ʖ ͡°)')
        
        if message.content.startswith('!storytime'):
            await message.channel.send('STORYTIME! I GET KILLED IN A WALMART PARKING LOT')
        
        if message.content.startswith('goBack') and self.isMadScientist == True:
            go_back()
            await message.channel.send('You head back to the main area')
            await asyncio.sleep(1)
            await message.channel.send('You open your eyes, disoriented. Glancing around, you realize something is not right. You are lying in a mad scientist\'s lab! \nClosest to you is his desk (d) and his lab coat (lc).')
            await message.channel.send('Which do you choose to look at first?')
            self.stagelevel = 3

        if message.content.startswith('goBack') and self.isAbandonedHouse == True:
            go_back()
            await message.channel.send('You walk back to the center of the room')
            await asyncio.sleep(1)
            await message.channel.send('Something still doesn\'t feel right...')
            await asyncio.sleep(1)
            await message.channel.send('Would you like to step forward? /nyes(y)/ no(n)')
            self.stagelevel = 2

        if message.content.startswith('goBack') and self.isCaveExperience == True:
            go_back()
            await message.channel.send('STORYTIME! You are in a cave and there just so happens to be a pool of suspicious looking liquid next to you. \n what do you do?')
            await asyncio.sleep(1)

            await message.channel.send('Would you like to check the suspicious liquid? (Y) / (N)')
            self.stagelevel = 2

        if message.content.startswith('-startEscape') and self.stagelevel == 0:
            print(message.author.id)
            await message.channel.send('Welcome to Escape the Room!')
            await message.channel.send('If you want to exit the game, just type \"exit\"')
            await message.channel.send('If you want to go to the scenario select, just type \"home\"')
            await message.channel.send('If you want to go to the main area, just type \"goBack\"')
            await message.channel.send('When you are ready to leave, type in \"door\"')
            await message.channel.send('Choose one of the following scenarios: \n' '-Mad scientist lab (msl) \n' '-Abandoned house office (aho) \n' '-Cave (c)')
            #scenario = input('Mad scientist lab (msl), Abandonded house office (aho), or Cave (c)?')
            self.stagelevel = 1
        
# Mad scientist path --------------------------------------------------------------------------------------------------        

        if message.content.startswith('msl') and self.stagelevel == 1: 
            print(message.author.id)
            await message.channel.send('You are trapped inside a mad scientist\'s basement\. \nOnce you enter \'begin\' \, you will have five minutes to escape. Good luck!')
            self.stagelevel = 2
            self.isMadScientist = True
            print(self.isMadScientist)
                #    print(message.author.id)
                #    await message.channel.send('Your five minutes begins now')
        #first choice ---------------------------------------------------
        if message.content.startswith('begin') and self.stagelevel == 2 and self.isMadScientist == True:
            print(message.author.id)
            await message.channel.send('Five minutes starts now \nYou open your eyes, disoriented. Glancing around, you realize something is not right. You are lying in a mad scientist\'s lab! \nClosest to you is his desk (d) and his lab coat (lc).')
            await message.channel.send('Which do you choose to look at first?')
            self.stagelevel = 3

        #second choice -----------------------------------------------------

        if message.content.startswith('d') and self.stagelevel == 3 and self.isMadScientist == True:
            print(message.author.id)
            await message.channel.send('You take a step closer to the desk. Do you look under the papers on the desk (p) or through the drawers (dr)')
            self.stagelevel = 4

        if message.content.startswith('lc') and self.stagelevel == 3 and self.isMadScientist == True or message.content.startswith('lc')  and self.stagelevel == 5 and self.isMadScientist == True:
            print(message.author.id)
            await message.channel.send('You take a step closer to the lab coat. You see a suspicious lump in the pockets. Looking through it, you find a diary (di) and a key (k), or you can go back to the previous stage (goBack). Which do you choose?')
            self.stagelevel = 4


        # third choice ----------------------------------------------------------

        if message.content.startswith('p') and self.stagelevel == 4 and self.isMadScientist == True:
            print(message.author.id)
            await message.channel.send('You ruffle through the papers on his desk, but find nothing of use. Do you search the drawers (dr), move on to his cabinet (c), or you can go back to the previous stage (goBackDesk)')
            self.stagelevel = 5

        if message.content.startswith('dr') and self.stagelevel == 4 and self.isMadScientist == True or message.content.startswith('dr') and self.stagelevel == 5 and self.isMadScientist == True:
            print(message.author.id)
            await message.channel.send('You search through his drawers, coming across a small box that appears to be a safe. However, you are lacking the key. Do you choose to move onto his cabinet (c) or go back and search his lab coat (lc), or you can go back to the previous stage (goBackDesk)')
            self.stagelevel = 5
       
        if message.content.startswith('di') and self.stagelevel == 4 and self.isMadScientist == True:
            print(message.author.id)
            await message.channel.send('You flip through the diary, finding a strip of paper with a combination of numbers. Not sure what it\'s for, you pocket it for later. Now, you move onto the key. Enter (k) to examine it.')
            self.stagelevel = 5

        if message.content.startswith('k') and self.stagelevel == 4 and self.isMadScientist == True or message.content.startswith('k') and self.stagelevel == 5 and self.isMadScientist == True:
            print(message.author.id)
            await message.channel.send('You pick up the key! Do you decide the test the lock on the door (t), or pocket the key for now (po)?')
            self.stagelevel = 5
        
# Abandoned office path --------------------------------------------------------------------------------------------------

        if message.content.startswith('aho') and self.stagelevel == 1:
            await message.channel.send('You wake up, light streaming in from a crack in the shutters. \n The house around is silent, it\'s mysteries hidden from you. ')
            await asyncio.sleep(1)
            await message.channel.send('You look around you, and you notice a door behind you. However, there is a big lock on the inside')
            await message.channel.send('Something doesn\'t feel right...')
            await asyncio.sleep(1)
            await message.channel.send('You do not know where you are.')
            await message.channel.send('You do not have any money') 
            await message.channel.send('You are not in position of the key for the lock.')
            await message.channel.send('As much as you want to stay, the vibes of this play are abysmal. You need to get out')
            await message.channel.send('Would you like to step forward? \nyes(y) or no(n)')
            self.stagelevel = 2
            self.isAbandonedHouse = True
        
        # breakdown of level 2 choices --------------------------------------------------------------
        if message.content.startswith('y') and self.stagelevel == 2 and self.isAbandonedHouse == True:
            await message.channel.send('You step forward, moving to the desk. You like down.')
            await message.channel.send('There is a computer, with a usb stick in one of it\'s ports. A sticky note near the mouspad has a password on it.')
            await message.channel.send('The computer turns on when you move closer, and you are logged into an account- Lohn Jenon')
            await asyncio.sleep(1)
            await message.channel.send('You see a folder on the desktop for the usb, and some browser is open on the computer')
            await message.channel.send('Would you like to investigate the usb folder (usbF), or the browser links (brL)?')
            self.stagelevel = 3
            self.isAbandonedHouse = True

        if message.content.startswith('n') and self.stagelevel == 2 and self.isAbandonedHouse == True:
            await message.channel.send('You look around. You are near a bed, which has a navy blue bed cover')
            await asyncio.sleep(1)
            await message.channel.send('A pillow is propped up at the top of the bed at an awkward angle.')
            await message.channel.send('It looks like there is somethething there...')
            await asyncio.sleep(1)
            await message.channel.send('On the blanket, there is a binder, which seems full of important document')
            await asyncio.sleep(1)
            await message.channel.send('What would you like to examine? \nPillow (pi) or Binder (bi)?')
            self.stagelevel = 3
            self.isAbandonedHouse = True

        # breakdown of level 3 choices --------------------------------------------------------------
                
        if message.content.startswith('pi') and self.stagelevel == 3 and self.isAbandonedHouse == True:
            await message.channel.send('You head over to the pillow. You pat it; something is below it')
            await asyncio.sleep(1)
            await message.channel.send('You lift the pillow up. Undearneath is a... small key!')
            await message.channel.send('Excitedly, you turn to face the door. Sadly, the key looks too small to be for the lock')
            await asyncio.sleep(1)
            await message.channel.send('It might open something else though...')
            self.isSmallKeyPresent = True
            await message.channel.send('You should go back now')

        if message.content.startswith('bi') and self.stagelevel == 3 and self.isAbandonedHouse == True:
            await message.channel.send('You pick up the binder. It is very heavy with all the documents inside. You flip to the first page:')
            await asyncio.sleep(1)   
            await message.channel.send('It seems to be some kind of tax form. Boring stuff, really')
            await message.channel.send('Next to the bed, you notice a big box...')
            await asyncio.sleep(1)
            await message.channel.send('Do you want to investigate? \nyes(y) or no(n).')
            self.stagelevel = 4

        if message.content.startswith('usbF') and self.stagelevel == 3 and self.isAbandonedHouse == True:
            await message.channel.send('You click on the folder, and some files pop up. There are some typical files, essays, bills, those kinds of things.')
            await asyncio.sleep(1) 
            await message.channel.send('Suddenly, you notice something. A file that looks like... a map!')
            await message.channel.send('You open it up, and sure enough, it\'s a map, of the surrounding area, and then some!')
            await message.channel.send('You go to print this map, and a minute later, you take it out of the printer near the computer')
            self.aquiredMap = True
            await asyncio.sleep(1)
            await message.channel.send('As you take a quick look around the desk, you notice a small safe, tucked away in the corner of the desk')
            await message.channel.send('Do you want to investigate or leave? \n(inv) or (lve)')
            self.stagelevel = 4   

        if message.content.startswith('brL') and self.stagelevel == 3 and self.isAbandonedHouse == True:
            await message.channel.send('The browser opens up, into seems to be some old web broswer. In it, a link is opened.')
            await asyncio.sleep(1)
            await message.channel.send('It seems to some regular website, like youtube.')
            await message.channel.send('You play around with it for a few minutes, watching a short video.')
            await message.channel.send('You should go back now')
        
        # breakdown of level 4 choices --------------------------------------------------------------

        if message.content.startswith('y') and self.stagelevel == 4 and self.isAbandonedHouse == True:
            await message.channel.send('You get closer to the box. You notice that it\'s big, is made of goldenrod colored reeds, and is closed shut with a small lock.')
            await asyncio.sleep(1)
            await message.channel.send('You feel a wierd cumpulsion to try and open the box')
            await message.channel.send('Do you want to try and open the box? \n(open) or (lve)')
            self.stagelevel = 5

        if message.content.startswith('n') and self.stagelevel == 4 and self.isAbandonedHouse == True:
            await message.channel.send('You decide not to investigat the box. You decide to head back')
            await asyncio.sleep()
            go_back()
            await message.channel.send('You walk back to the center of the room')
            await asyncio.sleep(1)
            await message.channel.send('Something still doesn\'t feel right...')
            await asyncio.sleep(1)
            await message.channel.send('Would you like to step forward? \n(y) or (n)')
            self.stagelevel = 2
        
        if message.content.startswith('inv') and self.stagelevel == 4 and self.isAbandonedHouse == True:
            await message.channel.send('You inspect the safe. It is fairly small, made of a hard silver material. \nIt has a passcode entry system on the front')
            await asyncio.sleep(1)
            await message.channel.send('\"Do you have the passcode?\" You wonder to yourself.')
            await message.channel.send('Do you want to try and open the safe? \nyes(y) or no(n)')
            self.stagelevel = 5

        if message.content.startswith('leave') and self.stagelevel == 4 and self.isAbandonedHouse == True:
            await message.channel.send('You decide to not investigate the safe. You think that you sould head back')
            await asyncio.sleep(1)
            go_back()
            await message.channel.send('You walk back to the center of the room')
            await asyncio.sleep(1)
            await message.channel.send('Something still doesn\'t feel right...')
            await asyncio.sleep(1)
            await message.channel.send('Would you like to step forward? \n(y)/ (n)')
            self.stagelevel = 2 
        
        
        
        # breakdown of level 5 path ----------------------------------------------------------

        #try and open the safe 
        if message.channel.send('y') and self.stagelevel == 5 and self.isAbandonedHouse == True and self.isSmallKeyPresent == True:
            await message.channel.send('You try putting in the key into the small lock on the box...')
            await asyncio.sleep(1)
            self.aquiredMainKey = True
            self.isPasscodePresent = True
            await message.channel.send('Success! To box creaks open. Inside is a big key, and a piece of paper with some password on it.')
            await message.channel.send('You reach in and take both. You look at the key... it looks like it\'s good for the door!')
            await 


        #try and open the box

        #try and 


        if message.content.startswith('goto') and self.stagelevel == 5 and self.isAbandonedHouse == True and self.discoverdSafe == True:
            await message.channel.send('You go back to the safe. You hold up the sheet with the pascode to your face')
            await asyncio.sleep(1)
            await message.channel.send('You plug in the code to keypad. You hear a soft ding...')
            await asyncio.sleep(1)
            self.aquiredMoney = True
            await message.channel.send('Sucess! The safe opens, and you find a generous stack of dolar bills. You reach in and take it')
            await message.channel.send('You should go back now')


# Cave escape path --------------------------------------------------------------------------------------------------

        if message.content.startswith('c') and self.stagelevel == 1:
            await message.channel.send('STORYTIME! You are in a cave and there just so happens to be a pool of suspicious looking liquid next to you. \n what do you do?')
            await asyncio.sleep(1)

            await message.channel.send('Would you like to check the suspicious liquid? (Y) / (N)')
            self.stagelevel = 2
            self.isCaveExperience = True
        # breakdown of level 2 choices -------------------------------------------------------------
        if message.content.startswith('Y') and self.stagelevel == 2 and self.isCaveExperience == True:
            await message.channel.send('the liquid smells like stalactite and tastes like eel. How delicious.')

            self.stagelevel = 3
        
        if message.content.startswith('N') and self.stagelevel == 2 and self.isCaveExperience == True:
            await message.channel.send('You are a plebian. You made a mistake. You go for the liquid anyways and now it tastes like drywall. A disappointing discovery.')
            await asyncio.sleep(1)

            await message.channel.send('The aftertaste of the liquid has left you in w e i r d vibe time. In your vision there is a circle-shaped object, a triangle-shaped object and a square-shaped object.')
            await asyncio.sleep(1)
            await message.channel.send('Do you reach for the shady circle-object (circ), the shadier triangle-shaped object (trig) or the even shadier square-shaped object (sqr)? ')              
            self.stagelevel = 3

        # breakdown of level 3 choices
          
        if message.content.startswith('circ') and self.stagelevel == 3:
            await message.channel.send('Whoa it is a coiled python, that is pretty cool. It kills you though.')
         
        if message.content.startswith('trig') and self.stagelevel == 3: 
            await message.channel.send('Mmmm it is a delicious stalactite. Possibly the one you consumed part of earlier. You eat a chunk off of it. It reveals a thread.')

        if message.content.startswith('sqr') and self.stagelevel == 3:
            await message.channel.send('S Q U A R E S Q U A R E S Q U A R E S Q U A R E S Q U A R E you eat two dice.')
            
        # breakdown of level  4 choices

        
        
        # return the user to a "home state"- let them try again, or to a check point
    '''async def test_timer():
        if timerTest == True:
            timer = True
        if timerTest == False:
            timer = False
            


    async def set_timerFalse():
        timerTest = False
    async def set_timerTrue():
        timerTest = True'''

#client.wait_for('message', check=check_msg, timeout=300)

client = MyClient()
client.run('NjM3NzUwMjY0NjE0MzU0OTgy.XbStSA.ZrPt1EMZAFQOVrOEvW9_JmzXtEc')
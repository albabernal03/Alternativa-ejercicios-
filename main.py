Phase3FinalWendyHp = 100
Phase2FinalWendyHp = 75
FinalWendyHp = 50
WendyHp = 30
YourHp = 10
TheirHp = 15
damage = 0
damaged = 0
Burn = 0
Burned = 0
SFB = False
SFB2 = False
MoreAttack = 0
MoreHp = 0
MoreDefence = 0
Healed = 0
Upgrade1 = False
Upgrade2 = False
Upgrade3 = False
M = False
Off = False
Answer3 = ""
WendyDefend = 0

#imports
import sys
import replit
import time
import random

#colors
Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m" 
black = "\033[0;30m"
black = "\033[0;90m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
white = "\033[0;97m"
cyan_back="\033[0;46m"
pink_back="\033[0;45m"
white_back="\033[0;47m"
blue_back="\033[0;44m"
orange_back="\033[0;43m"
green_back="\033[0;42m"
red_back="\033[0;41m"
grey_back="\033[0;40m"
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
reset = "\033[0m"

def HerTurn4():
        global damage
        global damaged
        global YourHp
        global Phase3FinalWendyHp
        global Burn
        global Burned
        global Attacked
        global SFB2
        global Healed
        global WendyDefend     
        global damage
        global damaged
        global MoreAttack
        global MoreHp
        global MoreDefence
        global Healed
        replit.clear()
        Turn = random.randint(1, 6)
        if Turn == 5:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Attacked = random.randint(10, 14)
                Attacked = Attacked - damaged + Burned
                Attacked = Attacked - MoreDefence
                if Attacked < 1:
                        Attacked = random.randint(1, 5)
                print(Red+"Wendy did a MORTAL "+(str(Attacked))+" damage."+reset)
                YourHp = YourHp - Attacked
                time.sleep(1)
                replit.clear()
                if YourHp <= 0:
                        Sleep()
                        print(Red+"You lost and were annihilated by Wendy."+reset) 
                        time.sleep(1)
                        YourHp = 10 + MoreHp
                        Phase3FinalWendyHp = 100
                        damage = 1
                        damaged = 0             
                        restart()     
                else:
                        FinalFight3()
        if Turn == 4:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                WendyDefend = random.randint(5, 7)
                print("Wendy defended herself!")
                time.sleep(1)
                replit.clear()
                FinalFight3()
        if Turn == 3:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Burned = random.randint(5, 7)
                print("Wendy "+Red+"ROASTED"+reset+" you, her attack damage increased!")
                time.sleep(1)
                replit.clear()
                FinalFight3()
        if Turn == 2:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Healed = random.randint(5, 7)
                print("Wendy healed herself with a hamburger!")
                Phase3FinalWendyHp += Healed
                time.sleep(1)
                replit.clear()
                FinalFight3()
        else:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Attacked = random.randint(5, 9)
                Attacked = Attacked - damaged + Burned
                Attacked = Attacked - MoreDefence
                if Attacked < 1:
                        Attacked = random.randint(1, 5)
                print("Wendy did "+(str(Attacked))+" damage.")
                YourHp = YourHp - Attacked
                time.sleep(1)
                replit.clear()
                if YourHp <= 0:
                        print(Red+"You lost and were annihilated by Wendy."+reset) 
                        time.sleep(1)
                        YourHp = 25
                        Phase3FinalWendyHp = 100
                        damage = 0
                        damaged = 0             
                        restart()     
                else:
                        FinalFight3()

def FinalFight3():
        global damage
        global damaged
        global YourHp
        global Phase3FinalWendyHp
        global MoreHp
        global MoreDefend
        global MoreAttack
        global SFB2
        global WendyDefend
        print(darken+Red+"Final Form!"+reset)
        time.sleep(0.1)
        Sleep()
        print("Your Turn!")
        Sleep()
        print(Blue+"You: "+(str(YourHp))+" Hp")
        Sleep()
        print(Red+"Wendy: "+(str(Phase3FinalWendyHp))+" Hp")
        Sleep()
        print(reset+"(1) - Attack!")
        Sleep()
        print("(2) - Insult!")
        Sleep()
        print("(3) - Defend!")
        Sleep()
        print("(4) - Heal!")
        Sleep()
        Attack = input("Choose your attack: "+Blue)
        if Attack == "1":
                Sleep()
                Attacking = random.randint(2, 5) 
                Attacking = Attacking + damage
                Attacking = Attacking + MoreAttack
                Attacking = Attacking - WendyDefend
                if Attacking < 0:
                        Attacking = random.randint(1, 3)
                print(reset+"You did "+(str(Attacking))+" damage.")
                Phase3FinalWendyHp = Phase3FinalWendyHp - Attacking 
                time.sleep(1)
        if Attack == "2":
                Sleep()
                print(reset+"You called Wendy a "+Red+"meanie"+reset+".")
                Sleep()
                time.sleep(1)
                print("Your attacks do more damage now")
                damage = damage + random.randint(5, 7)
                time.sleep(1)
        if Attack == "3":
                Sleep()
                print(reset+"You "+Blue+"defended"+reset+" youself.")
                Sleep()
                time.sleep(1)
                print("Wendy's attacks do less damage now")
                damaged = damaged + random.randint(5, 7)
                time.sleep(1)
        if Attack == "4":
                Sleep()
                print(reset+"You "+green+"Healed"+reset+" youself.")
                Health = random.randint(5, 7)
                YourHp = YourHp + Health
                time.sleep(1)
                print("You gained "+green+(str(Health))+reset+ " Hp!")
                time.sleep(1)
        if Phase3FinalWendyHp <= 0:
                Sleep()
                print(Blue+"You beat Final Form Wendy!")
                time.sleep(1)
                Sleep()
                print(reset+"Your favorite TV show should be on right about now.")
                time.sleep(2)
                Sleep()
                YourHp = 25
                Phase3FinalWendyHp = 100
                damage = 0
                damaged = 0
                SFB2 = True
                print("(Watch it to win!)"+reset)
                time.sleep(1)
                restart()
        else:
                HerTurn4()

def HerTurn3():
        global damage
        global damaged
        global YourHp
        global Phase2FinalWendyHp
        global Burn
        global Burned
        global Attacked
        global SFB2
        global Healed
        global WendyDefend   
        global MoreAttack
        global MoreHp
        global MoreDefence
        replit.clear()
        Turn = random.randint(1, 5)
        if Turn == 4:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                WendyDefend = random.randint(5, 7)
                print("Wendy defended herself!")
                time.sleep(1)
                replit.clear()
                FinalFight2()
        if Turn == 3:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Burned = random.randint(5, 7)
                print("Wendy "+Red+"ROASTED"+reset+" you, her attack damage increased!")
                time.sleep(1)
                replit.clear()
                FinalFight2()
        if Turn == 2:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Healed = random.randint(2, 3)
                print("Wendy healed herself with a hamburger!")
                Phase2FinalWendyHp += Healed
                time.sleep(1)
                replit.clear()
                FinalFight2()
        else:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Attacked = random.randint(5, 9)
                Attacked = Attacked - damaged + Burned
                Attacked = Attacked - MoreDefence
                if Attacked < 1:
                        Attacked = random.randint(1, 5)
                print("Wendy did "+(str(Attacked))+" damage.")
                YourHp = YourHp - Attacked
                time.sleep(1)
                replit.clear()
                if YourHp <= 0:
                        print(Red+"You lost and were annihilated by Wendy."+reset) 
                        time.sleep(1)
                        YourHp = 25
                        Phase2FinalWendyHp = 75
                        damage = 0
                        damaged = 0             
                        restart()     
                else:
                        FinalFight2()
def FinalFight2():
        global damage
        global damaged
        global YourHp
        global Phase2FinalWendyHp
        global SFB2
        global MoreHp
        global MoreDefend
        global MoreAttack
        global WendyDefend
        print(darken+Red+"Last Fight!"+reset)
        time.sleep(0.1)
        Sleep()
        print("Your Turn!")
        Sleep()
        print(Blue+"You: "+(str(YourHp))+" Hp")
        Sleep()
        print(Red+"Wendy: "+(str(Phase2FinalWendyHp))+" Hp")
        Sleep()
        print(reset+"(1) - Attack!")
        Sleep()
        print("(2) - Insult!")
        Sleep()
        print("(3) - Defend!")
        Sleep()
        print("(4) - Heal!")
        Sleep()
        Attack = input("Choose your attack: "+Blue)
        if Attack == "1":
                Sleep()
                Attacking = random.randint(2, 5) 
                Attacking = Attacking + damage
                Attacking = Attacking + MoreAttack
                Attacking = Attacking - WendyDefend
                if Attacking < 0:
                        Attacking = random.randint(1, 3) 
                print(reset+"You did "+(str(Attacking))+" damage.")
                Phase2FinalWendyHp = Phase2FinalWendyHp - Attacking 
                time.sleep(1)
        if Attack == "2":
                Sleep()
                print(reset+"You called Wendy a "+Red+"meanie"+reset+".")
                Sleep()
                time.sleep(1)
                print("Your attacks do more damage now")
                damage = damage + random.randint(5, 7)
                time.sleep(1)
        if Attack == "3":
                Sleep()
                print(reset+"You "+Blue+"defended"+reset+" youself.")
                Sleep()
                time.sleep(1)
                print("Wendy's attacks do less damage now")
                damaged = damaged + random.randint(5, 7)
                time.sleep(1)
        if Attack == "4":
                Sleep()
                print(reset+"You "+green+"Healed"+reset+" youself.")
                Health = random.randint(3, 5)
                YourHp = YourHp + Health
                time.sleep(1)
                print("You gained "+green+(str(Health))+reset+ " Hp!")
                time.sleep(1)
        if Phase2FinalWendyHp <= 0:
                Sleep()
                print(Blue+"You beat Last Fight Wendy!")
                time.sleep(1)
                Sleep()
                print(green+"Level Up! - Heal got upgraded")
                time.sleep(2)
                Sleep()
                print(reset+"But...")
                time.sleep(1)
                Sleep()
                print(Red+"It's still not over yet..."+reset)
                time.sleep(1)
                YourHp = 25
                Phase2FinalWendyHp = 75
                damage = 0
                damaged = 0
                replit.clear()
                print("           ")
                time.sleep(0.1)
                replit.clear()
                print("|         |")
                time.sleep(0.1)
                replit.clear()
                print("||       ||")
                time.sleep(0.1)
                replit.clear()
                print("|||     |||")
                time.sleep(0.1)
                replit.clear()
                print("||||   ||||")
                time.sleep(0.1)
                replit.clear()
                print("||||| |||||")
                time.sleep(0.1)
                replit.clear()
                print("|||||||||||")
                time.sleep(0.1)
                replit.clear()
                print("||||| |||||")
                time.sleep(0.1)
                replit.clear()
                print("||||l F||||")
                time.sleep(0.1)
                replit.clear()
                print("|||al Fo|||")
                time.sleep(0.1)
                replit.clear()
                print("||nal For||")
                time.sleep(0.1)
                replit.clear()
                print("|inal Form|")
                time.sleep(0.1)
                replit.clear()
                FinalFight3()
        else:
                HerTurn3()
def HerTurn2():
        global damage
        global damaged
        global YourHp
        global FinalWendyHp
        global Burn
        global Burned
        global Attacked
        global SFB2
        global MoreHp
        global MoreDefend
        global MoreAttack
        global Healed
        replit.clear()
        Turn = random.randint(1, 4)
        if Turn == 3:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Burned = random.randint(5, 7)
                print("Wendy "+Red+"ROASTED"+reset+" you, her attack damage increased!")
                time.sleep(1)
                replit.clear()
                FinalFight()
        if Turn == 2:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Healed = random.randint(3, 5)
                print("Wendy healed herself with a hamburger!")
                FinalWendyHp += Healed
                time.sleep(1)
                replit.clear()
                FinalFight()
        else:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Attacked = random.randint(5, 9)
                Attacked = Attacked - damaged + Burned
                Attacked = Attacked - MoreDefence
                if Attacked < 1:
                        Attacked = random.randint(1, 5)
                print("Wendy did "+(str(Attacked))+" damage.")
                YourHp = YourHp - Attacked
                time.sleep(1)
                replit.clear()
                if YourHp <= 0:
                        print(Red+"You lost and were annihilated by Wendy."+reset) 
                        SFB2 = False 
                        time.sleep(1)
                        YourHp = 10 + MoreHp
                        FinalWendyHp = 50
                        damage = 1
                        damaged = 0             
                        restart()     
                else:
                        FinalFight()
def FinalFight():
        global damage
        global damaged
        global YourHp
        global FinalWendyHp
        global MoreHp
        global MoreDefend
        global MoreAttack
        global SFB2
        print(darken+Red+"Death Wish!"+reset)
        time.sleep(0.1)
        Sleep()
        print("Your Turn!")
        Sleep()
        print(Blue+"You: "+(str(YourHp))+" Hp")
        Sleep()
        print(Red+"Wendy: "+(str(FinalWendyHp))+" Hp")
        Sleep()
        print(reset+"(1) - Attack!")
        Sleep()
        print("(2) - Insult!")
        Sleep()
        print("(3) - Defend!")
        Sleep()
        print("(4) - Heal!")
        Sleep()
        Attack = input("Choose your attack: "+Blue)
        if Attack == "1":
                Sleep()
                Attacking = random.randint(2, 5) 
                Attacking = Attacking + damage
                Attacking = Attacking + MoreAttack
                print(reset+"You did "+(str(Attacking))+" damage.")
                FinalWendyHp = FinalWendyHp - Attacking 
                time.sleep(1)
        if Attack == "2":
                Sleep()
                print(reset+"You called Wendy a "+Red+"meanie"+reset+".")
                Sleep()
                time.sleep(1)
                print("Your attacks do more damage now")
                damage = damage + random.randint(2, 3)
                time.sleep(1)
        if Attack == "3":
                Sleep()
                print(reset+"You "+Blue+"defended"+reset+" youself.")
                Sleep()
                time.sleep(1)
                print("Wendy's attacks do less damage now")
                damaged = damaged + random.randint(5, 7)
                time.sleep(1)
        if Attack == "4":
                Sleep()
                print(reset+"You "+green+"Healed"+reset+" youself.")
                Health = random.randint(3, 5)
                YourHp = YourHp + Health
                time.sleep(1)
                print("You gained "+green+(str(Health))+reset+ " Hp!")
                time.sleep(1)
        if FinalWendyHp <= 0:
                Sleep()
                print(Blue+"You beat Death Wish Wendy!")
                time.sleep(1)
                Sleep()
                print(green+"Level Up! - Insult got upgraded")
                time.sleep(2)
                Sleep()
                print(reset+"But...")
                time.sleep(1)
                Sleep()
                print(Red+"It's not over yet..."+reset)
                time.sleep(1)
                YourHp = 25
                FinalWendyHp = 50
                damage = 0
                damaged = 0
                replit.clear()
                print("           ")
                time.sleep(0.1)
                replit.clear()
                print("|         |")
                time.sleep(0.1)
                replit.clear()
                print("||       ||")
                time.sleep(0.1)
                replit.clear()
                print("|||     |||")
                time.sleep(0.1)
                replit.clear()
                print("||||   ||||")
                time.sleep(0.1)
                replit.clear()
                print("||||| |||||")
                time.sleep(0.1)
                replit.clear()
                print("|||||||||||")
                time.sleep(0.1)
                replit.clear()
                print("|||||F|||||")
                time.sleep(0.1)
                replit.clear()
                print("|||| Fi||||")
                time.sleep(0.1)
                replit.clear()
                print("|||t Fig|||")
                time.sleep(0.1)
                replit.clear()
                print("||st Figh||")
                time.sleep(0.1)
                replit.clear()
                print("|ast Fight|")
                time.sleep(0.1)
                replit.clear()
                FinalFight2()
        else:
                HerTurn2()
def sprint(s):
        for c in s+ '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(1./25)
sprint("Hello, welcome to "+Blue+"Wendy's!"+reset)
replit.clear()
#Methods
def HerTurn():
        global damage
        global damaged
        global YourHp
        global WendyHp
        global Burn
        global Burned
        global Attacked
        global SFB
        global MoreHp
        global MoreDefend
        global MoreAttack
        replit.clear()
        Burn = random.randint(1, 3)
        if Burn == 3:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Burned = random.randint(2, 3)
                print("Wendy "+Red+"ROASTED"+reset+" you, her attack damage increased!")
                time.sleep(1)
                replit.clear()
                BossFight()
        else:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Attacked = random.randint(5, 9)
                Attacked = Attacked - damaged + Burned
                Attacked = Attacked - MoreDefence
                if Attacked < 1:
                        Attacked = random.randint(1, 3)
                print("Wendy did "+(str(Attacked))+" damage.")
                YourHp = YourHp - Attacked
                time.sleep(1)
                replit.clear()
                if YourHp <= 0:
                        print(Red+"You lost and were eaten by Wendy."+reset) 
                        SFB = False 
                        time.sleep(1)
                        YourHp = 10
                        WendyHp = 30
                        damage = 0
                        damaged = 0             
                        restart()     
                else:
                        BossFight()
def BossFight():
        global damage
        global damaged
        global YourHp
        global WendyHp
        global SFB
        global MoreHp
        global MoreDefend
        global MoreAttack
        print(Red+"Final Boss!"+reset)
        time.sleep(0.1)
        Sleep()
        print("Your Turn!")
        Sleep()
        print(Blue+"You: "+(str(YourHp))+" Hp")
        Sleep()
        print(Red+"Wendy: "+(str(WendyHp))+" Hp")
        Sleep()
        print(reset+"(1) - Attack!")
        Sleep()
        print("(2) - Insult!")
        Sleep()
        print("(3) - Defend!")
        Sleep()
        print("(4) - Heal!")
        Sleep()
        Attack = input("Choose your attack: "+Blue)
        if Attack == "1":
                Sleep()
                Attacking = random.randint(2, 5) 
                Attacking = Attacking + damage
                Attacking = Attacking + MoreAttack
                print(reset+"You did "+(str(Attacking))+" damage.")
                WendyHp = WendyHp - Attacking 
                time.sleep(1)
        if Attack == "2":
                Sleep()
                print(reset+"You called Wendy a "+Red+"meanie"+reset+".")
                Sleep()
                time.sleep(1)
                print("Your attacks do more damage now")
                damage = damage + random.randint(2, 3)
                time.sleep(1)
        if Attack == "3":
                Sleep()
                print(reset+"You "+Blue+"defended"+reset+" youself.")
                Sleep()
                time.sleep(1)
                print("Wendy's attacks do less damage now")
                damaged = damaged + random.randint(2, 3)
                time.sleep(1)
        if Attack == "4":
                Sleep()
                print(reset+"You "+green+"Healed"+reset+" youself.")
                Health = random.randint(3, 5)
                YourHp = YourHp + Health
                time.sleep(1)
                print("You gained "+green+(str(Health))+reset+ " Hp!")
                time.sleep(1)
        if WendyHp <= 0:
                Sleep()
                print(Blue+"You beat Wendy and got her car keys!")
                time.sleep(1)
                Sleep()
                print(green+"Level Up! - Defense got upgraded")
                time.sleep(2)
                Sleep()
                print(reset+"But...")
                time.sleep(1)
                Sleep()
                print(Red+"It's not over yet."+reset)
                time.sleep(1)
                Sleep()
                print("(Some more options have been changed or made available to you)")
                SFB = True
                time.sleep(1)
                YourHp = 10
                WendyHp = 30
                damage = 0
                damaged = 0
                restart()
        else:
                HerTurn()
def home():
        global FinalWendyHp 
        global WendyHp
        global YourHp
        global TheirHp
        global damage
        global damaged
        global Burn
        global Burned
        global Success
        global SFB
        global MoreAttack
        global MoreHp
        global MoreDefence
        global Healed
        global M
        global Upgrade2
        global SFB2
        global Upgrade1
        global Upgrade3
        global Healed
        global MoreHp
        global Phase2FinalWendyHp
        global Phase3FinalWendyHp
        global Off
        replit.clear()
        print(reset+"Your home.")
        time.sleep(1)
        Sleep()
        print("Now, what?")
        Sleep()
        print("(1) - Go To Wendy's")
        Sleep()
        print("(2) - Grab Armour")
        Sleep()
        print("(3) - Watch TV")
        Sleep()
        Leave2 = input("What do you do?: "+Blue)
        if Leave2 == "1":
                Sleep()
                print(reset+"You go back to wendy's.")
                time.sleep(1)
                restart()
        if Leave2 == "2":
                if Upgrade2 == True:
                        Sleep()
                        print(reset+"You can't find your armour, becuase your wearing it.")
                        Sleep()
                        time.sleep(1)
                        home()
                Sleep()
                print(reset+"You grab your armour.")
                Sleep()
                time.sleep(1)
                Upgrade2 = True
                print("Your take less damage now!")
                MoreDefence = 5
                time.sleep(1)
                home()
        if Leave2 == "3":
                if SFB2 == True:
                        timeEnd= time.time()
                        timeTaken = timeEnd - timeStart
                        Sleep()
                        print(green+"Congradulations, you won!")
                        time.sleep(1)
                        Sleep()
                        print("Thank you for playing.")
                        time.sleep(1)
                        Sleep()
                        print("Sir, this is a Wendy's was made by:")
                        Sleep()
                        time.sleep(1)
                        print("ColoredHue! - Main Developer")
                        time.sleep(1)
                        Sleep()
                        print("Bobo!(My Dog) - Helpful Support")
                        time.sleep(1)
                        Sleep()
                        print("And You!")
                        time.sleep(1)
                        Sleep()
                        print("Thank you for you support!")
                        time.sleep(1)
                        Sleep()
                        print("Time: " + (str(round(timeTaken, 1))) + "seconds")
                        time.sleep(1)
                        Sleep()
                        print("The game will now reset, goodbye.+reset")
                        time.sleep(2)
                        Phase3FinalWendyHp = 100
                        Phase2FinalWendyHp = 75
                        FinalWendyHp = 50
                        WendyHp = 30
                        YourHp = 10
                        TheirHp = 15
                        damage = 0
                        damaged = 0
                        Burn = 0
                        Burned = 0
                        SFB = False
                        SFB2 = False
                        MoreAttack = 0
                        MoreHp = 0
                        MoreDefence = 0
                        Healed = 0
                        Upgrade1 = False
                        Upgrade2 = False
                        Upgrade3 = False
                        M = False
                        Off = False
                        restart()
                Sleep()
                print(reset+"You see a Wendy's commercial on TV.")
                time.sleep(1)
                home()
        else:
                Sleep()
                print("Please pick one of the options.")
                time.sleep(1)
                home()
def outside():
        replit.clear()
        print(Red+"You left."+reset)
        time.sleep(1)
        Sleep()
        print("Now, where do you go?")
        Sleep()
        print("(1) - Back Inside")
        Sleep()
        print("(2) - To Your Home")
        Sleep()
        print("(3) - To McDonalds")
        Sleep()
        Leave = input("Go where?: "+Blue)
        if Leave == "1":
                restart()
        if Leave == "2":
                if SFB == True:
                        Sleep()
                        print(reset+"You drive home...")
                        time.sleep(1)
                        home()
                Sleep()
                print(Red+"You don't have a way to get home."+reset)
                time.sleep(2)
                outside()
        if Leave == "3":
                Sleep()
                print(Red+"You don't see a McDonalds around, only Wendy's..."+reset)
                time.sleep(2)
                outside()
        else:
                Sleep()
                print("Please input a valid option.")
                time.sleep(1)
                outside()

def restart():
        time.sleep(1)
        replit.clear()
        print(reset+"Hello, welcome to "+Blue+"Wendy's!")
        time.sleep(1)
        Sleep()
        All()
def TheirTurn():
        global M
        global YourHp
        global TheirHp
        global damaged
        global damage
        global MoreHp
        global MoreDefend
        global MoreAttack
        replit.clear()
        print(Red+"Manager's Turn!"+reset)
        Sleep()
        Attacked = random.randint(2, 5)
        Attacked = Attacked - damaged
        Attacked = Attacked - MoreDefence
        if Attacked < 1:
                Attacked = random.randint(0, 2)
        print("The manager did "+(str(Attacked))+" damage.")
        YourHp = YourHp - Attacked
        time.sleep(1)
        if YourHp <= 0:
                Sleep()
                print(Red+"You lost and were slapped by the manager."+reset)  
                M = False
                time.sleep(1)
                YourHp = MoreHp + 10
                TheirHp = 15
                damage = 0
                damaged = 0             
                restart()     
        else:
                Fight()
def Fight():
        global Success
        global damage
        global damaged
        global YourHp
        global TheirHp
        global MoreHp
        global MoreDefend
        global MoreAttack
        global M
        replit.clear()
        print("Boss Fight!")
        time.sleep(1)
        Sleep()
        print("Your Turn!")
        Sleep()
        print(Blue+"You: "+(str(YourHp))+" Hp")
        Sleep()
        print(Red+"Manager: "+(str(TheirHp))+" Hp")
        Sleep()
        print(reset+"(1) - Attack!")
        Sleep()
        print("(2) - Insult!")
        Sleep()
        print("(3) - Defend!")
        Sleep()
        Attack = input("Choose your attack: "+Blue)
        if Attack == "1":
                Sleep()
                Attacking = random.randint(2, 5) 
                Attacking = Attacking + damage
                Attacking = Attacking + MoreAttack
                print(reset+"You did "+(str(Attacking))+" damage.")
                TheirHp = TheirHp - Attacking
                time.sleep(1)
        if Attack == "2":
                Sleep()
                print(reset+"You called the manager a "+Red+"meanie"+reset+".")
                Sleep()
                time.sleep(1)
                print("Your attacks do more damage now")
                damage = damage + random.randint(2, 3)
                time.sleep(1)
        if Attack == "3":
                Sleep()
                print(reset+"You "+Blue+"defended"+reset+" youself.")
                Sleep()
                time.sleep(1)
                print("Manager's attacks do less damage now")
                damaged = damaged + random.randint(2, 3)
                time.sleep(1)
        if TheirHp <= 0:
                Sleep()
                print(Blue+"You beat the manager!")
                time.sleep(1)
                Sleep()
                print(f"The manager isn't guarding the door anymore!{reset}")
                Sleep()
                print(green+"Level Up! - You learned the skill: Heal"+reset)
                time.sleep(2)
                M = True
                time.sleep(1)
                YourHp = 10 + MoreHp
                TheirHp = 15
                damage = 1
                damaged = 0
                restart()
        else:
                TheirTurn()
def Option1():
        print("(1) - Order a Big Mac.")

def Option2():
        print("(2) - Escape!")

def Option3():
        print("(3) - I WANT TO SPEAK TO YOUR MANAGER!")

def Option4():
        print("(4) - Wait.")

def Option5():
        print("(5) - Leave.")

def Sleep():
        time.sleep(0.1)
        print("")

def All():
        global damage
        global damaged
        global YourHp
        global Phase3FinalWendyHp
        global Burn
        global Burned
        global Attacked
        global SFB2
        global Healed
        global WendyDefend     
        global damage
        global damaged
        global MoreAttack
        global MoreHp
        global MoreDefence
        global Healed
        global M
        global Off
        global Upgrade1
        global Upgrade2
        global Upgrade3
        global Answer3
        Phase3FinalWendyHp = 100
        YourHp = 10
        damage = 0
        damaged = 0
        Burn = 0
        Burned = 0
        Healed = 0
        print(reset+"What can I get for you?")
        time.sleep(1)
        Sleep()
        Option1()
        Sleep()
        Option2()
        Sleep()
        Option3()
        Sleep()
        Option4()
        Sleep()
        Option5()
        Sleep()
        Answer = (input("Input selection here: "+Blue))
        Sleep()
        if Answer == "1":
                if SFB == True and Off == False:
                        replit.clear()
                        print(reset+"Sure, coming right up!")
                        time.sleep(1)
                        Sleep()
                        print("Here's your Big Mac- I mean burger, have a nice day.")
                        time.sleep(1)
                        Sleep()
                        print("You ate the Big Mac and gained 15 Hp!")
                        Upgrade1 = True
                        YourHp = 25
                        Off = True
                        time.sleep(1)
                        restart()
                if Off == True:
                        replit.clear()
                        print(reset+"No more Big Mac's- I mean burgers, for you.")
                        time.sleep(1)
                        Sleep()
                        print("Please go away.")
                        time.sleep(1)
                        restart()
                replit.clear()
                print(reset+"Sir, this is wendy's.")
                time.sleep(1)
                Sleep()
                print("Please go away.")
                time.sleep(1)
                restart()
        if Answer == "2":
                replit.clear()
                print(reset+"You look for a way to escape the Wendy's")
                time.sleep(1)
                Sleep()
                print("You see two ways to escape, (1) the employee's door, (2) the vents.")
                time.sleep(1)
                Sleep()
                Answer2 = input("Which do you choose: "+Blue)
                if Answer2 == "1":
                        Sleep()
                        print(reset+"You go in the employee's door...")
                        if M == True and SFB == False:
                                print(Red+"The developer was infront of the door and slapped you."+reset)
                                time.sleep(1)
                                restart()
                        if SFB2 == True:
                                print("She's not here anymore")
                                time.sleep(1)
                                restart()
                        if Upgrade1 == False and Upgrade2 == False and Upgrade3 == False and SFB == True:
                                time.sleep(1)
                                Sleep()
                                print(f"{Red}Your not ready to fight her yet.{reset}")
                                time.sleep(1)
                                restart()
                        if M == True and SFB == True:
                                time.sleep(1)
                                Sleep()
                                print("There's Wendy's secret recipy, it shows a Big Mac on the front.")
                                time.sleep(2)
                                replit.clear()
                                print(Red+"Uh-oh what's that?")
                                time.sleep(1)
                                print("It's Wendy, she looks enraged.")
                                time.sleep(1)
                                replit.clear()
                                print("           ")
                                time.sleep(0.1)
                                replit.clear()
                                print("|         |")
                                time.sleep(0.1)
                                replit.clear()
                                print("||       ||")
                                time.sleep(0.1)
                                replit.clear()
                                print("|||     |||")
                                time.sleep(0.1)
                                replit.clear()
                                print("||||   ||||")
                                time.sleep(0.1)
                                replit.clear()
                                print("||||| |||||")
                                time.sleep(0.1)
                                replit.clear()
                                print("|||||||||||")
                                time.sleep(0.1)
                                replit.clear()
                                print("||||h W||||")
                                time.sleep(0.1)
                                replit.clear()
                                print("|||th Wi|||")
                                time.sleep(0.1)
                                replit.clear()
                                print("||ath Wis||")
                                time.sleep(0.1)
                                replit.clear()
                                print("|eath Wish|")
                                time.sleep(0.1)
                                replit.clear()
                                FinalFight()
                        else:
                                time.sleep(1)
                                Sleep()
                                print("There was an employee right infront of the door!")
                                time.sleep(1)
                                Sleep()
                                print("You got caught and brought to the manager.")
                                time.sleep(1)
                                Sleep()
                                print(Red+"The manager slaps you.")
                                M = False
                                time.sleep(1)
                                restart()
                if Answer2 == "2":
                        Sleep()
                        print(reset+"You went into the vents...")
                        time.sleep(1)
                        Sleep()
                        print("You made your way out of the vents and found the managers secret stash of money...")
                        time.sleep(1)
                        Sleep()
                        print("You need to get out of there fast!")
                        time.sleep(1)
                        Sleep()
                        print("There is a door in front of you, it has a keypad on it.")
                        time.sleep(1)
                        Sleep()
                        Answer3 = input("Enter (something) in the keypad: "+Blue)
                        if Answer3 == "something":
                                if M == True:
                                        if SFB == True:
                                                if SFB2 == True:
                                                        Sleep()
                                                        print("She's not here anymore")
                                                        time.sleep(1)
                                                        restart()
                                                Sleep()
                                                print(reset+"The ground below you falls open")
                                                time.sleep(1)
                                                Sleep()
                                                print('Wendy has left, where is she now?')
                                                time.sleep(1)
                                                restart()
                                        Sleep()
                                        print(reset+"The ground below you falls open")
                                        time.sleep(1)
                                        Sleep()
                                        print(Red+"You see wendy herself, sitting in her chair very menacingly.")
                                        time.sleep(2)
                                        Sleep()
                                        print("Your doomed."+reset)
                                        time.sleep(0.5)
                                        replit.clear()
                                        print("           ")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("|         |")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("||       ||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("|||     |||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("||||   ||||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("||||| |||||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("|||||||||||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("||||| |||||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("||||l B||||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("|||al Bo|||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("||nal Bos||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("|inal Boss|")
                                        time.sleep(0.1)
                                        replit.clear()
                                        BossFight()
                                else:
                                        Sleep()
                                        print(reset+"It opened!")
                                        time.sleep(1)
                                        Sleep()
                                        print(Red+"The manager was standing right in front of the door, he slaps you.")
                                        M = False
                                        time.sleep(5)
                                        restart()
                        elif Answer3 == ":flushed:":
                                Sleep()
                                print(reset+"-O_O-")
                                time.sleep(1)
                                restart()
                        elif Answer3 == "Easy Mode":
                                Sleep()
                                print(reset+"Lol, that doesn't exist")
                                time.sleep(1)
                                restart()
                        elif Answer3 == ":?:":
                                Sleep()
                                print(reset+"Your in a Wendy's dimention, there are only Wendy's here. Here, Wendy is a very powerful being.")
                                time.sleep(3)
                                restart()
                        elif Answer3 == "Secret":
                                Sleep()
                                print(reset+"You found a secret")
                                time.sleep(1)
                                restart()
                        elif Answer3 == "Developer Boss":
                                Sleep()
                                print(reset+"Sorry, the developer is too lazy to make this, maybe later?")
                                time.sleep(1)
                                restart()
                        else:
                                Sleep()
                                print(Red+"It didn't work!")
                                time.sleep(1)
                                if M == True:
                                        Sleep()
                                        print(reset+"Since the manager isn't around I guess I'll slap you.")
                                        time.sleep(1)
                                        print(Red+"The game developer slaps you.")
                                        time.sleep(1)
                                        restart()
                                Sleep()
                                print(Red+"The manager walks in and slaps you.")
                                time.sleep(1)
                                restart()
                else:
                        if M == True:
                                Sleep()
                                print("Due to you failure to pick an option, the manager- oh, he's gone. I guess I'll slap you then.")
                                time.sleep(1)
                                print(Red+"The game developer slaps you.")
                                time.sleep(1)
                                restart()
                        Sleep()
                        print(Red+"Because of your failure to pick one of the options, the manager came and slapped you.")
                        time.sleep(3)
                        restart()
        if Answer == "3":
                replit.clear()
                if M == True:
                        print(Red+"The manager isn't here anymore."+reset)
                        time.sleep(1)
                        restart()
                print(Red+"Sir, I AM THE MANAGER!"+reset)
                time.sleep(2)
                replit.clear()
                print("           ")
                time.sleep(0.1)
                replit.clear()
                print("|         |")
                time.sleep(0.1)
                replit.clear()
                print("||       ||")
                time.sleep(0.1)
                replit.clear()
                print("|||     |||")
                time.sleep(0.1)
                replit.clear()
                print("||||   ||||")
                time.sleep(0.1)
                replit.clear()
                print("||||| |||||")
                time.sleep(0.1)
                replit.clear()
                print("|||||||||||")
                time.sleep(0.1)
                replit.clear()
                print("|||||F|||||")
                time.sleep(0.1)
                replit.clear()
                print("|||| Fi||||")
                time.sleep(0.1)
                replit.clear()
                print("|||s Fig|||")
                time.sleep(0.1)
                replit.clear()
                print("||ss Figh||")
                time.sleep(0.1)
                replit.clear()
                print("|oss Fight|")
                time.sleep(0.1)
                replit.clear()
                Fight()
                
        if Answer == "4":
                replit.clear()
                print(reset+"You wait...")
                time.sleep(5)
                if SFB == True:
                        if Upgrade3 == True:
                                Sleep()
                                print("You wait some more...")
                                Sleep()
                                time.sleep(5)
                                print("You wait even longer...")
                                Sleep()
                                time.sleep(5)
                                print("You wait impatiently...")
                                Sleep()
                                time.sleep(5)
                                print(Red+"You give up."+reset)
                                Sleep()
                                time.sleep(1)
                                restart()
                        Sleep()
                        print("A secret compartment opens up, there's a knife inside!")
                        Sleep()
                        time.sleep(1)
                        print("Your attacks do more damage now!")
                        Upgrade3 = True
                        MoreAttack = 5
                        time.sleep(1)
                        restart()
                else:
                        Sleep()
                        print("You wait some more...")
                        Sleep()
                        time.sleep(5)
                        print("You wait even longer...")
                        Sleep()
                        time.sleep(5)
                        print("You wait impatiently...")
                        Sleep()
                        time.sleep(5)
                        print(Red+"You give up."+reset)
                        Sleep()
                        time.sleep(1)
                        restart()
        if Answer == "5":
                outside()
        else:
                print("Please input a valid option.")
                time.sleep(1)
                restart()

#Code starts here
timeStart = time.time()
print("Hello, welcome to "+Blue+"Wendy's"+reset+"!")
time.sleep(1)
Sleep()
All()


 


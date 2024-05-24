# Kyloexe
# This program is a wrapper for the most common terminal commands in Linux and Windows!

# MODULES

import os
from pathlib import Path
import shutil

# CONSTANTS
# set the below variable to be the Linux enviromental variable $USER
USER_VAR_LINUX = str(os.environ.get('USER'))



# the main function

def main():
    print("=" * 39)
    print(" ")
    print("Welcome to Kyloexe's Command Commander!")
    print(" ")
    print("="*39)

    print("")
    print("Windows (win or windows)")
    print("Linux (lin or linux)")

    os_choice_user = input("From the above options, pick one to proceed: ")
    
    if os_choice_user == 'win' or os_choice_user == 'windows':
        windows()

    elif os_choice_user == 'lin' or os_choice_user == 'linux':
        linux()

    print("Thank you for using my program, god bless and goodbye! ")
    print('''
 __   __   _              _          
 \ \ / /__| |__ _ ___ _ _(_)___ _ _  
  \ V / -_) / _` / _ \ '_| / _ \ ' \ 
   \_/\___|_\__,_\___/_| |_\___/_||_|
                                     
''')






# Function that contains all the linux commands and their outputs



def linux():
    def create_file(path_touch):
        print("Hewwo, UWU")

                                                                                                              

    print("You have entered LINUX mode!")

    # Print statements that give the user the available modes to be used

    print("OPTIONS: ")
    print("1: ifconfig")
    print("2: top")
    print("3. touch")
    print("4: mkdir")
    print("5: rmdir")
    print("6") 

    list_command_linux = ['1','2','3','4','5']

    # Asks the user which of the options given they'd like to use

    command_choice_linux = input("Which Bash commands would you like to execute? ")

    # if c, the below block of code is executed

    if command_choice_linux == list_command_linux[0]:

        # Asks the user if they'd like to put the output of ifconfig into a file

        to_file_ifconfig = input("Do you want to print this command to a text file? (1/2)")

        # if the variable is equelled to 1, a file is created and written to by using touch

        if to_file_ifconfig == "1" :
            create_file = os.system(f'touch /home/{USER_VAR_LINUX}/Documents/ifconfig.txt')
            if_file =  open(f'/home/{USER_VAR_LINUX}/Documents/ifconfig.txt', 'wt')
            e = str(os.system('ifconfig'))
            if_file.write(e)
            if_file.close()

        # If the variable is equelled to 2, ifconfig is ran

        elif to_file_ifconfig == "2":
            os.system('ifconfig')
    
    # runs top when the variable command_choice is the same as 2

    elif command_choice_linux == list_command_linux[1]:
        os.system('top')

    elif command_choice_linux == list_command_linux[2]:
        name_of_file_touch = input("Okay, we're now using touch! What is the name of the file?: ")
        path_of_file_touch = Path(input("Please input either an absolute or relative path you'd like the file to be located at (Format would be like: /path/to/the/file.txt): "))

        if path_of_file_touch.exists == False:
            os.system(f'touch {path_of_file_touch}')

        
                      
    elif command_choice_linux == list_command_linux[3]:
        print("Okay, we're now creating directories!")
        print("It should be in the following format: /home/user/Desktop etc.")
        name_of_dir_linux = Path(input("Please input the name of the directory you want to make"))
        name_of_dir_linux.mkdir(parents=True, exist_ok=True)
        
    elif command_choice_linux == list_command_linux[4]:
        print("Okay, we're now removing directories!")
        name_of_dir_linux_remove = Path(input("Please input the name of the directory you want to remove"))
        
        try:
            shutil.rmtree(name_of_dir_linux_remove)
        except OSError as e:
            print("E")
           

        
def windows():
    print("You have entered WINDOWS mode!")


    print("OPTIONS")
    print('1: ipconfig')
    print('2: tasklist')
    print('3: create empty file (echo <text> >> <name/location>)')
    print('4: mkdir')
    print('5: rmdir')

    list_cmd = ['1','2','3','4','5']

    command_choice_cmd = input("Please input a choice from the above options: ")

    if command_choice_cmd == list_cmd[0]:
        to_file_ipconfig = input('Do you want to print your network information to a text file? (Y/N)')
        list_file_ipconfig = ['Y','y','N','n']

        if to_file_ipconfig == list_file_ipconfig[0] or to_file_ipconfig == list_file_ipconfig[1]:
            name_of_file_ipconfig = input("What are you going to name the file?: ")
            os.system(f'ipconfig /all >> {name_of_file_ipconfig}')

        elif to_file_ipconfig == list_file_ipconfig[2] or to_file_ipconfig == [4]:
            os.system('ipconfig /all')

    elif command_choice_cmd == list_cmd[1]:
        os.system('tasklist')

    elif command_choice_cmd == list_cmd[2]:
        name_of_file_cmd = input("Please input a name for the new file!: ")
        stuff_in_file_cmd = input("Please input what you want to be in the file: ")
        os.system(f'echo {stuff_in_file_cmd} >> {name_of_file_cmd}')

    elif command_choice_cmd == list_cmd[3]:
        name_of_dir_cmd = input("Please input the name of the directory you want to create: ")
        os.system(f'mkdir {name_of_dir_cmd}')

    elif command_choice_cmd == list_cmd[4]:
        name_of_dir_remove_cmd = input("Please input the name of the directory you want to remove: ")
        os.system(f'rmdir {name_of_dir_remove_cmd}')
        print("e")

    else:
        windows()

if __name__ == "__main__":
    main()


# Refactor the linux() function to have if statements check if the user input is within a pre-determined list

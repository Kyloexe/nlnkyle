# Kyloexe
# This program is a wrapper for the most common terminal commands in Linux and Windows!

# MODULES
# imports the os module (used to interact with the underlying operating system (Windows, linux, mac (hipster)))
import os
# Pathlib is a module used to make the use of paths within an OS easier for the programmer 
from pathlib import Path
# shutil is used to delete a file at a certain location within the filesystem using absolute paths
import shutil

# CONSTANTS
# set the below variable to be the Linux enviromental variable $USER
USER_VAR_LINUX = str(os.environ.get('USER'))



# the main function is used to call all the underlying functions which contain all the functionality of this script

'''This function welcomes the user, it then asks the user which operating system's commands they'd like to use. 
If the user selects windows, the windows function is called
If the user selects linux, the linux function is called
Once one of these functions are ran, the script ends'''

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

    # if below statement is true, the below block of code is executed

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

        # If the variable is equelled to 2, ifconfig is executed in the terminal

        elif to_file_ifconfig == "2":
            os.system('ifconfig')
    
    # runs top when the statement containing it is true

    elif command_choice_linux == list_command_linux[1]:
        os.system('top')

    # if the below statement is true, the user is asks to input the name of the file to be created, then the path where the file will be located on the main drive (both of these are stored as variables)

    elif command_choice_linux == list_command_linux[2]:
        name_of_file_touch = input("Okay, we're now using touch! What is the name of the file?: ")
        path_of_file_touch = Path(input("Please input either an absolute or relative path you'd like the file to be located at (Format would be like: /path/to/the/file.txt): "))

        if path_of_file_touch.exists == False:
            os.system(f'touch {path_of_file_touch}')

   # Very similar to the above block of code, creates a directory named by the user at a certain location on the main drive     
                      
    elif command_choice_linux == list_command_linux[3]:
        print("Okay, we're now creating directories!")
        print("It should be in the following format: /home/user/Desktop etc.")
        name_of_dir_linux = Path(input("Please input the name of the directory you want to make"))
        name_of_dir_linux.mkdir(parents=True, exist_ok=True)
        
    # Similar to above block of code, instead uses shutil to remove a directory

    elif command_choice_linux == list_command_linux[4]:
        print("Okay, we're now removing directories!")
        name_of_dir_linux_remove = Path(input("Please input the name of the directory you want to remove"))
        
        try:
            shutil.rmtree(name_of_dir_linux_remove)
        except OSError as e:
            print("E")
           
# The function from which the windows commands are ran
        
def windows():
    print("You have entered WINDOWS mode!")

    # Prints the options avaialble to the user

    print("OPTIONS")
    print('1: ipconfig')
    print('2: tasklist')
    print('3: create empty file (echo <text> >> <name/location>)')
    print('4: mkdir')
    print('5: rmdir')

    # A list called 'list_cmd' is created with 5 strings going from '1' to '5'

    list_cmd = ['1','2','3','4','5']

    # Asks the user to input a number above that correlates to a command

    command_choice_cmd = input("Please input a choice from the above options: ")

    '''Below, comments will only explain the general idea of the code and it'll explain the more complicated code where possible'''

    # if this if statement is true, it asks the user if they want to put the output of the command into a file
    # if the if statement is false, it just runs the command in the terminal


    if command_choice_cmd == list_cmd[0]:
        to_file_ipconfig = input('Do you want to print your network information to a text file? (Y/N)')
        list_file_ipconfig = ['Y','y','N','n']

        if to_file_ipconfig == list_file_ipconfig[0] or to_file_ipconfig == list_file_ipconfig[1]:
            name_of_file_ipconfig = input("What are you going to name the file?: ")
            os.system(f'ipconfig /all >> {name_of_file_ipconfig}')

        elif to_file_ipconfig == list_file_ipconfig[2] or to_file_ipconfig == [4]:
            os.system('ipconfig /all')

    # runs the command if the if statement is true

    elif command_choice_cmd == list_cmd[1]:
        os.system('tasklist')

    # If if is true, asks the user to input data into a variable, then to name the file, that is put into another variable
    # Lastly, the command 'echo' is ran with the variables created to create the specified file

    elif command_choice_cmd == list_cmd[2]:
        name_of_file_cmd = input("Please input a name for the new file!: ")
        stuff_in_file_cmd = input("Please input what you want to be in the file: ")
        os.system(f'echo {stuff_in_file_cmd} >> {name_of_file_cmd}')

    # if the below statement is true, the user is asked to name a directory within a variable, the command 'mkdir' is then executed with the used variable

    elif command_choice_cmd == list_cmd[3]:
        name_of_dir_cmd = input("Please input the name of the directory you want to create: ")
        os.system(f'mkdir {name_of_dir_cmd}')

    # The user is asks to input the name of a directory to be removed, the command 'rmdir' is then executed with the inputted directory

    elif command_choice_cmd == list_cmd[4]:
        name_of_dir_remove_cmd = input("Please input the name of the directory you want to remove: ")
        os.system(f'rmdir {name_of_dir_remove_cmd}')

    # If none of the above options are true, the function windows() is ran (brings the user back to the beginning, acting as an impromptu loop)

    else:
        windows()

# Is used to ensure that this script can be ran as both a module (like print()) or a standalone script to be executed as a file

if __name__ == "__main__":
    main()




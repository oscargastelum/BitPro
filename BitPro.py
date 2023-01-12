#########################################################################
#
# Program : BitwPro
#  
# Created : 01/04/2023
#   
# Programmer : Oscar Gastelum 
#  
# ########################################################################  
#  Program description/ purpose : 
#
#--------------------------- Change History ------------------------------
# Programmer : 
# Date :
# Description of change : 
#  
#########################################################################/ 

#modules 
import csv
import json  # manipulation of CSV files
import tkinter as tk
from tkinter import filedialog
from tkinter import *   # import everything from tkinter 
import os
import pyinputplus as pyip
import sys
import datetime


WIDTH = 80  #width for the divider bars to be printed. (Headers)
PROGRAM_NAME = 'BITPRO'     #program title 

PASSWORD_CHAR_LENGTH = 8    #password length requirement 
PASSWORD_MIN_NUM = 2        #password min recommended length
PASSWORD_MIN_SPECIAL = 2    #password min special characters
COLUMN_WIDTH = 20           #column width for the csv fields header

#determine min and max menu options input 
MIN_MENU_OPTIONS = 0
MAX_MENU_OPTIONS = 9

# CONSTANTS
#replace to match your bitwarden login file name or match to this name.
BITWARDEN_LOGIN_CSV = 'bitdata.csv'
SAVE_FILE_NAME = 'updatedBit'
WEAK_PASS_TXT_FILE_NAME = 'PasswordReport'



#--------------------------- Functions  ------------------------------


"""
This function takes a input string as argument and print it and also return the same string
:param input_string: string to be printed
:return: returns the same string
"""
def print_and_return_string(input_string):
    print(input_string)
    return input_string


"""Generates a save file name based on the given name and the current date and time.

Args:
    name (str): The base name for the save file.

Returns:
    str: The generated save file name.
"""
def get_save_file_name(name):
    # Get the current date and time
    now = datetime.datetime.now()

    # Format the date and time as a string that can be used in a file name
    date_time_str = now.strftime("%Y-%m-%d_%H-%M-%S")

    # Return the save file name
    return name + "_" + date_time_str 




"""
Print a header for a CSV file with dividers between each field and with each field centered.

Parameters:
    fields (List[str]): List of field names.
    column_width (int): Width of each column.

Returns:
    None
"""
def printCSVHeader():
    fields = ["folder", "favorite", "type", "name", "notes", "fields", "reprompt", "login_uri", "login_username", "login_password", "login_totp"]
    output = '\nCSV Fields:\n'
    # Print top divider
    output += "-" * COLUMN_WIDTH + "|"
    for field in fields[1:]:
        output += "-" * COLUMN_WIDTH + "|"
    output += '\n'

    # Print field names
    output += fields[0].center(COLUMN_WIDTH) + "|"
    for field in fields[1:]:
        output += field.center(COLUMN_WIDTH) + "|"
    output += '\n'

    # Print bottom divider
    output += "-" * COLUMN_WIDTH + "|"
    for field in fields[1:]:
        output += "-" * COLUMN_WIDTH + "|"
    output += '\n'

    print(output)
    return output










"""Prints a character to the screen a given number of times.

Args:
char: The character to print (default: '-')
width: The number of times to print the character (default: 75)
"""
def printDiv(char='-', width=75):
  for i in range(width):
    print(char, end='')
  print()


"""_summary_
Will read all the lines from the CSV File containing the following fields	
folder,favorite,type,name,notes,fields,reprompt,login_uri,login_username,
login_password,login_totp

This function reads a CSV file and prints the contents of each row to the 
console. The function assumes that the file is in the same format as the 
BITWARDEN_LOGIN_CSV file and has the same field names.

The function opens the file using the open() function and specifies the mode 
as 'r' for reading. It then creates a csv.DictReader object, which reads the 
rows of the CSV file as dictionaries, with the keys being the field names and 
the values being the field values.

The function then iterates over the rows in the reader object using a for 
loop and prints the contents of each row to the console.

You can modify this function to do something different with the data, such 
as storing the data in a database or performing some analysis on it.
"""
# def readCSVFile():
#     with open(BITWARDEN_LOGIN_CSV, 'r') as file:
#         reader = csv.DictReader(file, fieldnames=["folder", "favorite", "type", "name", "notes", "fields", "reprompt", "login_uri", "login_username", "login_password", "login_totp"])
#         for row in reader:
#             # You can access each field in the row using the field names
#             folder = row['folder']
#             favorite = row['favorite']
#             type = row['type']
#             name = row['name']
#             notes = row['notes']
#             fields = row['fields']
#             reprompt = row['reprompt']
#             login_uri = row['login_uri']
#             login_username = row['login_username']
#             login_password = row['login_password']
#             login_totp = row['login_totp']
#             # You can do something with the data here
#             print(f"Folder: {folder}, Favorite: {favorite}, Type: {type}, Name: {name}, Notes: {notes}, Fields: {fields}, Reprompt: {reprompt}, Login URI: {login_uri}, Login username: {login_username}, Login password: {login_password}, Login TOTP: {login_totp}")


"""Prompts the user to select a CSV file and returns the name of the selected file.

Returns:
    str: The name of the selected CSV file.
"""
def select_csv_file():
    # Create a Tkinter root window
    root = tk.Tk()

    # Hide the main window
    root.withdraw()

    # Open a file dialog to select the CSV file
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    # Split the file path into a directory and a file name
    directory, file_name = os.path.split(file_path)

    # Return the file name
    return file_name



"""_summary_
This function reads the CSV file and stores the data from each row in a list 
called data. It then returns the data list when the function is finished 
executing.

You can then access the data from the CSV file by calling the readCSVFile 
function and storing the returned value in a variable:

csvData = readCSVFile()

You can then access the data from the CSV file by indexing into the csvData 
list. For example, to access the first row of data, you would use csvData[0].

Returns:
    _type_: _description_
"""    
def getCSVFile():
    data = []
    if not os.path.exists(BITWARDEN_LOGIN_CSV):
        print(f"Error: CSV file {BITWARDEN_LOGIN_CSV} not found. Please select the file with the csv data.")
        
        file_name = select_csv_file()
    else:
        file_name = BITWARDEN_LOGIN_CSV
        
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file, fieldnames=["folder", "favorite", "type", "name", "notes", "fields", "reprompt", "login_uri", "login_username", "login_password", "login_totp"])
        for row in reader:
            data.append(row)


    return data, file_name




"""_summary_
This function takes in a list of dictionaries called data and an optional 
parameter called sortField, which defaults to 'all' if no value is 
specified. This will sort the data by folder name, then favorite, then type, 
and so on

It sorts the data using the sortField value as the key in 
the lambda function passed to the sorted function.


Args:
    data (list of dictionaries): list of dictonaries from a csv file 
    sortField (str, optional): _description_. Defaults to 'all'. Will sort
    the list given this parameter. If none, will defualt to 'all'

Returns:
    list of dictonaries: list ordered alphabetically given the sortField 
"""    
def sortData(data, sortField='all'):
    if(sortField == 'all'):
        # Sort the data by folder name, then favorite, then type, and so on
        sortedData = sorted(data, key=lambda x: (x['folder'], x['favorite'], x['type'], x['name'], x['notes'], x['fields'], x['reprompt'], x['login_uri'], x['login_username'], x['login_password'], x['login_totp']))
    else:  
        # Sort the data by the specified field
        sortedData = sorted(data, key=lambda x: x[sortField])

    return sortedData




"""
Saves a string to a txt file with the given name.

Parameters:
string (str): The string to be saved.
name (str): The name of the txt file.

"""
def save_to_txt(string, name):
    with open(name+'.txt', 'w') as file:
        file.write(string)
    print(f"Successfully saved {name}.txt")




"""
Overwrites a CSV file with the given data.
Args:
    data (list): A list of dictionaries containing the data to be written to 
    the CSV file.
    fileName (str): The name of the CSV file to be overwritten.
"""
def writeCSVFile(data, fileName):  
    # Create a temporary file to store the new data
    tempFileName = 'temp.csv'

    # Open the temporary file for writing
    with open(tempFileName, 'w', newline='') as file:
        # Create a CSV writer object
        writer = csv.DictWriter(file, fieldnames=["folder", "favorite", "type", "name", "notes", "fields", "reprompt", "login_uri", "login_username", "login_password", "login_totp"])

        # Write the data to the CSV file
        for row in data:
            writer.writerow(row)

    # Rename the temporary file to the original file name
    os.rename(tempFileName, (fileName + '.csv' ))
   
    print(f"Successfully saved data to file {fileName}")




"""_summary_
Will print the main menu optons to the user 
"""
def printMainMenuOptions():
    printDiv('-', int(WIDTH / 2))
    print("MAIN MENU")
    printDiv('-', int(WIDTH / 2))
    print("\n*TOOLS AND REPORTS*\n")
    print("1. Reused Passwords")
    print("2. Save Reused Password Report [* 1st generate Reused Password Report. Choice 1 *]")
    print("3. Weak Passwords")
    print("4. Save Weak Password Report [* 1st generate Weak Password Report. Choice 3 *]")
    print("5. Remove Duplicates")
    print("6. Save File")
    print("7. Save as New File")
    print("8. Quit Program")

    print("\n*SETTINGS*\n")
    print("9. Set Weak Password Settings")




"""
Prints a header with the given text centered within a line of the specified width.

Parameters:
- header_text (str): The text to print as the header.
- line_width (int, optional): The width of the line to print the header within. Default is 80 characters.
"""
def printHeader(header_text, line_width=80):
    #Get the length of the header text
    text_length = len(header_text)

    #Calculate the number of spaces to add on each side of the equals signs
    num_spaces = (line_width - text_length) // 2

    #Print the header text surrounded by equals signs
    output = " " * num_spaces + "=" * text_length + " " * num_spaces + '\n'
    output += header_text.center(line_width) + '\n'
    output += " " * num_spaces + "=" * text_length + " " * num_spaces + '\n'

    print(output)
    return output




"""_summary_
Will display the menu options for configuring the strong password requirement settings.
"""
def printConfigPassReqMenuOptions(password_requirements):
    print("\nChoose the options you want to enable/disable:\n")
    print("1. Length: {}".format(password_requirements["length"]))
    print("2. A-Z (uppercase): {}".format("enabled" if password_requirements["uppercase"] else "disabled"))
    print("3. a-z (lowercase): {}".format("enabled" if password_requirements["lowercase"] else "disabled"))
    print("4. 0-9 (digits): {}".format("enabled" if password_requirements["digits"] else "disabled"))
    print("5. !@#$%^&* (special characters): {}".format("enabled" if password_requirements["special_characters"] else "disabled"))
    print("6. Minimum number of numbers: {}".format(password_requirements["min_numbers"]))
    print("7. Minimum number of special characters: {}".format(password_requirements["min_special"]))
    print("8. Avoid ambiguous characters: {}".format("enabled" if password_requirements["avoid_ambiguous"] else "disabled"))
    print("9. Done\n")






"""Will provide the configurations settings for what determines a weak password. 

Args:
    password_requirements (dict): default dict of weak password requirement settings 

Returns:
    dict : updated dict of password requirement settings. 
"""    
def configurePasswordRequirements(password_requirements):
    printHeader("Password Requirements Configuration")
    
    option = -1
    
    # Loop until the user is done configuring the password requirements
    while option != 9:
        
        # display menu options 
        printConfigPassReqMenuOptions(password_requirements)
        
        # get valid user input 
        option = pyip.inputInt(prompt="\nEnter your choice: ", min = 1, max = 9)
        print()

        if(option != 9):
            printDiv('-', int(WIDTH / 2))

        # modify min char length 
        if option == 1:
            length = pyip.inputInt(min=1, prompt="Enter the minimum length: ")
            if length < 8:
                print("Warning: it is recommended to set the minimum length to at least 8 characters for security reasons.")
                confirm = pyip.inputYesNo(prompt="Are you sure you want to continue with a shorter minimum length? ")
                if not confirm:
                    continue
            password_requirements["length"] = length
            print("Minimum length successfully set to {}".format(length))
        # modify uppercase
        elif option == 2:
            password_requirements["uppercase"] = not password_requirements["uppercase"]
            print("Uppercase requirement successfully {}".format("enabled" if password_requirements["uppercase"] else "disabled"))
        # modify lowercase
        elif option == 3:
            password_requirements["lowercase"] = not password_requirements["lowercase"]
            print("Lowercase requirement successfully {}".format("enabled" if password_requirements["lowercase"] else "disabled"))
        # modify digits
        elif option == 4:
            password_requirements["digits"] = not password_requirements["digits"]
            print("Digits requirement successfully {}".format("enabled" if password_requirements["digits"] else "disabled"))
        # modify special chars
        elif option == 5:
            password_requirements["special_characters"] = not password_requirements["special_characters"]
            print("Special characters requirement successfully {}".format("enabled" if password_requirements["special_characters"] else "disabled"))
        # modify minimum numbers
        elif option == 6:
            min_numbers = pyip.inputInt(min=0, prompt="Enter the minimum number of numbers: ")
            if min_numbers < 1:
                print("Warning: it is recommended to set the minimum length to at least 1 number for security reasons.")
                confirm = pyip.inputYesNo(prompt="Are you sure you want to continue with a shorter minimum length? ")
                if not confirm:
                    continue
            password_requirements["min_numbers"] = min_numbers
            print("Minimum number of numbers requirement successfully set to {}".format(min_numbers))
        # modify minimum special characters
        elif option == 7:
            min_special = pyip.inputInt(min=0, prompt="Enter the minimum number of special characters: ")
            if min_special < 1:
                print("Warning: it is recommended to set the minimum length to at least 1 special character for security reasons.")
                confirm = pyip.inputYesNo(prompt="Are you sure you want to continue with a shorter minimum length? ")
                if not confirm:
                    continue
            password_requirements["min_special"] = min_special
            print("Minimum number of special characters requirement successfully set to {}".format(min_special))
        # modify avoid ambiguous characters
        elif option == 8:
            avoid_ambiguous = pyip.inputYesNo(prompt="Avoid ambiguous characters (such as l, 1, I, O, 0)? ")
            password_requirements["avoid_ambiguous"] = avoid_ambiguous
            print("Avoid ambiguous characters requirement successfully {}".format("enabled" if password_requirements["avoid_ambiguous"] else "disabled"))

        # exit sub menu
        elif option == 9:
            break

        printDiv('-', int(WIDTH / 2))

    return password_requirements



"""
Finds weak passwords in the given data based on the password requirements.
Prints a report of the weak passwords, including the number of times each password appears and the data for each password.

Parameters:
data (list): A list of dictionaries containing login data, with each dictionary having a 'login_password' key.
password_requirements (dict): A dictionary of password requirements, with keys:
    'length' (int): The minimum length of the password.
    'uppercase' (bool): Whether the password must contain at least one uppercase character.
    'lowercase' (bool): Whether the password must contain at least one lowercase character.
    'digits' (bool): Whether the password must contain at least one digit.
    'special_characters' (bool): Whether the password must contain at least one special character.
    'min_numbers' (int): The minimum number of digits the password must contain.
    'min_special' (int): The minimum number of special characters the password must contain.
    'avoid_ambiguous' (bool): Whether the password must avoid ambiguous characters (such as l, 1, I, O, 0).
"""
def printWeakPasswordReport(data, password_requirements):

    weak_passwords_count = 0  # Will store the number of weak passwords found
    weak_passwords_dict = {}  # Dictionary to store the data for each password
    report = "" # Will store the report as a string
    rows_by_password = {}
    temp_string = ''

    # Get the password requirements
    min_length = password_requirements['length']
    require_uppercase = password_requirements['uppercase']
    require_lowercase = password_requirements['lowercase']
    require_digits = password_requirements['digits']
    require_special_characters = password_requirements['special_characters']
    min_numbers = password_requirements['min_numbers']
    min_special = password_requirements['min_special']
    avoid_ambiguous = password_requirements['avoid_ambiguous']
    
    # Iterate through the data
    for row in data:
        if "login_password" not in row or row["login_password"] is None:
            continue
        password = row['login_password']  
        length_ok = len(password) >= min_length  # Check if the password meets the minimum length requirement
        uppercase_ok = not require_uppercase or any(c.isupper() for c in password)  # Check if the password meets the uppercase requirement
        lowercase_ok = not require_lowercase or any(c.islower() for c in password)  # Check if the password meets the lowercase requirement
        digits_ok = not require_digits or (sum(c.isdigit() for c in password) >= min_numbers)  # Check if the password meets the digits requirement
        special_characters_ok = not require_special_characters or (sum(not c.isalnum() for c in password) >= min_special)  # Check if the password meets the special characters requirement
        ambiguous_ok = not avoid_ambiguous or all(c not in "Il1O0" for c in password)  # Check if the password avoids ambiguous characters
        
        if not (length_ok and uppercase_ok and lowercase_ok and digits_ok and special_characters_ok and ambiguous_ok):
            # If any of the requirements are not met, add the row to the dictionary of weak passwords
            if password not in weak_passwords_dict:
                weak_passwords_dict[password] = [row]
            else:
                weak_passwords_dict[password].append(row)
            weak_passwords_count += 1



    # Print and add the report to the string
    report += printHeader('Weak Password Report')

    temp_string = f"\nTotal number of weak passwords found: {weak_passwords_count}\n"
    report += temp_string   #add the previous to the report string 
    print(temp_string) #print the previous string     
    

    #display the header for the CSV fields
    report += printCSVHeader()


    # Iterate through the dictionary of weak passwords
    for password, rows in weak_passwords_dict.items():
        count = len(rows)  # Get the number of times the password appears

        # Initialize the rows_by_password dictionary for the current password
        rows_by_password = {}
        
        # add to string 
        report += '\n'
        temp_string = f"\n{password} was used {count} times"
        report += '\n'
        report += str(temp_string)
        print(temp_string)

        if all(row == rows[0] for row in rows):  # If all of the rows are the same, print the first row only

            temp_string = (rows[0])
            report += str(temp_string)
            print(temp_string)

            #save to string 
            report += str(rows[0])

        else:  # If the rows are not all the same, print them all and group the rows that are the same
            for row in rows:
                row_str = json.dumps(row)
                if row_str not in rows_by_password:
                    rows_by_password[row_str] = [row,1]
                else:
                    rows_by_password[row_str][1] += 1

            for row_str, [row, count] in rows_by_password.items():

                temp_string = f'{row} is used {count} times'
                report += '\n'
                report += temp_string
                print(temp_string)

    print()

    #return the string version of the report 
    return report


"""
Print a password reuse report based on the given data.

Parameters:
data (list): a list of dictionaries, where each dictionary represents a row of data with the following fields:
    - folder: the folder that the password belongs to
    - favorite: a boolean indicating whether the password is a favorite
    - type: the type of password
    - name: the name of the password
    - notes: any notes associated with the password
    - fields: any fields associated with the password
    - reprompt: any reprompts associated with the password
    - login_uri: the login URI for the password
    - login_username: the login username for the password
    - login_password: the login password for the password
    - login_totp: the login TOTP (Time-Based One-Time Password) for the password

    will return the report as a string 
"""
def printReusedReport(data):
    password_counts = {}  # Dictionary to store the password counts
    password_data = {}  # Dictionary to store the data for each password
    rows_by_password = {}
    temp_string = None
    report = ''

    # Iterate through the data
    for row in data:
        password = row['login_password']  # Get the login password for the current row
        
        if password in password_counts:  # If we have seen this password before, increment the count
            password_counts[password] += 1  #key: password, value: count 



        else:  # If we haven't seen this password before, add it to the dictionary with a count of 1
            password_counts[password] = 1
            password_data[password] = []  # Initialize an empty list to store the rows for each password
        
        password_data[password].append(row)  # Add the current row to the list for this password
    
    
    
    # Count the number of unique passwords that appear more than once
    num_unique_passwords = 0
    for count in password_counts.values():
        if count > 1:
            num_unique_passwords += 1
    

    # Print and add the string to the report string that will be returned 
    temp_string = printHeader('Password Reuse Report')
    report += temp_string
    
    temp_string = (f"\nTotal number of unique passwords reused: {num_unique_passwords}")
    report += temp_string
    print(temp_string)

    report += printCSVHeader()

    for password, count in password_counts.items():
        if count > 1:  # Only print passwords that appear more than once

            # Initialize the rows_by_password dictionary for the current password
            rows_by_password = {}
            
            temp_string = (f"\n{password} was used {count} times")
            report += '\n'
            report += '\n'
            report += temp_string
            print(temp_string)

            rows = password_data[password]  # Get the rows for this password

            if all(row == rows[0] for row in rows):  # If all of the rows are the same, print the first row only

                temp_string = (rows[0])
                report += str(temp_string)
                print(temp_string)


            else:  # If the rows are not all the same, print them all and group the rows that are the same
                for row in rows:
                    row_str = json.dumps(row)
                    if row_str not in rows_by_password:
                        rows_by_password[row_str] = [row,1]
                    else:
                        rows_by_password[row_str][1] += 1
                for row_str, [row, count] in rows_by_password.items():

                    temp_string = (f'{row} is used {count} times')
                    report += '\n'
                    report += temp_string
                    print(temp_string)

    print()

    #return the report as a string 
    return report



"""
Removes duplicate rows from the given data and prints a report of all the duplicate rows removed.
The report will include the row and how many of its duplicates were removed.

Parameters:
data (list): A list of dictionaries containing login data.

Returns:
list: A list of dictionaries containing login data with no duplicate rows.
"""
def removeDuplicateRows(data):
    # Create a new dictionary to store the unique rows
    unique_data = {}
    duplicate_count = 0  # Counter for the number of duplicates removed

    # Iterate over the data
    for row in data:
        # Create a tuple of the values from the row
        key = tuple(row.values())
        # Check if the tuple is not already in the dictionary
        if key not in unique_data:
            # Add the row to the dictionary
            unique_data[key] = row
        else:
            # If the tuple is already in the dictionary, increment the duplicate counter
            duplicate_count += 1

    # Print the report
    printHeader('Remove Password Duplicates Report')
    print(f"\nTotal number of duplicates removed: {duplicate_count}")
    
    #print the header for the fileds in the csv file 
    printCSVHeader()
    print()

    printed_rows = []  # List to store the rows that have been printed
    for row in data:
        # Create a tuple of the values from the row
        key = tuple(row.values())
        if key in unique_data and row not in printed_rows:  # Check if the tuple is in the unique_data dictionary and has not been printed yet
            count = data.count(row) - 1  # Calculate the number of duplicates removed
            if count > 0:  # Only print rows with duplicates removed
                
                #print(f"\n{row['login_password']} had {count} duplicates removed")
                print(f"{count} duplicates removed:")
                print(row)
                print()

                printed_rows.append(row)  # Add the row to the printed_rows list
    
    print()

    # Return the values of the dictionary (the rows) as a list
    #return list(unique_data.values())

    #return the values of the dictionary (the rows) as an updated dictionary 
    return unique_data.values()




"""
Display a menu to the user and request input.
Display the selected menu option.
"""
def menu():

    #read and return the csv file into a list 
    csvData, saveFileName = getCSVFile()
    #set password config settigns to default values
    defaultPasswordRequirements = {
    "length": PASSWORD_CHAR_LENGTH,
    "uppercase": True,
    "lowercase": True,
    "digits": True,
    "special_characters": True, 
    "min_numbers": 2,
    "min_special": 2,
    "avoid_ambiguous": False
}


    weakPasswordReport = None
    reusedPasswordReport = None 
    reportName = None

    #while the user does not enter the int 0 to exit, display main menu
    choice = -1 #initialzie choice to a non-valid int value
    while choice != 0:
        # Display the main menu options
        printMainMenuOptions()
        
        # Request input from the user
        choice = pyip.inputInt(prompt="\nEnter your choice: ", min = MIN_MENU_OPTIONS, max = MAX_MENU_OPTIONS)
    
        #REPORT - Reused passwords
        if(choice == 1):
            reusedPasswordReport = printReusedReport(csvData)
        
        #TOOL - Save reused password report to txt file 
        elif(choice == 2):
            if reusedPasswordReport is None:
                print("Error: Please generate Reused Password Report first by selecting choice 1")
                continue
            reportName = 'reused' + WEAK_PASS_TXT_FILE_NAME
            save_to_txt(reusedPasswordReport, get_save_file_name(reportName))

        #REPORT - Weak Passwords
        elif(choice == 3):
            weakPasswordReport = printWeakPasswordReport(csvData, defaultPasswordRequirements)

        #TOOL - Save weak password report to txt file 
        elif(choice == 4):
            if weakPasswordReport is None:
                print("Error: Please generate Weak Password Report first by selecting choice 2")
                continue

            reportName = 'weak' + WEAK_PASS_TXT_FILE_NAME
            save_to_txt(weakPasswordReport, get_save_file_name(reportName))

        #TOOL - Remove Duplicates
        elif(choice == 5):
            csvData = removeDuplicateRows(csvData)
        
        #TOOL - Save the file 
        elif(choice == 6):
            writeCSVFile(csvData, saveFileName)
        

        #TOOL - Save the file as new 
        elif(choice == 7):
            saveFileName = get_save_file_name(SAVE_FILE_NAME)
            writeCSVFile(csvData, saveFileName)


        #exit the program 
        elif(choice == 8):
            #print msg to user of successfull program termination
            print('\n%s\n' % (' PROGRAM TERMINATED SUCCESSFULLY '.center(50, '*')))            # Exit the program
            sys.exit()

        #SETTINGS - Configure min password requirements 
        elif(choice == 9):
            defaultPasswordRequirements = configurePasswordRequirements(defaultPasswordRequirements)




#acts as the point of execution for any program.
def main():

    #print the header for the programs name 
    printHeader(PROGRAM_NAME)

    #display the menu for the program 
    menu()








   
#--------------------------- Code  -----------------------------------


#acts as the point of execution for any program.
main()
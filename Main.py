# ------------------------------------------------------------------------ #
# Title: Main
# Description: Working with Modules
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# JBrecht,9.1.2020,Revised script to complete assignment
# ---------------------------------------------------------- #

if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

lstTable = []

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of employee objects when script starts
# lstOfObjects = Fp.read_data_from_file("EmployeeData.txt")  # get file data
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))

# Show user a menu of options
while (True):
    Eio.print_menu_items()  # Shows menu

    # Get user's menu option choice
    strChoice = Eio.input_menu_options("Which option would you like to perform? [1 to 4] - ")  # message
    while strChoice not in str("1, 2, 3, 4"):
        strChoice = Eio.input_menu_options("Entry should be 1, 2, 3, or 4 - ")  # message

    # Show user current data in the list of employee objects
    if strChoice.strip() == '1':  # Show current data in list
        Eio.print_current_list_items(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    # Let user add data to the list of employee objects
    elif strChoice.strip() == '2':  # Add a new employee
        lstTable.append(Eio.input_employee_data())
        continue  # to show the menu

    # let user save current data to file
    elif strChoice == '3':  # Save Data to File
        Fp.save_data_to_file("EmployeeData.txt", lstTable)
        print("Save successful!")
        continue  # to show the menu

    # Let user exit program
    print("\nGoodbye!")
    break  # and Exit

# Main Body of Script  ---------------------------------------------------- #

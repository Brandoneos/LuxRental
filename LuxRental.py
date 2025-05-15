###############################################################################
# Presentationtier
# This module defines the application interface for 
# interacting with the Rental application.
###############################################################################
import json
import psycopg2
import objecttier
import menu_action as menu
##################################################################  
#
# setup_connection: 
#
# Set create a postgres conection with LuxRental.db
#
def setup_connection():
    with open('./config.json', 'r') as config_file:
        config = json.load(config_file)

    return psycopg2.connect(database=config["database"],
                            user=config["user"],
                            host=config["host"],
                            password=config["password"],
                            port=config["port"])

##################################################################  
#
# print statistics
#
# print statistics of Chicago Lobbyist Database
#
def printStatistics(dbConn):
    
    # get stats val
    num_managers = objecttier.num_managers(dbConn)
    num_drivers = objecttier.num_drivers(dbConn)
    num_clients = objecttier.num_clients(dbConn)
    num_cars = objecttier.num_cars(dbConn)
    num_models = objecttier.num_models(dbConn)

    # print stats
    print()
    print(f"General Statistics:")
    print(f"  Number of Managers: {num_managers:,}")
    print(f"  Number of Drivers: {num_drivers:,}") 
    print(f"  Number of Clients: {num_clients:,}")
    print(f"  Number of Cars: {num_cars:,}")
    print(f"  Number of Models: {num_models:,}")
    print()
    
def printFirstMenu():
    print("First Menu:")
    print("# 1: Register")
    print("# 2: Login")

def printSecondMenu(user):
    print(f"Second Menu for: {user}")
    if(user == "Manager"):
        print("# 1: Add Car")
        print("# 2: Add Car Model")
        print("# 3: Delete Car")
        print("# 4: Delete Car Model")
        print("# 5: Insert Driver")
        print("# 6: Remove Driver")
        print("# 7: Print Top-K Clients based on # of Rents")
        print("# 8: Print All Car Models and their # of Rents")
        print("# 9: Print All Drivers and their # of Rents and Ratings")
        print("# 10: (#7 Manager) Using C1, C2")
    elif(user == "Driver"):
        print("# 1: Change Address")
        print("# 2: List All Car Models")
        print("# 3: Declare Own Car Model")
    elif(user == "Client"):
        print("# 1: See Available Car Models On Date D")
        print("# 2: Book a Rent with Available Car Model On Date")
        print("# 3: List all Rents Currently Booked by Client")#with car model and assigned driver
        print("# 4: Write Review to Connected Driver")#Driver should have been assigned to a rent booked by client, otherwise not allowed
    else:
        print("Error, User is Not Within System")
    
    # print("# 2: Manager")

##################################################################  
#
# handle_register, always returns 1
#

def handle_register(dbConn):
    print("Register as")
    print("# 1: Manager")
    print("# 2: Client")

    option = input("Enter command 1-2: ")
    # Register as Manager
    if(option == "1"):
        print()
        menu.handle_register_manager(dbConn)
    # Register as Client
    elif(option == "2"):
        print()
        menu.handle_register_client(dbConn)
    return 1

##################################################################  
#
# handle_login
#

def handle_login(dbConn):
    print("Login as")
    print("# 1: Manager")
    print("# 2: Driver")
    print("# 3: Client")

    option = input("Enter command 1-3: ")
    # login as Manager
    if(option == "1"):
        print()
        s,ssn = menu.handle_login_manager(dbConn)
        if(s == 1): #successful
            return 2,"Manager",ssn
        else: #unsuccessful, stay in stage 1(Register/login)
            return 1,"None","None"
        
    # login as Driver
    elif(option == "2"):
        print()
        s,name = menu.handle_login_driver(dbConn)
        if(s == 1): #successful
            return 2,"Driver",name
        else: #unsuccessful, stay in stage 1(Register/login)
            return 1,"None","None"
    elif(option == "3"):
        print()
        s,email = menu.handle_login_client(dbConn)
        if(s == 1): #successful
            return 2,"Client",email
        else: #unsuccessful, stay in stage 1(Register/login)
            return 1,"None","None"
    else:
        return 1,"None","None"

##################################################################  
#
# inputCommand
#

def inputCommand(user):
    if(user == "Manager"):
        command = input("Please enter a command (1-10, x to exit, menu for options): ")
    elif(user == "Driver"):
        command = input("Please enter a command (1-3, x to exit, menu for options): ")
    elif(user == "Client"):
        command = input("Please enter a command (1-4, x to exit, menu for options): ")
    else:
        print("Error, User is Not Within System 2")
    return command

##################################################################  
#
# checkCommand
#

def checkCommand(user,command,userKey):
    if(user == "Manager"):
        if(command == "1"):#add car
            print()
            menu.handle_add_car(dbConn)
        elif(command == "2"):#add car model
            print()
            menu.handle_add_model(dbConn)
        elif(command == "3"):#delete car
            print()
            menu.handle_delete_car(dbConn)
        elif(command == "4"):#delete car model
            print()
            menu.handle_delete_model(dbConn)
        elif(command == "5"):#insert driver
            print()
            menu.handle_register_driver(dbConn)
        elif(command == "6"):#remove driver
            print()
            menu.handle_remove_driver(dbConn)
        elif(command == "7"):#Print Top-K Clients based on # of Rents
            print()
            menu.handle_top_k_clients(dbConn)
        elif(command == "8"):#Print All Car Models and their # of Rents
            print()
            menu.handle_view_model_usage(dbConn)
        elif(command == "9"):#Print All Drivers and their # of Rents and Ratings
            print()
            menu.handle_driver_usage_stats(dbConn)
        elif(command == "10"):# (#7 Manager) Using C1, C2
            print()
            menu.handle_query_clients_by_cities(dbConn)
        elif(command == "menu"):
            printSecondMenu(user)
        else:
            print("**Error, unknown command, try again...")
        
    elif(user == "Driver"):
        if(command == "1"):
            print()
            menu.handle_update_driver_address(dbConn)
        elif(command == "2"):
            print()
            menu.handle_view_all_car_model(dbConn)
        elif(command == "3"):
            print()
            menu.handle_add_driver_model(dbConn)
        elif(command == "menu"):
            printSecondMenu(user)
        else:
            print("**Error, unknown command, try again...")
    elif(user == "Client"):
        if(command == "1"):
            print()
            menu.handle_view_available_car_model(dbConn)
        elif(command == "2"):
            print()
            menu.handle_book_rent(dbConn)
        elif(command == "3"):
            print()
            menu.handle_view_all_rent_detail(dbConn)
        elif(command == "4"):
            print()
            menu.handle_add_review(dbConn,userKey)
        elif(command == "menu"):
            printSecondMenu(user)
        else:
            print("**Error, unknown command, try again...")
    else:
        print("Error, User is Not Within System 2")

##################################################################  
#
# main
#

# connect script to database
dbConn = setup_connection()
stage = 1
print('** Welcome to LuxRental **')
# print stats
printStatistics(dbConn)

# create user interface
printFirstMenu()
command = input("Please enter a command (1 or 2, x to exit, menu for options): ")
user = "None"
user1 = "None"
userKey = "None"
while (command != "x" and  command != "X" and stage == 1):
    # 1 Register
    if command == "1":
        print()
        # menu.handle_register_manager(dbConn)
        handle_register(dbConn)
    # 2 Manager Login 
    elif command == "2":
        print()
        # menu.handle_login_manager(dbConn)
        stage, user1, userKey = handle_login(dbConn)
    # menu. print all possible menu options. 
    elif command == "menu":
        printFirstMenu()
        
    # for every other input repeat until user inputs 'x' or 'X' to quit program
    else:
        print("**Error, unknown command, try again...")
    
    if(stage == 1):
        print()
        command = input("Please enter a command (1 or 2, x to exit, menu for options): ")

#After the User has logged in as a Manager,Driver, or Client
if(command != "x" and command != "X"):
    printSecondMenu(user1)
    # "Please enter a command (1 or 2, x to exit, menu for options): "
    command = inputCommand(user1)

while(command != "x" and  command != "X" and stage == 2):
    # print("in 2nd while")
    checkCommand(user1,command,userKey)
    print()
    command = inputCommand(user1)
# close connection to database
dbConn.close()
#
# done
#

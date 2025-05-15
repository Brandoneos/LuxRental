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
# insert_year: 
#
# Register an existing lobbyist for a new year.
#
def insert_year(dbConn):
    year = input("Enter year: ")
    ID = input("Enter the lobbyist ID: ")

    # validate ID
    Lobbyist_ = objecttier.get_lobbyist_details(dbConn,ID)
    if Lobbyist_ == None:
        print()
        print("No lobbyist with that ID was found.")
        return

    # perform insert action
    successful = objecttier.add_lobbyist_year(dbConn, ID, year)

    if successful == True:
        print()
        print("Lobbyist successfully registered.")
    else:
        print()
        print("No lobbyist with that ID was found.")
    
##################################################################  
#
# print_LobbyistClients: 
#
# print all properties of a LobbyistClients object
#
def print_LobbyistClients(LobbyistClient_):
    # print all properties LobbyistClient object

    print(LobbyistClient_.First_Name + " " + LobbyistClient_.Last_Name)
    print(f"  Phone: {LobbyistClient_.Phone}")
    print(f"  Total Compensation: ${LobbyistClient_.Total_Compensation:,.2f}")
    print("  Clients: ", end="")
    for client in LobbyistClient_.Clients:
        print(client, end=", ")
    print()
    

##################################################################  
#
# retrieve_top_N_Lobbyist: 
#
# Given a year, find the top N lobbyists based on their total compensation for that year
#
def retrieve_top_N_Lobbyist(dbConn):
    # obtain and validate number of lobbyist to return
    try:
        num = int(input("Enter the value of N: "))
    # catch Value error    
    except Exception as err:
        print("Please enter a positive value for N...")
        return
    # validate for -ve numbers
    if num < 0:
        print("Please enter a positive value for N...")
        return 
    
    # obtain year to query on
    year = input("Enter the year: ")

    top_Lobbyists = objecttier.get_top_N_lobbyists(dbConn, num, year)

    if(len(top_Lobbyists) == 0):
        return
    
    # print Lobbyists
    i = 1
    print()
    for lobbyists in top_Lobbyists:
        print(str(i) + " .", end=" ")
        print_LobbyistClients(lobbyists)
        i=i+1
    
##################################################################  
#
# print_Lobbyist: 
#
# prints all properties of a LobbyistDetails object . 
#
def print_Lobbyist(Lobbyist_):

    print()
    print(str(Lobbyist_.Lobbyist_ID)  + " :")
    print("  Full Name: " + Lobbyist_.Salutation  + " " + Lobbyist_.First_Name + " " + Lobbyist_.Middle_Initial+ " "+ Lobbyist_.Last_Name + " " + Lobbyist_.Suffix)
    print("  Address: " + Lobbyist_.Address_1 + " " + Lobbyist_.Address_2 + " , " + Lobbyist_.City + " , ", end="")
    print(Lobbyist_.State_Initial + " " + str(Lobbyist_.Zip_Code) + " " + Lobbyist_.Country)
    print("  Email: " + Lobbyist_.Email)
    print("  Phone: " + Lobbyist_.Phone)
    print("  Fax: "+ Lobbyist_.Fax)
    print("  Years Registered: ", end="")
    for year in Lobbyist_.Years_Registered:
        print(year, end= ", ")
    print()
    print("  Employers: ", end="")
    for employer in Lobbyist_.Employers:
        print(employer, end=", ")
    print()
    print("  Total Compensation: $", end="")
    print(f"{Lobbyist_.Total_Compensation:,.2f}")

##################################################################  
#
# retrieve_Lobbyists_by_id 
#
# Given the user input of an ID, creates a LobbyistDetails object that matches ID. 
#
def retrieve_Lobbyists_by_id(dbConn):
    # obtain Lobbyist ID from user
    ID = input("Enter Lobbyist ID: ")

    # validate ID
    if len(ID) == 0:
        print("\nNo lobbyist with that ID was found.")
        return
    
    # create Lobbyist object
    Lobbyist_ = objecttier.get_lobbyist_details(dbConn, ID)
    
    # validate result
    if Lobbyist_ == None:
        print("\nNo lobbyist with that ID was found.")
        return
    
    # print result
    print_Lobbyist(Lobbyist_)
    
##################################################################  
#
# retrieve_Lobbyists_by_name 
#
# Given the user input of a name, return all lobbyists that match that name. 
# Funtion allows first name or last name matches,
# and the user can enter patterns using the SQL wildcards _ and %.
#
def retrieve_Lobbyists_by_name(dbConn):
    # obtain name from user
    name = input("Enter lobbyist name (first or last, wildcards _ and % supported): ")

    # create a list of Lobbyist objects with objecttier
    Lobbyists_ = objecttier.get_lobbyists(dbConn, name)

    # validate result
    if Lobbyists_ == None:
        print(f"Number of lobbyists found: 0")
        return
    
    # print result
    print()
    print(f"Number of lobbyists found: {len(Lobbyists_)}\n")

    # validate length of query, if length greater than 100, return
    if len(Lobbyists_) > 100:
        print("There are too many lobbyists to display, please narrow your search and try again...")
        return
    
    for row in Lobbyists_:
        print(f"{row.Lobbyist_ID} : {row.First_Name} {row.Last_Name} Phone: {row.Phone}")


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
    
def printMenu():
    print("Menu:")
    print("# 1: Register Manager")
    print("# 2: Manager Login")
    print("# 3 Add Car (Manager)")
    print("# 4 Add Model (Manager)")
    print("# 5 Delete Car (Manager)")
    print("# 6 Delete Car Model (Manager)")
    print("# 7  Register Driver (Manager)")
    print("# 8  Remove Driver (Manager)")
    print("# 9 Update Driver Address (Driver)")
    print("# 10 Print all car model (Driver)")
    print("# 11 Top-K Clients (Manager)")
    print("# 12 Add Drivable Model (Driver)")
    print("# 13 Register Client (Client)")
    print("# 14 Book Rent Client (Client)")
    print("# 15 Print all Available Car Model (Client)")
    print("# 16 Print All Bookings (Client)")
    print("# 17: Print All Car Models and their # of Rents (Manager)")
    print("# 18: Print All Drivers and their # of Rents and Ratings (Manager)")
    print("# 19: Query Clients by Cities (Need better description) (Manager)")
    print("# 20: Add Review to Driver (Client)")

##################################################################  
#
# main
#

# connect script to database
dbConn = setup_connection()

print('** Welcome to LuxRental **')
# print stats
printStatistics(dbConn)
stage = 1
# create user interface
printMenu()
command = input("Please enter a command (1-15, x to exit, menu for options): ")

defaultClient = "client1.com"

while (command != "x" and  command != "X"):
    # 1 Register Manager 
    if command == "1":
        print()
        menu.handle_register_manager(dbConn)

    # 2 Manager Login 
    elif command == "2":
        print()
        menu.handle_login_manager(dbConn)

    # 3 Add Car (Manager)
    elif command == "3":
        print()
        menu.handle_add_car(dbConn)

    # 4 Add Car Model (Manager)
    elif command == "4":
        print()
        menu.handle_add_model(dbConn)

    # 5 Delete Car (Manager)
    elif command == "5":
        print()
        menu.handle_delete_car(dbConn)

    # 6 Delete Car Model (Manager)
    elif command == "6":
        print()
        menu.handle_delete_model(dbConn)

    # 7  Register Driver (Manager)
    elif command == "7":
        print()
        menu.handle_register_driver(dbConn)
        
    # 8 Remove Driver (Manager)
    elif command == "8":
        print()
        menu.handle_remove_driver(dbConn)
        
    # 9 Update Driver Address (Driver)
    elif command == "9":
        print()
        menu.handle_update_driver_address(dbConn)

    # 10 Print all car model (Driver)
    elif command == "10":
        print()
        menu.handle_view_all_car_model(dbConn)

    # 11 Top-K Clients (Manager)
    elif command == "11":
        print()
        menu.handle_top_k_clients(dbConn)

    # 12 Add Drivable Model (Driver)"
    elif command == "12":
        print()
        menu.handle_add_driver_model(dbConn)

    # 13 Register Client (Client)
    elif command == "13":
        print()
        menu.handle_register_client(dbConn)
    
    # 14 Book Rent Client (Client)
    elif command == "14":
        print()
        menu.handle_book_rent(dbConn)

    # 15 Print all available car model (Client)
    elif command == "15":
        print()
        menu.handle_view_available_car_model(dbConn)
    
    # 16 Print All Bookings (Client)
    elif command == "16":
        print()
        menu.handle_view_all_rent_detail(dbConn, defaultClient)
    
    elif command == "17":
        print()
        menu.handle_view_model_usage(dbConn)
    
    elif command == "18":
        print()
        menu.handle_driver_usage_stats(dbConn)

    elif command == "19":
        print()
        menu.handle_query_clients_by_cities(dbConn)

    elif command == "20":
        print()
        menu.handle_add_review(dbConn, defaultClient)

    # menu. print all possible menu options. 
    elif command == "menu":
        printMenu()
        

    # for every other input repeat until user inputs 'x' or 'X' to quit program
    else:
        print("**Error, unknown command, try again...")
    print()
    command = input("Please enter a command (1-25, x to exit, menu for options): ")

# close connection to database
dbConn.close()
#
# done
#

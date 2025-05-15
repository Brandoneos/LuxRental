import objecttier
from datetime import datetime
##################################################################  
#
# handle_register_manager: 
#
# Function to register a new manager in database
#
def handle_register_manager(dbConn):
    name = input("Enter your Name: ").lower()
    email = input("Enter your email: ").lower()
    ssn = input("Enter the ssn (9 digits required xxx-xx-xxxx): ")
    
    # validate ssn
    if len(ssn) != 11:
        print("Invalid ssn format!")
        return
    
    # validate format
    _ssn = ssn.replace('-', '')

    if not _ssn.isdigit():
        print("Invalid ssn format! SSN must contain only digits.")
        return

    Manager_ = objecttier.get_manager_info(dbConn,_ssn)
    if Manager_ != None:
        print(f"\nManager with name \"{Manager_.Name}\" already exists!")
        return

    # perform insert action
    successful = objecttier.register_manager(dbConn, name, _ssn, email)

    if successful == True:
        print("Manager registered successfully.")
    else:
        print()
        print("Failed to add manager.")


##################################################################  
#
# handle_login_manager: 
#
# Function to login a registered manager, 
# returns 1 if successful login
#         0 if unsuccessful
#
def handle_login_manager(dbConn):
    ssn = input("Enter ssn (9 digits required xxx-xx-xxxx): ")

    # validate ssn
    if len(ssn) != 11:
        print("Invalid ssn format!")
        return 0

    # validate format
    _ssn = ssn.replace('-', '')

    if not _ssn.isdigit():
        print("Invalid ssn format! SSN must contain only digits.")
        return 0
    
    Manager_ = objecttier.get_manager_info(dbConn,_ssn)
    if Manager_ != None:
        print("login successful as manager")
        print(f"\n \t\t\tWelcome back {Manager_.Name}!")
        return (1, ssn)  # Success: return tuple (status, ssn)
    else:
        print("login failed")
        print("Unable to find manager with credentials")
        return (0, None)  # Failure: return tuple (status, None)
    
##################################################################  
#
# handle_login_driver: 
#
# Function to login a driver using name
# returns 1 if successful login
#         0 if unsuccessful
#
def handle_login_driver(dbConn):
    driverName = input("Enter name: ").lower()

    Driver_ = objecttier.get_driver_info(dbConn,driverName)
    if Driver_ != None:
        print("login as driver successful")
        print(f"\n \t\t\tWelcome back {Driver_.Name}")
        return (1, driverName)  # Success: (status, name)
    else:
        print("login failed")
        print(f"Unable to find driver with name \"{driverName}\"")
        return (0, None)  # Failure: (status, None)


##################################################################  
#
# handle_register_client: 
#
# Function to register a new client in database
#
def handle_register_client(dbConn):
    name = input("Enter your Name: ").lower()
    email = input("Enter your email: ").lower()

    # validate client
    Client_ = objecttier.get_client_info(dbConn,email)
    if Client_ != None:
        print(f"\nClient with email \"{Client_.Email}\" already exists!")
        return
    
    # perform insert action, Register Client before anything else
    successful = objecttier.register_client(dbConn, email, name)
    if successful == True:
        print()
        print("Client temporarily registered.")
    else:
        print()
        print("Failed to add client.")
        return
    

    # add client address
    print()
    response = "y"
    count = 0
    while(response == "y"):
        # add new client address
        count += handle_add_client_address(dbConn, email)
        response = input("\nWould you like to add another address? "
                        "\nEnter y to continue or n to skip: ").lower()
    
    if(count == 0):
        print("No valid address added!")
        print("All clients are required to have at least one valid address.")
        print("Client will be removed from database.")
        if( handle_remove_client(dbConn, email) ):
            print(f"Client {name} has been deleted!")
            return
        else:
            print("REMOVE CLIENT FAILED!")
            return
    else:
        # at least one valid address was registered
        print(f"Number of addresses added to client: {count}")

    # add credit card
    print()
    response = "y"
    count = 0
    while(response == "y"):
        # add new credit card
        count += handle_add_creditcard(dbConn, email)
        response = input("\nWould you like to add another credit card? "
                        "\nEnter y to continue or n to skip: ").lower()
    
    if(count == 0):
        print("No valid credit card added!")
        print("All clients are required to have at least one valid credit card.")
        print("Client will be removed from database.")
        if( handle_remove_client(dbConn, email) ):
            print(f"Client {name} has been deleted!")
            return
        else:
            print("REMOVE CLIENT FAILED!")
            return
    else:
        # at least one valid credit card was registered
        print(f"Number of credit cards added to client: {count}")

    # Client registered with valid address(es) and credit card(s)
    print("\nSuccess!!!"
          "\nAll levels of registration complete!")
    return


##################################################################  
#
# handle_remove_client_address: 
#
# Function to remove all client_address using email
# returns 1 if successful
#         0 if unsuccessful
#
def handle_remove_client_address(dbConn, email):
    # validate client
    Client_ = objecttier.get_client_info(dbConn, email)
    if(Client_ == None):
        print(f"No client found with email \"{email}\"!")
        return
    
    # perform delete operation
    successful = objecttier.remove_client_address(dbConn, email)
    return successful

##################################################################  
#
# handle_remove_client: 
#
# Function to remove a client using email
# returns 1 if successful
#         0 if unsuccessful
#
def handle_remove_client(dbConn, email):
    # validate client
    Client_ = objecttier.get_client_info(dbConn, email)
    if(Client_ == None):
        print(f"No client found with email \"{email}\"!")
        return
    
    # remove all client_address
    if (handle_remove_client_address(dbConn, email)):
        print("All client addresses removed")
    else:
        print("FAILED TO DELETE CLIENT ADDRESSES!")
    # perform delete operation
    successful = objecttier.remove_client(dbConn, email)
    return successful

##################################################################  
#
# handle_login_client: 
#
# Function to login a client using email
# returns 1 if successful login
#         0 if unsuccessful
#
def handle_login_client(dbConn):
    clientEmail = input("Enter email: ").lower()

    
    Client_ = objecttier.get_client_info(dbConn,clientEmail)
    if Client_ != None:
        print("login as client successful")
        print(f"\n \t\t\tWelcome back {Client_.Name}!")
        return (1, clientEmail)  # Success: (status, email)
    else:
        print("login failed")
        print("Unable to find client with email")
        return (0, None)  # Failure: (status, None)


#####################################################################
# helper function to validate address id
# return: 1 and address info if address exist, else
#         0 and address info
#
def validate_address(dbConn):
    road = input("Enter street/road name: ").lower()
    number = input("Enter street number: ")
    city = input("Enter city: ").lower()

    Address_ = objecttier.get_address_info(dbConn, road, number, city)
    ## No address found -> 0
    if Address_ == None:
        return (0, road, number, city)
    
    ## valid address found -> 1
    return (1, road, number, city)

#####################################################################
# helper function to validate driver name
# return: 1 and address info if address exist, else
#         0 and address info
#
def validate_driver(dbConn, email):

    driverName = input("Enter Driver Name to send Review: ").lower()

    Driver_ = objecttier.get_driver_client_info(dbConn, email, driverName)
    ## No driver found -> 0
    if Driver_ == None:
        return (0, driverName)
    
    ## driver found -> 1
    return (1, driverName)

#####################################################################
# helper function to add address
# return: (1, road, number, city) if address added, else
#         (0, road, number, city)
#
def add_address_helper(dbConn, road, number, city):
    # perform insert action
    successful = objecttier.add_address(dbConn, road, number, city)

    if successful == True:
        print("Address added successfully.")
        # address added
        return (1, road, number, city)
    else:
        print()
        print("Failed to add address.")
    # Failed to add address
    return (0, road, number, city)

##################################################################  
#
# handle_add_address: 
#
# Function to add a new address in database
#   returns -> (flag, road, number, city)
#
def handle_add_address(dbConn):
    # validate address returns -> (bool, road, number, city)
    (valid, road, number, city) =  validate_address(dbConn)

    if valid:
        print(f"\n\"{road} {number} {city}\" already exists in address!")
        # address exist
        return (-1, road, number, city)
    
    # helper function to perform insert action
    return add_address_helper(dbConn, road, number, city)


##################################################################  
#
# handle_add_review: 
#
# Function to add a new review to driver 
# iff driver has been assigned to client for at least one rent
#   returns -> flag
#
def handle_add_review(dbConn, userKey):
    #userKey for client is email
    # 
    
    # provide rent details
    request = input("Enter y to view booking history with" \
                    " driver names or c to continue: ").lower()
    if(request == "y"):
        handle_view_all_rent_detail(dbConn, userKey)
    
    # get driver name
    (valid, driverName) =  validate_driver(dbConn, userKey)

    if not valid:
        # Driver doesn't exist, or wasn't booked by client
        print(f"No matching booking with driver \"{driverName}\".")
        return -1
    
    # Driver exists and is booked by client
    return handle_add_review_helper(dbConn,userKey,driverName)
    
        


##################################################################  
#
# handle_add_review_helper: 
#
# helper Function to add a new review if driver exists 
# and has been assigned to client in database
#   returns -> flag
#
def handle_add_review_helper(dbConn, userKey, driverName):
    #userKey for client is email

    # helper for messge preveiw
    def message_preview(driverName, message):
        print("\n" + "-" * 70)
        print(f"\t\t\tReview Message")
        print("-" * 70)
        print(f"To: {driverName}")
        print()
        print(f"Message: \n{message}")
        print()
        print("-" * 70)
        print()
        print("\t\t\t\t\t\t\t\tSent!")
        print("-" * 70)
        return
    
    #Assuming Driver exists and is booked by client
    message = input("Enter Message For Review: ")
    rating = input("Enter Rating For Review(0-5): ")

    # validate rating
    if not rating.isdigit():
        print("Invalid rating! Must be a digit")
        return -1
    
    # validate rating contraint
    rating_ = int(rating)
    if (rating_ < 0 or rating_ > 5):
        print("Invalid rating! Must be an integer between 0 and 5")
        return -1
    
    successful = objecttier.add_review(dbConn, 
                                       message, rating_,
                                       driverName, userKey)

    if successful == True:
        message_preview(driverName, message)
        # review added
        return 1
    else:
        print()
        print("Failed to add Review")
        return 0


##################################################################  
#
# handle_add_client_address: 
#
# Function to add a new client address in database
#   returns -> 1 if client address was added sucessfully, else
#              0
#
def handle_add_client_address(dbConn, email):
    # validate address returns -> (bool, road, number, city)
    (valid, road, number, city) =  validate_address(dbConn)

    # All Addresses must exist in Address table -> add new client address
    if not valid:
        add_address_helper(dbConn, road, number, city)

    # perform insert into client_address
    successful = objecttier.add_client_address(dbConn, email, road, number, city)

    if successful == True:
        print("Client address added successfully.")
        # address added
        return 1
    else:
        print()
        print("Failed to add client address.")
    # Failed to add address
    return 0


#####################################################################
# helper function to validate payment address 
# return: 1 ->  payment address fails UNIQUE constraint (exist)
#         0 -> payment address passes UNIQUE constraint (does not exist)
#
def validate_payment_address(dbConn, road, number, city):
    # get payment address count
    return objecttier.get_payment_address_count(dbConn, road, number, city)
##################################################################  
#
# handle_add_creditcard: 
#
# Function to add a new credit card in database
#   returns -> 1 if card was added succeddfully, else
#              0
#
def handle_add_creditcard(dbConn, email):
    # validate card
    cardnum = input("Enter Credit Card Number: ")

    CreditCard_ = objecttier.get_creditcard_info(dbConn, cardnum)
    
    # payment address
    if CreditCard_ != None:
        print("Illegal! Credit card is owned by a client!")
        return 0
    
    # credit card is new, add card
    (valid, road, number, city) =  validate_address(dbConn)

    # validate address
    if not valid:
        # add new address
        add_address_helper(dbConn, road, number, city)
    
    # check unique constraint
    is_unique = validate_payment_address(dbConn, road, number, city)
    if(is_unique == -1):
        print("AN EXCEPTION OCCURED IN COUNT PAYMENT ADDRESS!")
        return 0
    elif(is_unique == 1):
        # payment address exist and fails unique constraint
        print("Illegal! Payment Address belongs to a differernt credit card")
        print("Aborting")
        return 0
    # payment address passes unique constraint

    # perform insert action
    successful = objecttier.add_credit_card(dbConn, cardnum, email, road, number, city)

    if successful == True:
        print("Credit card added successfully.")
        # credit card added
        return 1
    else:
        print()
        print("Failed to add Credit card.")
    # Failed to add credit card
    return 0


##################################################################  
#
# handle_update_driver_address: 
#
# Function to update driver address in database
#
def handle_update_driver_address(dbConn):
    # validate driver 
    name = input("Enter name: ").lower()
    Driver_ = objecttier.get_driver_info(dbConn, name)
    if Driver_ == None:
        print(f"Illegal! No matching driver found.")
        return
    
    # validate address returns -> (bool, road, number, city)
    (valid, road, number, city) =  validate_address(dbConn)

    if not valid:
        print(f"Address registration required!")
        # add address to Address table (road,number,city) -> bool
        register = input("Would you like to register this address? "
                         f"\n {road} {number} {city}"
                         "\nEnter y to confirm or n to abort: ").lower()
        if register != "y":
            print("Aborted!")
            return
        # continue logic: add address
        (valid, _, _, _) = add_address_helper(dbConn, road, number, city)    
        # valid = 1 | 0
        if valid == 0:
            return

    # confirm update
    print(f"\n Warning! \"{Driver_.Road} {Driver_.Number} {Driver_.City}\" "
          f"will be updated to \"{road} {number} {city}\" in database!")
    confirm = input("Enter y to confirm or n to abort: ").lower()
    if confirm != "y":
        print("Aborted!")
        return
    
    # perform update action
    successful = objecttier.update_driver_address(dbConn, road, number, city, name)

    if successful == True:
        print("Address updated successfully.")
    else:
        print()
        print("Failed to add address.")


##################################################################
#
# handle_register_driver: 
#
# Function to register a new driver in database
#
def handle_register_driver(dbConn):
    # validate driver name
    name = input("Enter driver name: ").lower()
    Driver_ = objecttier.get_driver_info(dbConn, name)
    if Driver_ != None:
        print(f"Driver name \"{Driver_.Name}\" already exists!")
        return
    
    # add address to Address table (road,number,city) -> bool
    (valid, road, number, city) =  handle_add_address(dbConn)

    # valid = -1 | 1 | 0
    if valid == 0:
        print("Failed to add driver! A valid address is required.")
        return

    # perform insert action
    successful = objecttier.register_driver(dbConn, 
                                            name, 
                                            road, number, city)

    if successful == True:
        print("Driver registered successfully.")
    else:
        print()
        print("Failed to add driver.")


##################################################################  
#
# handle_remove_driver: 
#
# Function to remove a driver from database
#
def handle_remove_driver(dbConn):
    # user input driver name
    name = input("Enter name of driver to be removed: ").lower()

    # validate result
    Driver_ = objecttier.get_driver_info(dbConn, name)
    if Driver_ == None:
        print(f"Illegal! No matching driver found.")
        return
    
    # confirm deletion
    print(f"\n\"{Driver_.Name}\" will be deleted from database!")
    # Remove Driver -> Remove Rent and Drives and Review
    print(f"Here's a list of the Reviews for Driver Name: {Driver_.Name}")
    handle_view_certain_driver_reviews(dbConn, Driver_.Name)
    print(f"Here's a list of the car models declared by Driver Name: {Driver_.Name}")#Drives Table
    handle_view_certain_drives2(dbConn, Driver_.Name)
    print(f"Here's a list of the Rents with Driver Name: {Driver_.Name}") #Rent Table
    handle_view_certain_rents2(dbConn, Driver_.Name)
    confirm = input("Enter y to confirm or n to abort: ").lower()
    if confirm != "y":
        print("Aborted!")
        return
    
    # delete reviews 

    successful3  = objecttier.delete_certain_driver_reviews(dbConn, Driver_.Name)

    if successful3 == True:
        print("All Reviews associated with DriverName deleted successfully.")
    else:
        print()
        print("Failed to delete Reviews.")


    #delete rents
    successful2  = objecttier.delete_certain_rents2(dbConn, Driver_.Name)

    if successful2 == True:
        print("All Rents associated with CarId deleted successfully.")
    else:
        print()
        print("Failed to delete Rents.")
    


    #delete Drives entries
    successful1  = objecttier.delete_certain_drives2(dbConn, Driver_.Name)

    if successful1 == True:
        print("All Drives Entries deleted successfully.")
    else:
        print()
        print("Failed to delete Drives Entries.")
    
    # perform delete action
    successful = objecttier.remove_driver(dbConn, name)

    if successful == True:
        print("Driver removed successfully.")
    else:
        print()
        print("Failed to remove driver.")


#####################################################################
# helper function to validate car id
#
def validate_carId(dbConn, carId):

    if not carId.isdigit():
        return (None, -1)
    
    Car = objecttier.get_car_info(dbConn, int(carId))
    ## No car found -> return -2
    if Car == None:
        return (None, -2)
    return (Car, Car.CarId)


##################################################################  
#
# handle_add_car: 
#
# Function to add a new car in database
#
def handle_add_car(dbConn):
    brand = input("Enter car brand: ").lower()

    # validate carId -> returns (Car, CarID)
    carId = input("Enter car id: ")
    (Car_, carId_) = validate_carId(dbConn, carId)

    # validate result
    if(carId_ == -1):
        print("Invalid carId! carId must contain only digits.")
        return
    
    # safe check
    if Car_ != None:
        print(f"\n\"{Car_.Brand}\" is associated to id! Ids must be unique.")
        return

    # perform insert action
    successful = objecttier.add_car(dbConn, int(carId), brand)

    if successful == True:
        print("Car added successfully.")
    else:
        print()
        print("Failed to add car.")

##################################################################  
#
# handle_delete_car: 
#
# Function to delete a car from database
#
def handle_delete_car(dbConn):
    # user input carId
    carId = input("Enter car id to be deleted: ")

    # validate result
    (Car_, carId_) = validate_carId(dbConn, carId)
    if(carId_ == -1):
        print("Invalid carId! carId must contain only digits.")
        return
    elif(carId_ == -2):
        print(f"Illegal! No matching car found.")
        return
    
    
    # confirm deletion
    print(f"\n\"{Car_.Brand}\" will be deleted from database!")
    print(f"Here's a list of the car models (to be deleted) associated with Car ID: {carId_}")
    handle_view_certain_car_models(dbConn, carId_)
    print(f"Here's a list of the car models declared by Drivers who drive Car ID: {carId_}")#Drives Table
    handle_view_certain_drives(dbConn, carId_)
    print(f"Here's a list of the Rents with Car ID: {carId_}") #Rent Table
    handle_view_certain_rents(dbConn, carId_)
    confirm = input("Enter y to confirm or n to abort: ").lower()
    if confirm != "y":
        print("Aborted!")
        return
    

    # delete reviews (Not doing right now, may not be necessary)

    #delete rents
    successful2  = objecttier.delete_certain_rents(dbConn, carId_)

    if successful2 == True:
        print("All Rents associated with CarId deleted successfully.")
    else:
        print()
        print("Failed to delete Rents.")
    


    #delete Drives entries
    successful1  = objecttier.delete_certain_drives(dbConn, carId_)

    if successful1 == True:
        print("All Drives Entries deleted successfully.")
    else:
        print()
        print("Failed to delete Drives Entries.")

    # Then delete all car models
    # First delete all car models
    successful0 = objecttier.delete_all_model(dbConn, carId_)

    if successful0 == True:
        print("All Car Models deleted successfully.")
    else:
        print()
        print("Failed to delete car models.")
        

    # perform delete action
    successful = objecttier.delete_car(dbConn, carId_)

    if successful == True:
        print("Car deleted successfully.")
    else:
        print()
        print("Failed to delete car.")



#####################################################################
# helper function to validate model id
#
def validate_modelId(dbConn, carId, modelId):

    # validate modelId
    if not modelId.isdigit():
        return (None, -1)
    
    # validate Model
    _modelID = int(modelId)
    Model_ = objecttier.get_model_info(dbConn, _modelID, carId)

    ## No model found -> return -2
    if Model_ == None:
        return (None, -2)
    return (Model_, Model_.ModelId)

##################################################################  
#
# handle_add_model: 
#
# Function to add a new car model in database
#
def handle_add_model(dbConn):
    
    # validate carId
    carId = input("Enter car id: ")
    (Car_, carId_) = validate_carId(dbConn, carId)
    if(carId == -1):
        print("Invalid carId! carId must contain only digits.")
        return
    elif(carId_ == -2):
        print(f"Illegal! No matching car found.")
        return
    
    print(f"Model will be added to {Car_.Brand}!")
    
    # validate modelId -> returns (Model, ModelID)
    modelId = input("Enter car model id: ")
    (Model_, _modelId) = validate_modelId(dbConn, carId_, modelId)

    # validate result
    if(_modelId == -1):
        print("Invalid modelId! modelId must contain only digits.")
        return
    
    # safe check
    if Model_ != None:
        print(f"\n\"{Car_.Brand} {Model_.ModelId} {Model_.Year}\" "
               "is associated to id! Ids must be unique.")
        return
    
    color = input("Enter model color: ").lower()

    transmission = input("Enter transmission type (manual or automatic): ").lower()
    # validate transmission
    if not (transmission == "manual" or transmission == "automatic"):
        print("Invalid transmission type! Must be manual or automatic.")
        return
    
    year = input("Enter model year: ")
    if not year.isdigit():
        print("Invalid year! Year must contain only digits.")
        return
    _year = int(year)

    # perform insert action
    successful = objecttier.add_model(dbConn, 
                                      int(modelId), color, _year, transmission, carId_)

    if successful == True:
        print("Model added successfully.")
    else:
        print()
        print("Failed to add model.")



##################################################################  
#
# handle_delete_model: 
#
# Function to delete a car model from database
#
def handle_delete_model(dbConn):
    # validate car id
    carId = input("Enter car id for model to be deleted: ")
    (Car_, carId_) = validate_carId(dbConn, carId)

    # validate result
    if(carId == -1):
        print("Invalid carId! carId must contain only digits.")
        return
    elif(carId_ == -2):
        print(f"Illegal! No matching car found.")
        return
    
    # validate modelId -> returns (Model, ModelID)
    modelId = input("Enter car model id to be deleted: ")
    (Model_, _modelId) = validate_modelId(dbConn, carId_, modelId)

    # validate result
    if(_modelId == -1):
        print("Invalid modelId! modelId must contain only digits.")
        return
    elif(_modelId == -2):
        print(f"Illegal! No matching car model found.")
        return
    
    # confirm deletion
    print(f"\n\"{Car_.Brand} {Model_.ModelId} {Model_.Year}\" "
               " will be deleted from database!")
    
    print(f"Here's a list of the Drivers who drive modelId ID: {_modelId}")#Drives Table
    handle_view_certain_drives3(dbConn, _modelId)
    print(f"Here's a list of the Rents with Model ID: {_modelId}") #Rent Table
    handle_view_certain_rents3(dbConn, _modelId)

    confirm = input("Enter y to confirm or n to abort: ").lower()
    if confirm != "y":
        print("Aborted!")
        return
    

    #delete rents
    successful2  = objecttier.delete_certain_rents3(dbConn, _modelId)

    if successful2 == True:
        print("All Rents associated with ModelId deleted successfully.")
    else:
        print()
        print("Failed to delete Rents.")
    


    #delete Drives entries
    successful1  = objecttier.delete_certain_drives3(dbConn, _modelId)

    if successful1 == True:
        print("All Drives Entries deleted successfully.")
    else:
        print()
        print("Failed to delete Drives Entries.")

    # perform delete action
    successful = objecttier.delete_model(dbConn, _modelId, carId_)

    if successful == True:
        print("Model deleted successfully.")
    else:
        print()
        print("Failed to delete model.")
    return


##################################################################  
#
# handle_view_all_car_model: 
#
# Function to print all car model in the system
# Format: Brand, ModelId, Color, Year, Transmission, CarId
def handle_view_all_car_model(dbConn):

    Car_Model_List = objecttier.get_car_model_list(dbConn)

    if(Car_Model_List == None):
        print("=" * 80)
        print("No records found.")
        print("=" * 80)
        return
    
    # print result
    print("=" * 80)
    print(f"Records found: {len(Car_Model_List)}")
    print("=" * 80)
    print(f"Brand\t \tModelId\t Color\t Year\t Transmission\t CarId")
    for car_model in Car_Model_List:
        if car_model.Transmission == "manual":
            print(f"{car_model.Brand}\t {car_model.ModelId}\t "
              f"{car_model.Color}\t {car_model.Year}\t " 
              f"{car_model.Transmission}\t\t {car_model.CarId}")
        else:
            print(f"{car_model.Brand}\t {car_model.ModelId}\t "
              f"{car_model.Color}\t {car_model.Year}\t " 
              f"{car_model.Transmission}\t {car_model.CarId}")
    print("=" * 80)
    return

##################################################################  
#
# handle_view_certain_car_models: 
#
# Function to print all car model in the system, from a certain carId
# Format: Brand, ModelId, Color, Year, Transmission, CarId
def handle_view_certain_car_models(dbConn,carId):

    Car_Model_List = objecttier.get_certain_car_model_list(dbConn,carId)

    if(Car_Model_List == None):
        print("=" * 80)
        print("No records found.")
        print("=" * 80)
        return
    
    # print result
    print("=" * 80)
    print(f"Records found: {len(Car_Model_List)}")
    print("=" * 80)
    print(f"Brand\t ModelId Color\t Year\t Transmission\t CarId")
    for car_model in Car_Model_List:
        if car_model.Transmission == "manual":
            print(f"{car_model.Brand}\t {car_model.ModelId}\t "
              f"{car_model.Color}\t {car_model.Year}\t " 
              f"{car_model.Transmission}\t\t {car_model.CarId}")
        else:
            print(f"{car_model.Brand}\t {car_model.ModelId}\t "
              f"{car_model.Color}\t {car_model.Year}\t " 
              f"{car_model.Transmission}\t {car_model.CarId}")
    print("=" * 80)
    return

##################################################################  
#
# handle_view_certain_driver_reviews: 
#
# Function to print all reviews based on Driver Name
def handle_view_certain_driver_reviews(dbConn,DriverName):

    Review_List = objecttier.get_certain_driver_review_list(dbConn,DriverName)

    if(Review_List == None):
        print("=" * 80)
        print("No records found.")
        print("=" * 80)
        return
    if(len(Review_List) == 0):
        print("=" * 80)
        print("No records found.")
        print("=" * 80)
        return
    
    # print result
    print("=" * 80)
    print(f"Records found: {len(Review_List)}")
    print("=" * 80)
    print(f"ReviewId\t Message Rating\t Name\t Email")
    for review in Review_List:
        print(f"{review.ReviewId}\t {review.Message}\t "
              f"{review.Rating}\t {review.Name}\t " 
              f"{review.Email}")
    print("=" * 80)
    return


##################################################################  
#
# handle_add_driver_model: 
#
# Function to add a new driver_model relationship in database
#
def handle_add_driver_model(dbConn):
    
    # validate driver 
    name = input("Enter name: ").lower()
    Driver_ = objecttier.get_driver_info(dbConn, name)
    if Driver_ == None:
        print(f"Illegal! No matching driver found.")
        return
    
    # display all car models
    request = input("press 1 to view all car models or c to continue: ")
    if(request == "1"):
        handle_view_all_car_model(dbConn)

    ## display all car model driver drives
    
    # validate car id
    carId = input("Enter car id for model to be added: ")
    (Car_, carId_) = validate_carId(dbConn, carId)

    # validate result
    if(carId == -1):
        print("Invalid carId! carId must contain only digits.")
        return
    elif(carId_ == -2):
        print(f"Illegal! No matching car found.")
        return
    
    # validate modelId -> returns (Model, ModelID)
    modelId = input("Enter car model id to be added: ")
    (Model_, _modelId) = validate_modelId(dbConn, carId_, modelId)

    # validate result
    if(_modelId == -1):
        print("Invalid modelId! modelId must contain only digits.")
        return
    elif(_modelId == -2):
        print(f"Illegal! No matching car model found.")
        return

    # perform insert action
    successful = objecttier.add_driver_model(dbConn, _modelId, carId_, name)

    if successful == True:
        print("Model added successfully.")
    else:
        print()
        print("Failed to add model.")


##################################################################  
#
# available_car_model_helper: 
#
# Function to display and get all available car model on Date xxxx-xx-xx in database
#
def available_car_model_helper(dbConn, date):
    # get car available car models
    Car_Model_List = objecttier.get_available_car_model_list(dbConn, date)

    if(Car_Model_List == None or len(Car_Model_List) == 0):
        print(f"System has no available car for rent for {date}.")
        print("Please try a different date.")
        return None
    
    # display all available car models
    print()
    print("=" * 80)
    print(f"Available models for rent found: {len(Car_Model_List)}")
    print("=" * 80)
    print(f"Brand\t \tModelId\t Color\t Year\t Transmission\t CarId")
    for car_model in Car_Model_List:
        if car_model.Transmission == "manual":
            print(f"{car_model.Brand}\t {car_model.ModelId}\t "
              f"{car_model.Color}\t {car_model.Year}\t " 
              f"{car_model.Transmission}\t\t {car_model.CarId}")
        else:
            print(f"{car_model.Brand}\t {car_model.ModelId}\t "
              f"{car_model.Color}\t {car_model.Year}\t " 
              f"{car_model.Transmission}\t {car_model.CarId}")
    print("=" * 80)
    return

##################################################################  
#
# handle_view_certain_car_models: 
#
# Function to print all car model in the system, from a certain carId
# Format: Brand, ModelId, Color, Year, Transmission, CarId
def handle_view_certain_car_models(dbConn,carId):

    Car_Model_List = objecttier.get_certain_car_model_list(dbConn,carId)

    if(Car_Model_List == None):
        print("=" * 80)
        print("No car model records found.")
        print("=" * 80)
        return
    
    # print result
    print("=" * 80)
    print(f"Records found: {len(Car_Model_List)}")
    print("=" * 80)
    print(f"Brand\t ModelId Color\t Year\t Transmission\t CarId")
    for car_model in Car_Model_List:
        if car_model.Transmission == "manual":
            print(f"{car_model.Brand}\t {car_model.ModelId}\t "
              f"{car_model.Color}\t {car_model.Year}\t " 
              f"{car_model.Transmission}\t\t {car_model.CarId}")
        else:
            print(f"{car_model.Brand}\t {car_model.ModelId}\t "
              f"{car_model.Color}\t {car_model.Year}\t " 
              f"{car_model.Transmission}\t {car_model.CarId}")
    print("=" * 80)
    return

##################################################################  
#
# handle_view_certain_drives: 
#
# Function to print all entries in the Drives Table associated with a certain carId
# Format: 
def handle_view_certain_drives(dbConn,carId):

    Drives_List = objecttier.get_certain_drives_list(dbConn,carId)

    if(Drives_List == None):
        print("=" * 80)
        print("No Drives records found.")
        print("=" * 80)
        return
    
    # print result
    print("=" * 80)
    print(f"Drives Records found: {len(Drives_List)}") #D.modelId, D.carId, D.name
    print("=" * 80)
    print(f"ModelId\t CarID\t Driver Name\t")
    for drives in Drives_List:
        print(f"{drives.ModelId}\t {drives.CarId}\t "
              f"{drives.Name}\t")
    print("=" * 80)
    return

##################################################################  
#
# handle_view_certain_drives2: 
#
# Function to print all entries in the Drives Table associated with a certain Driver Name
# Format: 
def handle_view_certain_drives2(dbConn,DriverName):

    Drives_List = objecttier.get_certain_drives_list2(dbConn,DriverName)

    if(Drives_List == None):
        print("=" * 80)
        print("No Drives records found.")
        print("=" * 80)
        return
    if(len(Drives_List) == 0):
        print("=" * 80)
        print("No Drives records found.")
        print("=" * 80)
        return
    
    # print result
    print("=" * 80)
    print(f"Drives Records found: {len(Drives_List)}") #D.modelId, D.carId, D.name
    print("=" * 80)
    print(f"ModelId\t CarID\t Driver Name\t")
    for drives in Drives_List:
        print(f"{drives.ModelId}\t {drives.CarId}\t "
              f"{drives.Name}\t")
    print("=" * 80)
    return

##################################################################  
#
# handle_view_certain_drives3: 
#
# Function to print all entries in the Drives Table associated with a certain Driver Name
# Format: 
def handle_view_certain_drives3(dbConn,modelId):

    Drives_List = objecttier.get_certain_drives_list3(dbConn,modelId)

    if(Drives_List == None):
        print("=" * 80)
        print("No Drives records found.")
        print("=" * 80)
        return
    if(len(Drives_List) == 0):
        print("=" * 80)
        print("No Drives records found.")
        print("=" * 80)
        return
    
    # print result
    print("=" * 80)
    print(f"Drives Records found: {len(Drives_List)}") #D.modelId, D.carId, D.name
    print("=" * 80)
    print(f"ModelId\t CarID\t Driver Name\t")
    for drives in Drives_List:
        print(f"{drives.ModelId}\t {drives.CarId}\t "
              f"{drives.Name}\t")
    print("=" * 80)
    return

##################################################################  
#
# handle_view_certain_rents: 
#
# Function to print all car model in the system, from a certain carId
# Format: Brand, ModelId, Color, Year, Transmission, CarId
def handle_view_certain_rents(dbConn,carId):
    # TODO:
    Rents_List = objecttier.get_certain_rents_list(dbConn,carId)

    if(Rents_List == None):
        print("=" * 80)
        print("No records found.")
        print("=" * 80)
        return
    
    # print result
    print("=" * 80)
    print(f"Records found: {len(Rents_List)}")
    print("=" * 80)
    print(f"RentId\t Date Email\t DriverName\t ModelId\t CarId")
    # rentId, date, email, name, modelId, carId):
    # self.RentId self.Date = date
    #   self._Email = email
    #   self._Name = name
    #   self._ModelId = modelId
    #   self._CarId = carId

    for rent in Rents_List:
        print(f"{rent.RentId}\t {rent.Date}\t "
              f"{rent.Email}\t {rent.Name}\t " 
              f"{rent.ModelId}\t\t {rent.CarId}")
    print("=" * 80)
    return

##################################################################  
#
# handle_view_certain_rents2: 
#
# Function to print all car model in the system, from a Driver Name
# Format: Brand, ModelId, Color, Year, Transmission, CarId
def handle_view_certain_rents2(dbConn,driverName):
    # TODO:
    Rents_List = objecttier.get_certain_rents_list2(dbConn,driverName)

    if(Rents_List == None):
        print("=" * 80)
        print("No records found.")
        print("=" * 80)
        return
    if(len(Rents_List) == 0):
        print("=" * 80)
        print("No records found.")
        print("=" * 80)
        return
    # print result
    print("=" * 80)
    print(f"Records found: {len(Rents_List)}")
    print("=" * 80)
    print(f"RentId\t Date Email\t DriverName\t ModelId\t CarId")
    # rentId, date, email, name, modelId, carId):
    # self.RentId self.Date = date
    #   self._Email = email
    #   self._Name = name
    #   self._ModelId = modelId
    #   self._CarId = carId

    for rent in Rents_List:
        print(f"{rent.RentId}\t {rent.Date}\t "
              f"{rent.Email}\t {rent.Name}\t " 
              f"{rent.ModelId}\t\t {rent.CarId}")
    print("=" * 80)
    return

##################################################################  
#
# handle_view_certain_rents3: 
#
# Function to print all car model in the system, from a Driver Name
# Format: Brand, ModelId, Color, Year, Transmission, CarId
def handle_view_certain_rents3(dbConn,driverName):
    # TODO:
    Rents_List = objecttier.get_certain_rents_list3(dbConn,driverName)

    if(Rents_List == None):
        print("=" * 80)
        print("No records found.")
        print("=" * 80)
        return
    if(len(Rents_List) == 0):
        print("=" * 80)
        print("No records found.")
        print("=" * 80)
        return
    # print result
    print("=" * 80)
    print(f"Records found: {len(Rents_List)}")
    print("=" * 80)
    print(f"RentId\t Date Email\t DriverName\t ModelId\t CarId")
    # rentId, date, email, name, modelId, carId):
    # self.RentId self.Date = date
    #   self._Email = email
    #   self._Name = name
    #   self._ModelId = modelId
    #   self._CarId = carId

    for rent in Rents_List:
        print(f"{rent.RentId}\t {rent.Date}\t "
              f"{rent.Email}\t {rent.Name}\t " 
              f"{rent.ModelId}\t\t {rent.CarId}")
    print("=" * 80)
    return


##################################################################  
#
# handle_add_driver_model: 
#
# Function to add a new driver_model relationship in database
#
def handle_add_driver_model(dbConn):
    
    # validate driver 
    name = input("Enter name: ").lower()
    Driver_ = objecttier.get_driver_info(dbConn, name)
    if Driver_ == None:
        print(f"Illegal! No matching driver found.")
        return
    
    # display all car models
    request = input("press 1 to view all car models or c to continue: ")
    if(request == "1"):
        handle_view_all_car_model(dbConn)

    ## display all car model driver drives
    
    # validate car id
    carId = input("Enter car id for model to be added: ")
    (Car_, carId_) = validate_carId(dbConn, carId)

    # validate result
    if(carId == -1):
        print("Invalid carId! carId must contain only digits.")
        return
    elif(carId_ == -2):
        print(f"Illegal! No matching car found.")
        return
    
    # validate modelId -> returns (Model, ModelID)
    modelId = input("Enter car model id to be added: ")
    (Model_, _modelId) = validate_modelId(dbConn, carId_, modelId)

    # validate result
    if(_modelId == -1):
        print("Invalid modelId! modelId must contain only digits.")
        return
    elif(_modelId == -2):
        print(f"Illegal! No matching car model found.")
        return

    # perform insert action
    successful = objecttier.add_driver_model(dbConn, _modelId, carId_, name)

    if successful == True:
        print("Model added successfully.")
    else:
        print()
        print("Failed to add model.")


##################################################################  
#
# available_car_model_helper: 
#
# Function to display and get all available car model on Date xxxx-xx-xx in database
#
def available_car_model_helper(dbConn, date):
    # get car available car models
    Car_Model_List = objecttier.get_available_car_model_list(dbConn, date)

    if(Car_Model_List == None or len(Car_Model_List) == 0):
        print(f"System has no available car for rent for {date}.")
        print("Please try a different date.")
        return None
    
    # display all available car models
    print()
    print("=" * 80)
    print(f"Available models for rent found: {len(Car_Model_List)}")
    print("=" * 80)
    print(f"Brand\t \tModelId\t Color\t Year\t Transmission\t CarId")
    for car_model in Car_Model_List:
        if car_model.Transmission == "manual":
            print(f"{car_model.Brand}\t {car_model.ModelId}\t "
              f"{car_model.Color}\t {car_model.Year}\t " 
              f"{car_model.Transmission}\t\t {car_model.CarId}")
        else:
            print(f"{car_model.Brand}\t {car_model.ModelId}\t "
              f"{car_model.Color}\t {car_model.Year}\t " 
              f"{car_model.Transmission}\t {car_model.CarId}")
    print("=" * 80)
    return Car_Model_List

##################################################################  
#
# handle_view_available_car_model: 
#
# Function to print all available car model in the system
# Format: Brand, ModelId, Color, Year, Transmission, CarId
def handle_view_available_car_model(dbConn):
    # get rent date
    date = input("Enter rent date (YYYY-MM-DD): ")
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Please enter the date in YYYY-MM-DD format.")
        return
    
    _ = available_car_model_helper(dbConn, date)
    return

##################################################################  
#
# handle_book_rent: 
#
# Function to add a new rent datail in database
#
def handle_book_rent(dbConn):
    # validate client 
    email = input("Enter your email: ").lower()

    Client_ = objecttier.get_client_info(dbConn, email)
    if(Client_ == None):
        print(f"No client found with email \"{email}\"!")
        return
    
    # get rent date
    date = input("Enter rent date (YYYY-MM-DD): ")
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Please enter the date in YYYY-MM-DD format.")
        return

    # get car available car models
    Car_Model_List = available_car_model_helper(dbConn, date)

    # validate result
    if(Car_Model_List == None):
        return
    
    # validate car id
    carId = int(input("Enter car id for model to rent: "))
    if not any(car_model.CarId == carId for car_model in Car_Model_List):
        print("Car selected is unavailble.")
        print("Aborting")
        return
    
    # validate model id
    modelId = int(input("Enter model id for model to rent: "))
    if not any((car_model.CarId == carId  and car_model.ModelId == modelId)
               for car_model in Car_Model_List):
        print("Model selected is unavailble.")
        print("Aborting")
        return

    # find available drivers
    Drivers_List = objecttier.get_available_drivers_list(dbConn, date, modelId, carId)

    # validate drivers
    if(Drivers_List == None or len(Drivers_List) == 0):
        print("Sorry, there is no available driver for this rent")
        print("Please try a model or date.")
        print("Aborting")
        return
    
    # Assign first driver returned
    Driver_ = Drivers_List[0]

    # perform insert action
    successful = objecttier.add_rent(dbConn, 
                                     date, email, Driver_.Name, modelId, carId)

    if successful == True:
        print("Congrats! Your rent has been booked!.")
        print()
        print("Rent details: ")
        print(f"Date: {date}")
        print(f"Your driver name is {Driver_.Name}")
        vehicle_info = next((car_model for car_model in Car_Model_List if car_model.ModelId == modelId and car_model.CarId == carId), None)
        if vehicle_info:
            print(f"Vehicle info: Brand: {vehicle_info.Brand}, ModelId: {vehicle_info.ModelId}, Color: {vehicle_info.Color}, Year: {vehicle_info.Year}, Transmission: {vehicle_info.Transmission}, CarId: {vehicle_info.CarId}")
        else:
            print("Vehicle info: Not found")

    else:
        print()
        print("Booing failed.")

##################################################################  
#
# handle_view_all_rent_detail:
#
# Function to print all rent detail of client the system
# Format: -------------------------------------------------------------
#          1.
#          Bookings details for: Rent ID
#          Rent date: xxxx-xx-xx
#          Assigned driver: XYZ
#          Brand, ModelId, Color, Year, Transmission, CarId
#          -------------------------------------------------------------
def handle_view_all_rent_detail(dbConn, email):

    # email = input("Enter your email: ").lower()
    Rent_Detail_List = objecttier.get_rent_detail_list(dbConn, email)

    if(Rent_Detail_List == None):
        print("=" * 70)
        print("No records found.")
        print("=" * 70)
        return
    
    # print result
    print("=" * 70)
    print(f"Records found: {len(Rent_Detail_List)}")
    print("=" * 70)
    count = 1
    for rent_detail in Rent_Detail_List:
        print("-" * 70)
        print(f"{count}.")
        print(f"\tBooking details for RentID: # {rent_detail.RentId}")
        print(f"\tRent date : {rent_detail.Date}")
        print(f"\tAssigned driver: {rent_detail.Name.upper()}")
        print("\tVehicle details: "
              f"{rent_detail.Brand} {rent_detail.ModelId} "
              f"{rent_detail.Color} {rent_detail.Year} " 
              f"{rent_detail.Transmission} {rent_detail.CarId}")
        print("-" * 70)
        count += 1
    print("=" * 70)
    return

##################################################################  
#
# handle_top_k_clients: 
#
# Function to return top-k clients with respect to how many rents the client has booked
# Format: 
def handle_top_k_clients(dbConn):
    k = input("Enter k for top-k clients with highest number of booked rents to be returned: ")

    if not k.isdigit() or int(k) <= 0:
        print("k must be a positive integer or greater than 0")
        return

    k = int(k)  # Convert k into an integer

    Top_Client_List = objecttier.get_top_k_clients_by_rents(dbConn, k)

    if (Top_Client_List == None or len(Top_Client_List) == 0):
        print("No Rental Data")
        return
    
    print()
    print("-" * 70 )
    print("\nTop Clients")
    print("-" * 70 )
    print(f"Rank\t \tName\t \t\tEmail\t \tRents")

    # print Top_K Clients
    rank = 1
    for top_client in Top_Client_List:
        print(f"{rank}\t \t{top_client.Name}\t \t{top_client.Email}\t \t{top_client.RentCount}")        
        rank += 1
    return


##################################################################  
#
# handle_view_model_usage: 
#
# Function to return a list of every model with how many times its been rented 
def handle_view_model_usage(dbConn):
    Car_Model_Usage_List = objecttier.get_model_rent_counts(dbConn)

    if(Car_Model_Usage_List == None or len(Car_Model_Usage_List) == 0):
        print("=" * 80)
        print("No Car Model Data")
        print("=" * 80)
        return

    # print result
    print("=" * 80)
    print(f"Records found: {len(Car_Model_Usage_List)}")
    print("=" * 80)

    print("\t\t\tCar - Model Usage")
    print("=" * 80)
    count = 1
    print(f"Brand\t \tModelId\t Color\t Year\t Transmission\t CarId\t Times Rented")
    for car_model_usage in Car_Model_Usage_List:
        if car_model_usage.Transmission == "manual":
            print(f"{car_model_usage.Brand}\t {car_model_usage.ModelId}\t "
                  f"{car_model_usage.Color}\t {car_model_usage.Year}\t " 
                  f"{car_model_usage.Transmission}\t\t {car_model_usage.CarId}\t "
                  f"  {car_model_usage.RentCount}")
        else:
            print(f"{car_model_usage.Brand}\t {car_model_usage.ModelId}\t "
                  f"{car_model_usage.Color}\t {car_model_usage.Year}\t " 
                  f"{car_model_usage.Transmission}\t {car_model_usage.CarId}\t "
                  f"  {car_model_usage.RentCount}")
    print("=" * 80)
    return


##################################################################  
#
# handle_driver_usage_stats: 
#
# Function to return a list of each drivers statistics
def handle_driver_usage_stats(dbConn):
    all_driver_usage_stats = objecttier.get_driver_usage_stats(dbConn)

    if not all_driver_usage_stats:
        print("No Driver Data")

    print("\nDriver Stats")
    print("-------------------------")
    print(f"Driver Name\t Rents\t Avg Review Rating")
    for name, num_rents, avg_rating in all_driver_usage_stats:
        print(f"{name}\t\t {num_rents}\t {avg_rating}")

    return

# Ask the manager for two cities and list the matching
def handle_query_clients_by_cities(dbConn):
    city_1 = input("Enter Client's City Address: ").lower()
    city_2 = input("Enter Driver's City Address: ").lower()

    # get client list
    Client_List = objecttier.get_clients_by_cities(dbConn, city_1, city_2)

    # validate result
    if (Client_List == None or len(Client_List) == 0):
        print("\nNo clients match this criteria")

    # print result
    print(f"\n\nShowing results for client in {city_1} city" \
          f" who have booked a rent having a driver in {city_2} city")
    print("=" * 70)
    print(f"Records found: {len(Client_List)}")
    print("=" * 70)

    print("-" * 70)
    print(f"Client Name\t\t\t Client Email")
    print("\n" + "-" * 70)
    for client in Client_List:
        print(f"{client.Name}\t\t\t\t {client.Email}")
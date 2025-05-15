###############################################################################
#  Objecttier
# This module defines class objects and functions to manipulate those objects.
###############################################################################
import datatier

##################################################################
#
##################################################################
#
# Manager:
#
# Constructor(...)
# Properties:
#   SSN: string
#   Email: string
#   Name: string

class Manager:
   def __init__(self, ssn, email, name):
      self._SSN = ssn
      self._Email = email
      self._Name = name

   # define properties
   @property
   def SSN(self):
      return self._SSN

   @property
   def Email(self):
      return self._Email

   @property
   def Name(self):
      return self._Name
   
##################################################################
#
##################################################################
#
# Clients:
#
# Constructor(...)
# Properties:
#   Email: string
#   Name: string

class Client:
   def __init__(self, email, name):
      self._Email = email
      self._Name = name

   # define properties
   @property
   def Email(self):
      return self._Email

   @property
   def Name(self):
      return self._Name


##################################################################
#
##################################################################
#
# Top_Client:
#
# Constructor(...)
# Properties:
#   Email: string
#   Name: string
#   RentCount: int

class Top_Client:
   def __init__(self, email, name, rentCount):
      self._Email = email
      self._Name = name
      self._RentCount = rentCount

   # define properties
   @property
   def Email(self):
      return self._Email

   @property
   def Name(self):
      return self._Name
   
   @property
   def RentCount(self):
      return self._RentCount
   

##################################################################
#
##################################################################
#
# Address:
#
# Constructor(...)
# Properties:
#   Road: string
#   Number: string
#   City: string

class Address:
   def __init__(self, road, number, city):
      self._Road = road
      self._Number = number
      self._City = city

   # define properties
   @property
   def Road(self):
      return self._Road

   @property
   def Number(self):
      return self._Number

   @property
   def City(self):
      return self._City


##################################################################
#
##################################################################
#
# Driver:
#
# Constructor(...)
# Properties:
#   Name: string
#   Road: string
#   Number: string
#   City: string

class Driver:
   def __init__(self, name, road, number, city):
      self._Name = name
      self._Road = road
      self._Number = number
      self._City = city

   # define properties
   @property
   def Name(self):
      return self._Name

   @property
   def Road(self):
      return self._Road

   @property
   def Number(self):
      return self._Number

   @property
   def City(self):
      return self._City
   

##################################################################
#
##################################################################
#
# Car:
#
# Constructor(...)
# Properties:
#   CarId: int
#   Brand: string

class Car:
   def __init__(self, carId, brand):
      self._CarId = carId
      self._Brand = brand

   # define properties
   @property
   def CarId(self):
      return self._CarId
   
   @property
   def Brand(self):
      return self._Brand
   

##################################################################
#
##################################################################
#
# Model:
#
# Constructor(...)
# Properties:
#   ModelId: int
#   Color: string
#   Year: int
#   Transmission: string
#   CarId: int

class Model:
   def __init__(self, modelId, color, year, transmission, carId):
      self._ModelId = modelId
      self._Color = color
      self._Year = year
      self._Transmission = transmission
      self._CarId = carId

   # define properties
   @property
   def ModelId(self):
      return self._ModelId

   @property
   def Color(self):
      return self._Color

   @property
   def Year(self):
      return self._Year

   @property
   def Transmission(self):
      return self._Transmission

   @property
   def CarId(self):
      return self._CarId
   
##################################################################
#
##################################################################
#
# Car_Model:
#
# Constructor(...)
# Properties:
#   ModelId: int
#   Color: string
#   Year: int
#   Transmission: string
#   CarId: int
#   Brand: string

class Car_Model:
   def __init__(self, modelId, color, year, transmission, carId, brand):
      self._ModelId = modelId
      self._Color = color
      self._Year = year
      self._Transmission = transmission
      self._CarId = carId
      self._Brand = brand

   # define properties
   @property
   def ModelId(self):
      return self._ModelId

   @property
   def Color(self):
      return self._Color

   @property
   def Year(self):
      return self._Year

   @property
   def Transmission(self):
      return self._Transmission

   @property
   def CarId(self):
      return self._CarId
   
   @property
   def Brand(self):
      return self._Brand
   

##################################################################
#
##################################################################
#
# Car_Model_Usage:
#
# Constructor(...)
# Properties:
#   ModelId: int
#   Color: string
#   Year: int
#   Transmission: string
#   CarId: int
#   Brand: string
#   RentCount: int

class Car_Model_Usage:
   def __init__(self, modelId, color, year, transmission, carId, brand, rentCount):
      self._ModelId = modelId
      self._Color = color
      self._Year = year
      self._Transmission = transmission
      self._CarId = carId
      self._Brand = brand
      self._RentCount = rentCount

   # define properties
   @property
   def ModelId(self):
      return self._ModelId

   @property
   def Color(self):
      return self._Color

   @property
   def Year(self):
      return self._Year

   @property
   def Transmission(self):
      return self._Transmission

   @property
   def CarId(self):
      return self._CarId
   
   @property
   def Brand(self):
      return self._Brand
   
   @property
   def RentCount(self):
      return self._RentCount
   

##################################################################
#
##################################################################
#
# Rent:
#
# Constructor(...)
# Properties:
#   RentId: int
#   Date: date
#   Email: string
#   Name: string
#   ModelId: int
#   CarId: int

class Rent:
   def __init__(self, rentId, date, email, name, modelId, carId):
      self._RentId = rentId
      self._Date = date
      self._Email = email
      self._Name = name
      self._ModelId = modelId
      self._CarId = carId

   # define properties
   @property
   def RentId(self):
      return self._RentId

   @property
   def Date(self):
      return self._Date

   @property
   def Email(self):
      return self._Email

   @property
   def Name(self):
      return self._Name

   @property
   def ModelId(self):
      return self._ModelId

   @property
   def CarId(self):
      return self._CarId
   

##################################################################
#
##################################################################
#
# Rent_Detail:
#
# Constructor(...)
# Properties:
#   RentId: int
#   Date: date
#   Email: string
#   Name: string
#   Brand: string
#   ModelId: int
#   Color: string
#   Year: int
#   Transmission: string
#   CarId: int

class Rent_Detail:
   def __init__(self, rentId, date, email, name, brand, modelId,
                      color, year, transmission, carId):
      self._RentId = rentId
      self._Date = date
      self._Email = email
      self._Name = name
      self._Brand = brand
      self._ModelId = modelId
      self._Color = color
      self._Year = year
      self._Transmission = transmission
      self._CarId = carId

   # define properties
   @property
   def RentId(self):
      return self._RentId

   @property
   def Date(self):
      return self._Date

   @property
   def Email(self):
      return self._Email

   @property
   def Name(self):
      return self._Name

   @property
   def Brand(self):
      return self._Brand

   @property
   def ModelId(self):
      return self._ModelId

   @property
   def Color(self):
      return self._Color

   @property
   def Year(self):
      return self._Year

   @property
   def Transmission(self):
      return self._Transmission

   @property
   def CarId(self):
      return self._CarId
   

##################################################################
#
##################################################################
#
# Review:
#
# Constructor(...)
# Properties:
#   ReviewId: int
#   Message: string
#   Rating: int
#   Name: string
#   Email: string

class Review:
   def __init__(self, reviewId, message, rating, name, email):
      self._ReviewId = reviewId
      self._Message = message
      self._Rating = rating
      self._Name = name
      self._Email = email

   # define properties
   @property
   def ReviewId(self):
      return self._ReviewId

   @property
   def Message(self):
      return self._Message

   @property
   def Rating(self):
      return self._Rating

   @property
   def Name(self):
      return self._Name

   @property
   def Email(self):
      return self._Email
   

##################################################################
#
##################################################################
#
# CreditCard:
#
# Constructor(...)
# Properties:
#   CardNum: int
#   Email: string
#   Road: string
#   Number: string
#   City: string

class CreditCard:
   def __init__(self, cardNum, email, road, number, city):
      self._CardNum = cardNum
      self._Email = email
      self._Road = road
      self._Number = number
      self._City = city

   # define properties
   @property
   def CardNum(self):
      return self._CardNum

   @property
   def Email(self):
      return self._Email

   @property
   def Road(self):
      return self._Road

   @property
   def Number(self):
      return self._Number

   @property
   def City(self):
      return self._City
   

##################################################################
#
##################################################################
#
# Drives:
#
# Constructor(...)
# Properties:
#   ModelId: int
#   CarId: int
#   Name: string

class Drives:
   def __init__(self, modelId, carId, name):
      self._ModelId = modelId
      self._CarId = carId
      self._Name = name

   @property
   def ModelId(self):
      return self._ModelId
   
   @property
   def CarId(self):
      return self._CarId
   
   @property
   def Name(self):
      return self._Name

##################################################################
#
##################################################################
#
# ClientAddress:
#
# Constructor(...)
# Properties:
#   Email: string
#   Road: string
#   Number: string
#   City: string

class ClientAddress:
   def __init__(self, email, road, number, city):
      self._Email = email
      self._Road = road
      self._Number = number
      self._City = city

   # define properties
   @property
   def Email(self):
      return self._Email
   
   @property
   def Road(self):
      return self._Road

   @property
   def Number(self):
      return self._Number

   @property
   def City(self):
      return self._City




##################################################################
# 
# num_managers:
#
# Returns: number of managers in the database
#           If an error occurs, the function returns -1
#
def num_managers(dbConn):

   # query to get the number of lobbyists
   sql = """SELECT COUNT(*) FROM Manager"""

   try:
      result = datatier.select_one_row(dbConn, sql)[0]
      return result
   except Exception as err:
      return -1   
      

##################################################################
# 
# num_drivers:
#
# Returns: number of drivers in the database
#           If an error occurs, the function returns -1
#
def num_drivers(dbConn):

   # query to get the number of drivers
   sql = """SELECT COUNT(*) FROM Driver"""

   try:
      result = datatier.select_one_row(dbConn, sql)[0]
      return result
   except Exception as err:
      return -1
   

##################################################################
# 
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
   
   # query to get the number of clients
   sql = """SELECT COUNT(*) FROM Client"""

   try:
      result = datatier.select_one_row(dbConn, sql)[0]
      return result
   except Exception as err:
      return -1


##################################################################
# 
# num_cars:
#
# Returns: number of cars in the database
#           If an error occurs, the function returns -1
#
def num_cars(dbConn):

   # query to get the number of drivers
   sql = """SELECT COUNT(*) FROM Car"""

   try:
      result = datatier.select_one_row(dbConn, sql)[0]
      return result
   except Exception as err:
      return -1
   

##################################################################
# 
# num_models:
#
# Returns: number of car models in the database
#           If an error occurs, the function returns -1
#
def num_models(dbConn):

   # query to get the number of drivers
   sql = """SELECT COUNT(*) FROM Model"""

   try:
      result = datatier.select_one_row(dbConn, sql)[0]
      return result
   except Exception as err:
      return -1
   
##################################################################
# 
# get_payment_address_count:
#
# return: 1 -> payment address exist
#         0 -> payment address does not exist
#
def get_payment_address_count(dbConn, road, number, city):
   
   # query to get the number of clients
   sql = """SELECT COUNT(*) FROM CreditCard
            WHERE road = %s AND number = %s AND city = %s
         """

   try:
      result = datatier.select_one_row(dbConn, sql, [road, number, city])[0]
      return result
   except Exception as err:
      return -1
   

##################################################################
#
# get_manager_info:
#
# returns manager with ssn if manager exist
#
def get_manager_info(dbconn, ssn):
   # query to fetch details of user specified ssn
   sql = """
            SELECT * 
            FROM Manager
            WHERE ssn = %s
         """
   
   # retrieve result from datatier
   result = datatier.select_one_row(dbconn, sql, [ssn])

   # validate result
   if result == None or len(result) == 0:
      return None
   return Manager(result[0], result[1], result[2])


##################################################################
#
# get_driver_info:
#
# returns driver with name if driver exist
#
def get_driver_info(dbconn, name):
   # query to fetch details of user specified name
   sql = """
            SELECT * 
            FROM Driver
            WHERE name = %s
         """
   
   # retrieve result from datatier
   result = datatier.select_one_row(dbconn, sql, [name])

   # validate result
   if result == None or len(result) == 0:
      return None
   return Driver(result[0], result[1], result[2], result[3])

##################################################################
#
# get_driver_client_info:
#
# returns driver with name if driver exist, and was/is booked by client
#
def get_driver_client_info(dbconn, email, name):
   # query to fetch details of user specified name
   sql = """ 
            SELECT Rent.name
            FROM Rent
            WHERE Rent.email = %s AND Rent.name = %s
         """

   
   # retrieve result from datatier
   result = datatier.select_one_row(dbconn, sql, [email, name])

   # validate result
   if result == None or len(result) == 0:
      return None
   return Driver(result[0], "", "", "") # hide driver address


##################################################################
#
# get_client_info:
#
# returns client with email if driver exist
#
def get_client_info(dbconn, email):
   # query to fetch details of user specified email
   sql = """
            SELECT * 
            FROM Client
            WHERE email = %s
         """
   
   # retrieve result from datatier
   result = datatier.select_one_row(dbconn, sql, [email])

   # validate result
   if result == None or len(result) == 0:
      return None
   return Client(result[0], result[1])

##################################################################
#
# get_address_info:
#
# returns address with (road, number, city) if address exist
#
def get_address_info(dbconn, road, number, city):
   # query to fetch details of address specified
   sql = """
            SELECT * 
            FROM Address
            WHERE road = %s AND number = %s AND city = %s
         """
   
   # retrieve result from datatier
   result = datatier.select_one_row(dbconn, sql, [road, number, city])

   # validate result
   if result == None or len(result) == 0:
      return None
   return Address(result[0], result[1], result[2])

##################################################################
#
# get_creditcard_info:
#
# returns creditCard with (cardnum) if credit card exist
#
def get_creditcard_info(dbconn, cardnum):
   # query to fetch details of creditcard specified
   sql = """
            SELECT * 
            FROM CreditCard
            WHERE cardnum = %s
         """
   
   # retrieve result from datatier
   result = datatier.select_one_row(dbconn, sql, [cardnum])

   # validate result
   if result == None or len(result) == 0:
      return None
   return CreditCard(result[0], result[1], result[2], result[3], result[4])


##################################################################
#
# get_car_info:
#
# returns car with carId if car exist
#
def get_car_info(dbconn, carId):
   # query to fetch details of car specified carId
   sql = """
            SELECT * 
            FROM Car
            WHERE carId = %s
         """
   
   # retrieve result from datatier
   result = datatier.select_one_row(dbconn, sql, [carId])

   # validate result
   if result == None or len(result) == 0:
      return None
   return Car(result[0], result[1])


##################################################################
#
# get_model_info:
#
# returns model with (modelId, carId) if model exist
#
def get_model_info(dbconn, modelId, carId):
   # query to fetch details of model specified 
   sql = """
            SELECT * 
            FROM Model
            WHERE modelId = %s AND carId = %s
         """
   
   # retrieve result from datatier
   result = datatier.select_one_row(dbconn, sql, [modelId, carId])

   # validate result
   if result == None or len(result) == 0:
      return None
   return Model(result[0], result[1], result[2], result[3], result[4])

##################################################################
#
# get_rent_detail_list:
#
# returns full rent details of client 
#
def get_rent_detail_list(dbconn, email):
   # query to fetch details of user specified name
   sql = """
            SELECT R.rentId, R.date, R.email, R.name,
            C.Brand, M.modelId, M.color, M.year, M.transmission, M.carId
            FROM Car AS C
            INNER JOIN Model AS M ON M.carId = C.carId
            INNER JOIN Rent AS R ON R.carId = M.carId
                                AND R.modelId = M.modelId
            WHERE R.email = %s
            ORDER BY R.date DESC
          """
   
   # retrieve result from datatier
   result = datatier.select_n_rows(dbconn, sql, [email])

   # validate result
   if result == None:
      return None
   
   # itemize tupled result
   itemized = []
   
   for item in result:
      itemized.append(Rent_Detail(item[0], item[1], item[2], item[3],
                                 item[4], item[5], item[6], item[7],
                                 item[8], item[9])
                                 )
   return itemized
##################################################################
#
# get_car_model_list:
#
# returns car_model where (Model.carId = Car.carID) 
#  Format -> ModelId, Color, Year, Transmission, CarId, Brand
def get_car_model_list(dbconn):
   # query to fetch details of all car_model
   sql = """ SELECT M.modelId, M.color, M.year, M.transmission, C.carId, C.brand
              FROM Model AS M
              INNER JOIN Car AS C
              USING (carid)
         """

   # retrieve result from datatier
   result = datatier.select_n_rows(dbconn, sql, [])

   # validate result
   if result == None:
      return None
   
   # itemize tupled result
   itemized = []
   
   for item in result:
      itemized.append(Car_Model(item[0], item[1], item[2], item[3], item[4], item[5]))
   return itemized

##################################################################
#
# get_certain_car_model_list:
#
# returns car_model where (Model.carId = Car.carID) 
#  Format -> ModelId, Color, Year, Transmission, CarId, Brand
def get_certain_car_model_list(dbconn,carId):
   # query to fetch details of all car_model
   sql = """ SELECT M.modelId, M.color, M.year, M.transmission, C.carId, C.brand
              FROM Model AS M
              INNER JOIN Car AS C
              USING (carid)
              WHERE C.carId = %s
         """

   # retrieve result from datatier
   result = datatier.select_n_rows(dbconn, sql, [carId])

   # validate result
   if result == None:
      return None
   
   # itemize tupled result
   itemized = []
   
   for item in result:
      itemized.append(Car_Model(item[0], item[1], item[2], item[3], item[4], item[5]))
   return itemized

##################################################################
#
# get_certain_driver_review_list:
#
# returns driver review list
#  Format -> 
def get_certain_driver_review_list(dbconn,DriverName):
   # query to fetch details of all car_model
   sql = """ SELECT R.reviewId, R.message, R.rating, R.name, R.email
              FROM Review as R
              WHERE R.name = %s
         """

   # retrieve result from datatier
   result = datatier.select_n_rows(dbconn, sql, [DriverName])

   # validate result
   if result == None:
      return None
   
   # itemize tupled result
   itemized = []
   # self, reviewId, message, rating, name, email):
   #    self._ReviewId = reviewId
   #    self._Message = message
   #    self._Rating = rating
   #    self._Name = name
   #    self._Email = email
   for item in result:
      itemized.append(Review(item[0], item[1], item[2], item[3], item[4]))
   return itemized

##################################################################
#
# get_certain_drives_list:
#
# returns car_model where (Model.carId = Car.carID) 
#  Format -> ModelId, Color, Year, Transmission, CarId, Brand
def get_certain_drives_list(dbconn,carId):
   # query to fetch details of all car_model
   sql = """ SELECT D.modelId, D.carId, D.name
              FROM Drives AS D
              WHERE D.carId = %s
         """

   # retrieve result from datatier
   result = datatier.select_n_rows(dbconn, sql, [carId])

   # validate result
   if result == None:
      return None
   
   # itemize tupled result
   itemized = []
   
   for item in result:
      itemized.append(Drives(item[0], item[1], item[2]))#(self, modelId, carId, name)
   return itemized

##################################################################
#
# get_certain_drives_list2:
#
# returns drives entries based on driverName
#  Format -> 
def get_certain_drives_list2(dbconn,driverName):
   # query to fetch details of all car_model
   sql = """ SELECT D.modelId, D.carId, D.name
              FROM Drives AS D
              WHERE D.name = %s
         """

   # retrieve result from datatier
   result = datatier.select_n_rows(dbconn, sql, [driverName])

   # validate result
   if result == None:
      return None
   
   # itemize tupled result
   itemized = []
   
   for item in result:
      itemized.append(Drives(item[0], item[1], item[2]))#(self, modelId, carId, name)
   return itemized

##################################################################
#
# get_certain_drives_list3:
#
# returns drives entries based on driverName
#  Format -> 
def get_certain_drives_list3(dbconn,modelId):
   # query to fetch details of all car_model
   sql = """ SELECT D.modelId, D.carId, D.name
              FROM Drives AS D
              WHERE D.modelId = %s
         """

   # retrieve result from datatier
   result = datatier.select_n_rows(dbconn, sql, [modelId])

   # validate result
   if result == None:
      return None
   
   # itemize tupled result
   itemized = []
   
   for item in result:
      itemized.append(Drives(item[0], item[1], item[2]))#(self, modelId, carId, name)
   return itemized

##################################################################
#
# get_certain_rents_list:
#
# returns car_model where (Model.carId = Car.carID) 
#  Format -> ModelId, Color, Year, Transmission, CarId, Brand
def get_certain_rents_list(dbconn,carId):
   # query to fetch details of all car_model
   sql = """ SELECT R.rentId, R.date, R.email, R.name, R.modelId, R.carId
              FROM Rent AS R
              WHERE R.carId = %s
         """

   # retrieve result from datatier
   result = datatier.select_n_rows(dbconn, sql, [carId])

   # validate result
   if result == None:
      return None
   
   # itemize tupled result
   itemized = []
   
   for item in result: # rentId, date, email, name, modelId, carId):
      itemized.append(Rent(item[0], item[1], item[2], item[3], item[4], item[5]))
   return itemized


##################################################################
#
# get_certain_rents_list2:
#
# returns 
#  Format -> ModelId, Color, Year, Transmission, CarId, Brand
def get_certain_rents_list2(dbconn,driverName):
   # query to fetch details of all car_model
   sql = """ SELECT R.rentId, R.date, R.email, R.name, R.modelId, R.carId
              FROM Rent AS R
              WHERE R.name = %s
         """

   # retrieve result from datatier
   result = datatier.select_n_rows(dbconn, sql, [driverName])

   # validate result
   if result == None:
      return None
   
   # itemize tupled result
   itemized = []
   
   for item in result: # rentId, date, email, name, modelId, carId):
      itemized.append(Rent(item[0], item[1], item[2], item[3], item[4], item[5]))
   return itemized

##################################################################
#
# get_certain_rents_list3:
#
# returns 
#  Format -> ModelId, Color, Year, Transmission, CarId, Brand
def get_certain_rents_list3(dbconn,modelId):
   # query to fetch details of all car_model
   sql = """ SELECT R.rentId, R.date, R.email, R.name, R.modelId, R.carId
              FROM Rent AS R
              WHERE R.modelId = %s
         """

   # retrieve result from datatier
   result = datatier.select_n_rows(dbconn, sql, [modelId])

   # validate result
   if result == None:
      return None
   
   # itemize tupled result
   itemized = []
   
   for item in result: # rentId, date, email, name, modelId, carId):
      itemized.append(Rent(item[0], item[1], item[2], item[3], item[4], item[5]))
   return itemized

##################################################################
#
# delete_certain_drives:
#
# returns car_model where (Model.carId = Car.carID) 
#  Format ->
def delete_certain_drives(dbconn,carId):
   # query to fetch details of all car_model
   sql = """ DELETE FROM Drives WHERE carId = %s """

   # call datatier function to perform action
   changes = datatier.perform_action(dbconn, sql, [carId])

   if changes >= 1:
      return 1
   else:
      return 0
   
##################################################################
#
# delete_certain_drives2:
#
# returns car_model where (Model.carId = Car.carID) 
#  Format ->
def delete_certain_drives2(dbconn,driverName):
   # query to fetch details of all car_model
   sql = """ DELETE FROM Drives WHERE name = %s """

   # call datatier function to perform action
   changes = datatier.perform_action(dbconn, sql, [driverName])

   if changes >= 1:
      return 1
   else:
      return 0

##################################################################
#
# delete_certain_rents:
#
# returns car_model where (Model.carId = Car.carID) 
#  Format -> 
def delete_certain_rents(dbconn,carId):
   # query to fetch details of all car_model
   sql = """ DELETE FROM Rent WHERE carId = %s """

   # call datatier function to perform action
   changes = datatier.perform_action(dbconn, sql, [carId])

   if changes >= 1:
      return 1
   else:
      return 0
   
##################################################################
#
# delete_certain_rents2:
#
# returns car_model where (Model.carId = Car.carID) 
#  Format -> 
def delete_certain_rents2(dbconn,driverName):
   # query to fetch details of all car_model
   sql = """ DELETE FROM Rent WHERE name = %s """

   # call datatier function to perform action
   changes = datatier.perform_action(dbconn, sql, [driverName])

   if changes >= 1:
      return 1
   else:
      return 0
   
#################################################################
#
# delete_certain_rents3:
#
# returns car_model where (Model.carId = Car.carID) 
#  Format -> 
def delete_certain_rents3(dbconn,modelId):
   # query to fetch details of all car_model
   sql = """ DELETE FROM Rent WHERE modelId = %s """

   # call datatier function to perform action
   changes = datatier.perform_action(dbconn, sql, [modelId])

   if changes >= 1:
      return 1
   else:
      return 0

##################################################################
#
# delete_certain_driver_reviews:
#
# returns car_model where (Model.carId = Car.carID) 
#  Format -> 
def delete_certain_driver_reviews(dbconn,driverName):
   # query to fetch details of all car_model
   sql = """ DELETE FROM Review WHERE name = %s """

   # call datatier function to perform action
   changes = datatier.perform_action(dbconn, sql, [driverName])

   if changes >= 1:
      return 1
   else:
      return 0
   
##################################################################
#
# get_review_count:
#
# returns car_model where (Model.carId = Car.carID) 
#  Format -> ModelId, Color, Year, Transmission, CarId, Brand
def get_certain_car_model_list(dbconn,carId):
   # query to fetch details of all car_model
   sql = """ SELECT M.modelId, M.color, M.year, M.transmission, C.carId, C.brand
              FROM Model AS M
              INNER JOIN Car AS C
              USING (carid)
              WHERE C.carId = %s
         """

   # retrieve result from datatier
   result = datatier.select_n_rows(dbconn, sql, [carId])

   # validate result
   if result == None:
      return None
   
   # itemize tupled result
   itemized = []
   
   for item in result:
      itemized.append(Car_Model(item[0], item[1], item[2], item[3], item[4], item[5]))
   return itemized

##################################################################
#
# get_review_count:
#
# returns review count of Review Table

def get_review_count(dbconn):
   # query to fetch details of all car_model
   sql = """ SELECT *
              FROM Review
         """

   # retrieve result from datatier
   result = datatier.select_n_rows(dbconn, sql, [])

   if result == None:
      return 0
   
   # if list is empty return error message
   if len(result) == 0:
      return 0 
   
   return len(result)


##################################################################
#
# get_available_car_model_list:
#
# returns car_model list where 
# ( (modelId,carId) NOT IN Rent on Date AND HAS at least 1 available Driver) 
#  
def get_available_car_model_list(dbconn, date):
   # query to fetch details 
   sql = """
            SELECT M.modelId, M.color, M.year, M.transmission, C.carId, C.brand
            FROM Model AS M
            INNER JOIN Car AS C ON M.carId = C.carId
            WHERE
               NOT EXISTS (
                     SELECT 1
                     FROM Rent AS R
                     WHERE R.date = %s
                     AND R.modelId = M.modelId
                     AND R.carId = M.carId
               )
               AND EXISTS (
                     SELECT 1
                     FROM Driver AS D
                     INNER JOIN Drives AS DR ON D.name = DR.name
                     WHERE DR.modelId = M.modelId
                     AND NOT EXISTS (
                        SELECT 1
                        FROM Rent AS R2
                        WHERE R2.date = %s
                           AND D.name = R2.name
                     )
               )
         """
   # retrieve result from datatier
   result = datatier.select_n_rows(dbconn, sql, [date, date])

   # validate result
   if result == None:
      return None
   
   # itemize tupled result
   itemized = []
   
   for item in result:
      itemized.append(Car_Model(item[0], item[1], item[2], item[3], item[4], item[5]))
   return itemized


##################################################################
#
# get_available_drivers_list:
#
# returns drivers available for rent who can drive ( (modelId, carId) on Date)
#
def get_available_drivers_list(dbconn, date, modelId, carId):
   # query to fetch details of drivers that match criteria
   sql = """
            SELECT D.name, D.road, D.number, D.city
            FROM Driver AS D
            INNER JOIN DRIVES AS DR
            ON ( D.name = DR.name AND DR.modelId = %s  AND DR.carId = %s )
            WHERE
               NOT EXISTS (
                     SELECT 1
                     FROM
                     RENT AS R
                     WHERE R.date = %s AND
                           R.modelId = DR.modelId AND
                           R.carId = DR.carId
               )
         """
   
   # retrieve result from datatier
   result = datatier.select_n_rows(dbconn, sql, [modelId, carId, date])

   # validate result
   if result == None:
      return None
   
   # itemize tupled result
   itemized = []
   
   for item in result:
      itemized.append(Driver(item[0], item[1], item[2], item[3]))
   return itemized


##################################################################
#
# register_manager:
#
# Inserts a new manager into manager table adding their information with (name, ssn, email) 
#
# Returns: 1 if the manager was successfully added,
#          0 if an internal error occurred.
#
def register_manager(dbConn, name, ssn, email):
   
   # query to perform insert action
   sql = """ INSERT INTO Manager (name, ssn, email)
	            VALUES ( %s, %s, %s )
         """

   # call datatier function to perform action
   changes = datatier.perform_action(dbConn, sql, [name, ssn, email])

   if changes == 1:
      return 1
   else:
      return 0
   

##################################################################
#
# register_driver:
#
# Inserts a new driver into driver table adding driver
# information with (name, road, number, city) 
#
# Returns: 1 if the driver was successfully added,
#          0 if an internal error occurred.
#
def register_driver(dbConn, name, road, number, city):
   
   # query to perform insert action
   sql = """ INSERT INTO Driver (name, road, number, city)
	            VALUES ( %s, %s, %s, %s )
         """

   # call datatier function to perform action
   changes = datatier.perform_action(dbConn, sql, [name, road, number, city])

   if changes == 1:
      return 1
   else:
      return 0


##################################################################
#
# remove_driver:
#
# Remove a driver from driver table of information (name) 
#
# Returns: 1 if the driver was successfully removed,
#          0 if an internal error occurred.
#
def remove_driver(dbConn, name):
   
   # query to perform delete action
   sql = """ DELETE FROM Driver WHERE name = %s """

   # call datatier function to perform action
   changes = datatier.perform_action(dbConn, sql, [name])

   if changes == 1:
      return 1
   else:
      return 0

##################################################################
#
# get_top_k_clients_by_rents:
#
# Returns: Top_Client list of the top-k clients with 
# respect to the number of rents they have booked.
#
def get_top_k_clients_by_rents(dbConn, k):
   # query to fetch details of all top k clients
   sql = """
      SELECT Client.name,Client.email,COUNT(Client.email)
      FROM Rent JOIN Client ON (Rent.email = Client.email)
      GROUP BY Client.name,Client.email
      ORDER BY COUNT(Client.email) DESC,email ASC
      LIMIT %s
   """

   result = datatier.select_n_rows(dbConn, sql, [k])
   
   # validate result
   if result == None:
      return None
   
   # itemize tupled result
   itemized = []
   
   for item in result:
      itemized.append(Top_Client(item[0], item[1], item[2]))
   return itemized

##################################################################
#
# get_model_rent_counts:
#
# Returns: Car_Model_Usage list containing every current car model 
# and the number of rents it has been used
#
def get_model_rent_counts(dbConn):
   # query to fetch details of all model rents
   sql = """
            SELECT M.modelId, M.color, M.year, M.transmission,
                  M.carId, C.Brand, COUNT(R.rentId) AS rentcount
            FROM Model AS M 
            INNER JOIN Car AS C ON C.carId = M.carId
            LEFT JOIN Rent AS R ON R.modelId = M.modelId
                                 AND R.carId = M.carId
            GROUP BY M.modelId, M.color, M.year, M.transmission, M.carId, C.Brand;
         """
   
   result = datatier.select_n_rows(dbConn, sql, [])
   
   # validate result
   if result == None:
      return None
   
   # itemize tupled result
   itemized = []
   
   for item in result:
      itemized.append(Car_Model_Usage(item[0], item[1], item[2], item[3],
                                 item[4], item[5], item[6]))
   return itemized


def get_driver_usage_stats(dbConn):
   # query to fetch details about driver usage stats
   sql = """
      SELECT Driver.name, COUNT(Rent.rentid) AS rentcount, AVG(Review.Rating)
      FROM Driver
      LEFT JOIN Review ON(Driver.name = Review.name) LEFT JOIN Rent ON (Rent.name = Driver.name) 
      GROUP BY Driver.name;
   """
   return datatier.select_n_rows(dbConn, sql)


##################################################################
#
# get_clients_by_cities:
#
# Returns: Client list containing every client from city_1 
#          who has booked a rent with driver from city_2 
#
def get_clients_by_cities(dbConn, city_1, city_2):
   sql = """ 
      SELECT DISTINCT Client.email, Client.name
      FROM Rent JOIN ClientAddress ON (Rent.email = ClientAddress.email)
      JOIN Driver ON (Rent.name = Driver.name) 
      JOIN Client ON (Rent.email = Client.email)
      WHERE ClientAddress.city = %s 
            AND Driver.city = %s;
   """
   result = datatier.select_n_rows(dbConn, sql, [city_1, city_2])
   
   # validate result
   if result == None:
      return None
   
   # itemize tupled result
   itemized = []
   
   for item in result:
      itemized.append(Client(item[0], item[1]))
   return itemized


   
##################################################################
#
# register_client:
#
# Inserts a new client into Client table adding client
# information with (email,name)
#
# Returns: 1 if the client was successfully added,
#          0 if an internal error occurred.
#
def register_client(dbConn, email, name):
   
   # query to perform insert action
   sql = """ INSERT INTO Client (email, name)
	            VALUES ( %s, %s )
         """

   # call datatier function to perform action
   changes = datatier.perform_action(dbConn, sql, [email,name])

   if changes == 1:
      return 1
   else:
      return 0
   
##################################################################
#
# remove_client:
#
# Remove a client from client table with information (email) 
#
# Returns: 1 if the client was successfully removed,
#          0 if an internal error occurred.
#
def remove_client(dbConn, email):
   
   # query to perform delete action
   sql = """ DELETE FROM Client WHERE email = %s """

   # call datatier function to perform action
   changes = datatier.perform_action(dbConn, sql, [email])

   if changes == 1:
      return 1
   else:
      return 0
   

##################################################################
#
# add_address:
#
# Inserts a new address into address table adding the 
# address information with (road, number, city) 
#
# Returns: 1 if the address was successfully added,
#          0 if an internal error occurred.
#
def add_address(dbConn, road, number, city):
   
   # query to perform insert action
   sql = """ INSERT INTO Address (road, number, city)
               VALUES ( %s, %s, %s )
         """

   # call datatier function to perform action
   changes = datatier.perform_action(dbConn, sql, [road, number, city])

   if changes == 1:
      return 1
   else:
      return 0
   
##################################################################
#
# add_review:
#
# Inserts a new review into review table adding the 
# address information with (message, rating, name, email) 
#
# Returns: 1 if the review was successfully added,
#          0 if an internal error occurred.
#
def add_review(dbConn, message, rating, name, email):
   
   # query to perform insert action
   sql = """ INSERT INTO Review ( message, rating, name, email)
               VALUES ( %s, %s, %s, %s )
         """

   # call datatier function to perform action
   changes = datatier.perform_action(dbConn, sql, 
                                     [message, rating, name, email])

   if changes == 1:
      return 1
   else:
      return 0
   
##################################################################
#
# add_client_address:
#
# Inserts a new client address into Clientaddress table adding the 
# address information with (email, road, number, city)
#
# Returns: 1 if the clientaddress was successfully added,
#          0 if an internal error occurred.
#
def add_client_address(dbConn, email, road, number, city):
   
   # query to perform insert action
   sql = """ INSERT INTO ClientAddress (email, road, number, city)
               VALUES ( %s, %s, %s, %s )
         """

   # call datatier function to perform action
   changes = datatier.perform_action(dbConn, sql, [email, road, number, city])

   if changes == 1:
      return 1
   else:
      return 0
    

##################################################################
#
# remove_client_address:
#
# Remove a client address from ClientAddress table with information (email) 
#
# Returns: 1 or n number of clientAddress that was successfully removed,
#          0 if an internal error occurred.
#
def remove_client_address(dbConn, email):
   
   # query to perform delete action
   sql = """ DELETE FROM ClientAddress WHERE email = %s """

   # call datatier function to perform action
   changes = datatier.perform_action(dbConn, sql, [email])

   if changes == 1:
      return 1
   elif changes > 1:
      return changes
   else:
      return 0
   

##################################################################
#
# add_credit_card:
#
# Inserts a new credit card into CreditCard table adding the 
# address information with (cardnum, email, road, number, city)
#
# Returns: 1 if the creditcard was successfully added,
#          0 if an internal error occurred.
#
def add_credit_card(dbConn, cardnum, email, road, number, city):
   
   # query to perform insert action
   sql = """ INSERT INTO CreditCard (cardnum, email, road, number, city)
               VALUES ( %s, %s, %s, %s, %s )
         """

   # call datatier function to perform action
   changes = datatier.perform_action(dbConn, sql, [cardnum, email, road, number, city])

   if changes == 1:
      return 1
   else:
      return 0
   

##################################################################
#
# update_driver_address:
#
# Update driver address into driver table adding the 
# address information with (name, road, number, city) 
#
# Returns: 1 if the address was successfully updated,
#          0 if an internal error occurred.
#
def update_driver_address(dbConn, road, number, city, name):
   
   # query to perform insert action
   sql = """ UPDATE Driver 
             SET road = %s, number = %s, city = %s
             WHERE name = %s
         """

   # call datatier function to perform action
   changes = datatier.perform_action(dbConn, sql, [road, number, city, name])

   if changes == 1:
      return 1
   else:
      return 0
   

##################################################################
#
# add_car:
#
# Inserts a new car into car table adding the car information with (cardId, brand) 
#
# Returns: 1 if the car was successfully added,
#          0 if an internal error occurred.
#
def add_car(dbConn, carId, brand):
   
   # query to perform insert action
   sql = """ INSERT INTO Car (carId, brand)
               VALUES ( %s, %s )
         """

   # call datatier function to perform action
   changes = datatier.perform_action(dbConn, sql, [carId, brand])

   if changes == 1:
      return 1
   else:
      return 0
   
##################################################################
#
# delete_car:
#
# Delete a car from car table using car primary key (carId)
#
# Returns: 1 if the car was successfully deleted,
#          0 if an internal error occurred.
#
def delete_car(dbConn, carId):
   
   # query to perform delete action
   sql = """ DELETE FROM Car WHERE carId = %s """

   # call datatier function to perform action
   changes = datatier.perform_action(dbConn, sql, [carId])

   if changes == 1:
      return 1
   else:
      return 0
   

##################################################################
#
# add_model:
#
# Inserts a new car model into model table adding the model information ->
# with (modelId, color, year, transmission, carId)
 
#
# Returns: 1 if the model was successfully added,
#          0 if an internal error occurred.
#
def add_model(dbConn, modelId, color, year, transmission, carId):
   
   # query to perform insert action
   sql = """ INSERT INTO Model (modelId, color, year, transmission, carId)
               VALUES ( %s, %s, %s, %s, %s )
         """

   # call datatier function to perform action
   changes = datatier.perform_action(dbConn, 
                                     sql, 
                                     [modelId, color, year, transmission, carId])

   if changes == 1:
      return 1
   else:
      return 0
   
##################################################################
#
# delete_model:
#
# Delete a car model from model table using model primary key (modelId, carId)
#
# Returns: 1 if the model was successfully deleted,
#          0 if an internal error occurred.
#
def delete_model(dbConn, modelId, carId):
   
   # query to perform delete action
   sql = """ DELETE FROM Model WHERE modelId = %s AND carId = %s """

   # call datatier function to perform action
   changes = datatier.perform_action(dbConn, sql, [modelId,  carId])

   if changes == 1:
      return 1
   else:
      return 0
   
##################################################################
#
# delete_all_model:
#
# Delete all car models from model table using carId
#
# Returns: 1 if the model was successfully deleted,
#          0 if an internal error occurred.
#
def delete_all_model(dbConn, carId):
   
   # query to perform delete action
   sql = """ DELETE FROM Model WHERE carId = %s """

   # call datatier function to perform action
   changes = datatier.perform_action(dbConn, sql, [carId])

   if changes >= 1:
      return 1
   else:
      return 0
   

##################################################################
#
# add_driver_model:
#
# Inserts a model which a driver can drive in driver table 
# add the drives information with  (modelId, carId, name) 
#
# Returns: 1 if the relationship was successfully added,
#          0 if an internal error occurred.
#
def add_driver_model(dbConn, modelId, carId, name):
   
   # query to perform insert action
   sql = """ INSERT INTO Drives (modelId, carId, name)
                VALUES ( %s, %s, %s )
         """

   # call datatier function to perform action
   changes = datatier.perform_action(dbConn, sql, [modelId, carId, name])

   if changes == 1:
      return 1
   else:
      return 0
   

##################################################################
#
# add_rent:
#
# Inserts a rent detail in rent table 
# add the rent detail information with ->
#              ([AUTO_GENERATED], date, email, name, modelId, carId)
#
# Returns: 1 if the rent was successfully added,
#          0 if an internal error occurred.
#
def add_rent(dbConn, date, client_email, driver_name, modelId, carId):
   
   # query to perform insert action
   sql = """ INSERT INTO Rent 
               ( date, email, name, modelId, carId)
               VALUES ( %s, %s, %s, %s, %s )
         """

   # call datatier function to perform action
   changes = datatier.perform_action(dbConn, sql, 
                                     [date, client_email, driver_name, modelId, carId])

   if changes == 1:
      return 1
   else:
      return 0

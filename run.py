"""
Import gspread in order to update google spreadsheet
"""
import gspread
from google.oauth2.service_account import Credentials
import time # import for timestamp
from datetime import date,datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Ice-creams")
flavours = SHEET.worksheet("flavours")

#flavours = SHEET.worksheet("flavours")
#order = SHEET.worksheet("order")

# create a list of the customers order
customer_order = []
price = []
flavour = flavours.col_values(1)[1:]  #list of flavours listed in the spreadsheet

# date and time generated for receipt generated by receipt function
today = date.today()
now = datetime.now()

""" 
function to welcome customer.
"""
def start_order():
    print("Hi, Welcome to The Inside Scoop.")
    print("Would you like to place and order?")
    question1 = input("Please enter yes or no.")
    if question1 == "yes":
        place_order()
    elif question1 == "no":
        print("Ok, let me know when you have decided.")
        start_order()
    else:
        print("Sorry invalid entry.")
        print("Plese enter yes or no.")
        start_order()
        
"""
Function to start order requesting if they would like a cone or cup.
"""
def place_order():
    print("Would you like your ice cream in a cone or a cup?")
    question2 = input("Please enter cone or cup.")
    if question2 == "cup":
        print("cup it is")
        customer_order.append("cup")
        number_scoops()
    elif question2 == "cone":
        print("cone it is")
        customer_order.append("cone")
        number_scoops()
    else:
        print("Sorry invalid entry.")
        print("Plese enter cup or cone.")
        place_order()

def number_scoops():
    scoops = int(input("How many scoops? Enter 1 ,2 or 3"))
    if scoops == 1:
        print("Ok, one scoop")
        customer_order.append("One scoop")
        price.apend(2.00)
        flavour_choice()
    elif scoops == 2:
        print("Ok, two scpops it is.")
        customer_order.append("Two scoops")
        price.append(3.00)
        flavour_choice()
    elif scoops == 3:
        print("Ok, three scpops it is.")
        customer_order.append("Three scoops")
        price.append(4.00)
        flavour_choice()
    else:
        print("Sorry invalid entry.")
        number_scoops()

def flavour_choice():
    """ 
    Shows the list of flavours available from the gsheet.
    """
    print("What flavours would you like?")
    print(flavour)


   




start_order()

print(customer_order)
print(price)
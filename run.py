"""
Import gspread in order to update google spreadsheet
"""
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate  # import modale to create a tables for flavours
import time   # import for timestamp
from datetime import date, datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("CREDS.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Ice-creams")
flavours = SHEET.worksheet("flavours")

#  order = SHEET.worksheet("order")

# create a list of the customers order
customer_order = []
price = []
scoops = []
#flavour = flavours.col_values(1)  #  List of flavours in spreadsheet



# date and time generated for receipt generated by receipt function
today = date.today()
now = datetime.now()

def start_order():
    """
    Function to welcome the customer and ask if they would like to order.
    """
    print("Hi, Welcome to The Inside Scoop")
    print("Would you like to place and order?")
    question1 = input("Please enter yes or no.")
    if question1.lower() == ("yes"):
        place_order()
    elif question1.lower() == ("no"):
        print("Ok, let me know when you have decided.")
        start_order()
    else:
        print("Sorry invalid entry.")
        print("Plese enter yes or no.")
        start_order()
        

def place_order():
    list = []
    choice = True
    while True:
        holder = input("What would you like a cup or a cone?").lower()
        if holder in ("cup","cone"):
            number_scoops()
            append.customer_order[holder]
            break
            
        else:
            holder = input("incorrect input....\n Please select cup or cone").lower()

def number_scoops():
    scoops = int(input("How many scoops? Enter 1, 2 or 3"))
    if scoops == 1:
        print("Ok, one scoop")
        customer_order.append("One scoop.")
        price.append(2.00)
        flavour_choice()
    elif scoops == 2:
        print("Ok, two scoops it is.")
        customer_order.append("two scoops")
        price.append(3.00)
        flavour_choice()
    elif scoops == 3:
        print("ok, Three scoops it is.")
        price.append(4.00)
        flavour_choice()
    else:
        print("Sorry invalid entry.")
        number_scoops()
        return(scoops)

def flavour_choice():
    """
    Create a list of flavours using tabulate modal so the user can
    choose easily.
    """
    list = []
    choice = True
    while True:
        flavour = input("Please choose the corrisponding flavour number 1, 2, 3, 4, 5, 6,").int()
        if flavour in ("1", "2", "3", "4", "5", "6"):
            break
        else:
            flavour = input("incorrect input....\n Please select from").int()
    #print(flavour)
    #list = [item for item in input(f"Choose your flavours.").split()]
    #print(list)
    all_rows = flavours.get_all_values()
    print(all_rows)
    


def populate_receipt_worksheet(data):
    """ 
    update the receipt worksheet with the order the customer made
    """
    SHEET_receipt.append_row([date,time, question2, scoops, list])
    print("would you like a receipt?")
    receipt_worksheet = SHEET.worksheet("receipt")
    receipt_worksheet.append_row(data)
    print("reciept ready to print")

start_order()

print(f"That will be a total of €{price}")
print(customer_order)
retrun(populate_receipt_worksheet)

"""
Import gspread in order to update google spreadsheet
"""
import gspread
from google.oauth2.service_account import Credentials
import time # import for timestamp

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

flavours = flavours.get_all_values()

print(flavours)
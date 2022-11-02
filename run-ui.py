import gspread
from colorama import Fore, Style
from csvAPI import api
import time
import variables as var
from gspread_formatting import *

userinput = input(f"{Fore.BLUE}Select 1 for Navy Federal Credit Union.{Fore.GREEN}\nSelect 2 for Paypal.{Style.RESET_ALL}\n") # add color

sa = gspread.service_account()
sh = sa.open("Personal Finances")
wks = sh.worksheet('raw')
# wks = sh.worksheet(f"{var.MONTH}")
rows = []
lines = 0 

fmt = cellFormat(
    numberFormat={'type':'CURRENCY'},
    horizontalAlignment='RIGHT'
    )

def linecounter(file):
    with open(file, mode='r') as fp:
        linecount = len(fp.readlines())
        return linecount

if userinput == "1":
    print("Checking NFCU!")
    api.readNFCU()
    linecount = linecounter(var.nfcu_file)
    rows = api.readNFCU()
    for row in rows:
        if lines < linecount:
            wks.insert_row([row[0], row[1], row[2], row[3]], 7, inherit_from_before=True)
            time.sleep(2)
            lines += 1
            print(lines)
            print('linecount '+ str(linecount))
    format_cell_range(wks, 'D2:D', fmt)
    print("Format Succesfull!")

elif userinput == "2":
    print("Checking Paypal!")
    api.readPaypal()
    linecount = linecounter(var.paypal_file)
    rows = api.readPaypal()
    for row in rows:
        if lines < linecount:
            wks.insert_row([row[0], row[1], row[2], row[3]], 7, inherit_from_before=True)
            time.sleep(2)
            lines += 1
else:
    print("Invalid input!")
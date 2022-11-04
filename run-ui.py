import gspread
from rich import print
from rich.prompt import Prompt
from csvAPI import api
import time
import variables as var
from gspread_formatting import *

userinput = Prompt.ask(f"[blue]Select 1 for Navy Federal Credit Union.\n[green]Select 2 for Paypal.\n") 

sa = gspread.service_account()
sh = sa.open("Personal Finances")
wks = sh.worksheet('raw')
# wks = sh.worksheet(f"{var.MONTH}")
rows = []
lines = 0 

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
            wks.insert_row([row[0], row[1], row[2], row[3]], 7)
            time.sleep(2)
            lines += 1
            print(f'Transaction {lines} imported out of {linecount}')
    wks.format('D2:D',{"numberFormat": {'type':'CURRENCY'}})
    print("Formatting Succesfull!")

elif userinput == "2":
    print("Checking Paypal!")
    api.readPaypal()
    linecount = linecounter(var.paypal_file)
    rows = api.readPaypal()
    for row in rows:
        if lines < linecount:
            wks.insert_row([row[0], row[1], row[2], row[3]], 7)
            time.sleep(2)
            lines += 1
            print(f'Transaction {lines} imported out of {linecount}')
    wks.format('D2:D',{"numberFormat": {'type':'CURRENCY'}})
    print("Formatting Succesfull!")
            
else:
    print("[red]Invalid input!")
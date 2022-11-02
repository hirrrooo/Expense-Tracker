import variables as var
import csv

class api:
    def categorizer(name):
        if any(name.casefold() in var.deposits for name in name.split()):
            category = "Deposits"
            return category
        elif any(name.casefold() in var.transfer for name in name.split()):
            category = "Bank Transfer"
            return category
        elif any(name.casefold() in var.paypal_payin4 for name in name.split()):
            category = "Paypal Pay in 4"
            return category
        elif any(name.casefold() in var.paypal for name in name.split()):
            category = "Paypal Transfer"
            return category
        elif any(name.casefold() in var.gas for name in name.split()):
            category = "Gas"
            return category
        elif any(name.casefold() in var.shopping for name in name.split()):
            category = "Shopping"
            return category
        elif any(name.casefold() in var.subscriptions for name in name.split()):
            category = "Subscription"
            return category
        elif any(name.casefold() in var.wegmans for name in name.split()):
            category = "Wegmans"
            return category
        elif any(name.casefold() in var.food for name in name.split()):
            category = "Food"
            return category
        elif any(name.casefold() in var.Investing for name in name.split()):
            category = "Investments"
            return category
        else:
            category = "Other"
            return category

    def readNFCU():
        with open(var.nfcu_file, mode='r') as csv_file: 
            csv_reader = csv.reader(csv_file)
            for row in reversed(list(csv_reader)):
                date = row[0]
                name = row[2]
                debit = row[3]
                credit = row[4]
                if debit == '':
                    debit = 0
                else:
                    credit = 0
                net = (-(float(debit)))+float(credit)
                category = api.categorizer(name)
                transaction = ((date, name, category, str(net))) 
                print(transaction)
                var.transactions.append(transaction)
            return var.transactions
                
# NFCU .csv
# "Date","No.","Description","Debit","Credit"
# Column 0 is Date
# Column 1 is empty
# Column 2 is Name
# Column 3 is Debit
# Column 4 is Credit

    def readPaypal():
        with open(var.paypal_file, mode='r') as csv_file: 
            csv_reader = csv.reader(csv_file)
            for row in reversed(list(csv_reader)):
                date = row[0]
                name = row[3]
                net = row[9]
                category = api.categorizer(name)
                transaction = ((date, name, net, category)) 
                print(transaction)
                var.transactions.append(transaction)
            return var.transactions
# paypal.csv
# Column 0 is Date
# Column 1 is Time
# Column 2 is Timezone
# Column 3 is Name
# Column 4 is Type (ie; Express Checkout Payment, General Card Deposit, Paypal Buyer Credit Payment Funding)
# Column 5 is Status (ie; Pending/Complete)
# Column 6 is Currency Type
# Column 7 is Gross
# Column 8 is Fee
# Column 9 is Net (Overall)
# Column 10 is Receipt ID 
# Column 11 Is Balance
# Column 12 is Tip
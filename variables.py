from pathlib import Path

data_folder = Path('.csv')
MONTH = 'Oct'
transactions = []

nfcu_file = data_folder / f'NFCU_{MONTH}.csv'
paypal_file = data_folder / 'paypal.csv'


deposits = {'deposit'}
transfer = {'transfer'}
paypal = {'inst'}
Investing = {'robinhood'}
paypal_payin4 = {'payin'}
gas = {'fuel', 'gas', 'oil'}
wegmans = {'wegmans','teamworldi'}
shopping = {'amzn', 'amzncom', 'amzn mktp','ebay'}
subscriptions = {'twitch', 'discord', 'adobe', 'google','spotify','ppadobe'}
food = {'aramark','cook out','cava','grubhub','starbucks','molly','chipotle','taco','domoishi', 'cain', 'bonchon', 'greek','indian','7-eleven','grubhub-chick-fil-'}
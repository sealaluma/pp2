from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(1)
tomorrow = today + timedelta(1)

print("Yesterday was ", yesterday.strftime('%d-%m-%Y'))
print ("Today is " + today.strftime('%d-%m-%Y'))
print ("Tomorrow wiil be " + tomorrow.strftime('%d-%m-%Y'))
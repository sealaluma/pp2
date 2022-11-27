from datetime import datetime, timedelta

today = datetime.now()
past = today - timedelta(5)

print(past.strftime('%d-%m-%Y'))

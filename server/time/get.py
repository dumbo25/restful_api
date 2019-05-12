global Data
# returns date and time on server
now = datetime.datetime.now()
Data = {"date" : str(now.month) + "/" + str(now.day) + "/" + str(now.year), "time" : str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)}


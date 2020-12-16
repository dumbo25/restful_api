global Data
# returns CPU stats
Data = {"cores" : str(psutil.cpu_count()), "frequency" : str(round(psutil.cpu_freq().max/1000,2)) + "GHz", "used" : str(psutil.cpu_percent()) + "%" }


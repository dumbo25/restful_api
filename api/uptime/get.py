global Data
# returns uptime using:
uptime = time.time() - psutil.boot_time()
days = int(uptime / (24 * 60 * 60))
hours = int((uptime - days*(24*60*60)) / (60 * 60))
minutes = int((uptime - days*(24*60*60) - hours*(60*60)) / (60))
seconds = int(uptime - days*(24*60*60) - hours*(60*60) - minutes*(60))
Data = {"uptime" : {"days" : str(days), "hours" : str(hours), "minutes" : str(minutes), "seconds" : str(seconds)} }

global Data
# returns disk (microSD Card) usage
disk_total = str(round(psutil.disk_usage('/').total/ (1000*1000*1000),2)) + "GB"
disk_used = str(round(psutil.disk_usage('/').used/ (1000*1000*1000),2)) + "GB"
disk_free = str(round(psutil.disk_usage('/').free/ (1000*1000*1000),2)) + "GB"
Data = {"total" : disk_total, "used" : disk_used, "free" : disk_free}

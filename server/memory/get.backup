global Data
mem_free = str(round(psutil.virtual_memory().free / (1000 * 1000),2)) + "MB"
mem_used = str(round(psutil.virtual_memory().used / (1000 * 1000),2)) + "MB"
mem_total = str(round(psutil.virtual_memory().total / (1000 * 1000),2)) + "MB"
mem_avail = str(round(psutil.virtual_memory().available / (1000 * 1000),2)) + "MB"
Data = {"total" : mem_total, "used" : mem_used, "available" : mem_avail, "free" : mem_free}

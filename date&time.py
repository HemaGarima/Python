import time

print(time.time())
print(time.ctime())
# time.sleep(10)
# print(time.ctime())

print(time.localtime(time.time()))
print(time.localtime(1708020150.0))
print(time.gmtime(time.time()))
local_time = (2024 , 2 , 15 , 23 , 32 , 30 , 3 , 46 , 0)
print(time.mktime(local_time))

local_time = (2022, 7, 24, 20, 14, 39, 6, 205, 0)
print(time.asctime(local_time))

local_time = "24 July, 2022"
print(time.strptime(local_time, "%d %B, %Y"))

import calendar

print(calendar.month(2024,5))
import datetime
from datetime import timedelta
 
datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
#date1 = '2016-04-16 10:01:28.585'
#date2 = '2016-03-10 09:56:28.067'
o = datetime.datetime.now()
n = o - datetime.timedelta(hours=2, minutes=10)
o=str(o)
n=str(n)

diff = datetime.datetime.strptime(o, datetimeFormat)\
    - datetime.datetime.strptime(n, datetimeFormat)
 
print("Difference:", diff)
print("Days:", diff.days)
print("Microseconds:", diff.microseconds)
print("Seconds:", diff.seconds)

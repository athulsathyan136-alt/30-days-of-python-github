
from datetime import datetime
now = datetime.now()
print(now)
day = now.day
print(day)
month = now.month
print(month)

print()
from datetime import datetime
new = datetime(2020,2,2)
print(new)
day = new.day
print(day)
sec = new.second
print(sec)
print()
x = datetime.now()
t = x.strftime("%H:%M:%S")
print(f'time :{t}')
c = x.strftime("%Y/%m/%d")
print(f'year :{c}')

dates = "5 December, 2022"
print(dates)
f = datetime.strptime(dates,"%d %B, %Y")
print(f)

from datetime import date
f = date(2022,3,5)
print(f"cD :{f.today()}")

from datetime import time
a = time()
print(a)
b = time(10,30,55)
print(b)
print()
from datetime import date,datetime
t1 = date(year=2019,month=12,day=15)
t2 = date(year=2022,month=1,day=1)

duff = t2 - t1
print(duff)
print()
from datetime import timedelta
t1 = timedelta(weeks=12,days=12,hours=4,seconds=20)
t2 = timedelta(weeks=7,days=11,hours=1,seconds=55)
t4 = t1 - t2
print(t4)

print()
print('======EXERCISES==========')
from datetime import datetime
o = datetime.now()
c_day = o.day
print(c_day)
m = o.month
print(m)
y =o.year
print(y)
h = o.hour
print(h)
n = o.minute
print(n)


x = datetime.now()
currrent = x.strftime("%m/%d%Y ,%H:%M:%S")
print('current',currrent)

r = '5 December, 2013'
y = datetime.strptime(r,"%d %B, %Y")
print(y)

t1 = datetime(year=2027,month=1,day=1)
t2 = datetime(year=2026,month=10,day=1)
diff = t1-t2
print(f"new year :{diff}")

t3 = datetime(year=2026,month=10,day=1)
t4 = datetime(year=1970,month=1,day=1)
g = t3 - t4
print(f"differnece :{g}")
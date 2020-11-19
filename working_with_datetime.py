import datetime
import pytz

print(type(datetime))

d = datetime.date(2020, 11, 17)
print(d)

tday = datetime.date.today()

print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)
print(tday + tdelta)
print(tday - tdelta)

# date 2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2021, 7, 19)

till_bday = bday - tday
print(till_bday.total_seconds())


t = datetime.time(9, 30, 45, 100000)
print(t)
print(t.hour)

dt = datetime.datetime(2020, 11, 17, 9, 10, 45, 100000)
print(dt)

dt_today = datetime.datetime.now()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

dt_aware = datetime.datetime(2020, 11, 17, 11, 55, tzinfo=pytz.UTC)
print("Time Zone Aware: ", dt_aware)

dt_now = datetime.datetime.now(tz=pytz.UTC)
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_now)
print(dt_utcnow)


dt_mtn = dt_now.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

dt_samoa = dt_now.astimezone(pytz.timezone('Pacific/Samoa'))
print(dt_samoa)

import datetime
import pytz

#variables
tz_india = pytz.timezone("Asia/Calcutta")

#main
print("=================================")
print("          current time")
print("=================================")
print("Hour:",datetime.datetime.now(tz=tz_india).hour)
print("Min:",datetime.datetime.now(tz=tz_india).minute)
print("=================================")
print("   Notice: this in 24h format")
print("=================================")
hour = int(input("Hour : "))
minute = int(input("Min : "))
msg = str(input("message : "))
while 1==1:
  if hour == datetime.datetime.now(tz=tz_india).hour and minute == datetime.datetime.now(tz=tz_india).minute:
    print("=================================")
    print(msg)
    print("=================================")
    break
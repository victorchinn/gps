from sense_hat import SenseHat
from datetime import datetime
from gps import *



sense = SenseHat()
session = gps() 
#session.stream(WATCH_ENABLE|WATCH_NEWSTYLE)
#report = session.next()
#print report

#while True:
for x in range(1,10):

    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    
    #print(datetime.now())
    msg = "Temperature = {0}, Pressure = {1}, Humidity = {2}".format(t,p,h)
    sense.show_message(msg, scroll_speed=0.01)
    print(datetime.now()), ('Temperature: {0} Pressure: {1} Humidity: {2}'.format(t,p,h))

    #report = session.next()
    #print report

   

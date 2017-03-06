#!/usr/bin/python
import serial
import pynmea2

lat = 0; 
lon = 0;

with serial.Serial('/dev/ttyS0', baudrate=9600, timeout=1) as ser:
    # read 10 lines from the serial output
    while(1):
        try:
            line = ser.readline().decode('ascii', errors='replace')
            #print "read :", (line.strip()),":end--"   
            print ".",
        except Exception as e:
            #print "serial port exception"
            #ignored
            pass

        try:
            #decoded = pynmea2.parse('$GPRMC,223114.000,A,4733.8824,N,12206.4382,W,0.06,275.93,050317,,,A*78')
            decoded = pynmea2.parse(line.strip())
            lat = (decoded.latitude + lat) / 2.0
            lon = (decoded.longitude + lon) / 2.0
            alt = decoded.alt
            print "\n\rLAT LON ALT:", lat,lon,alt
        except Exception as e:
            #print "Error decoding :",line.strip()
            #so ignore it if cant decode it
            pass

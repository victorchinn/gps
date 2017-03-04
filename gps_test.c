
#include<stdio.h>
#include<stdlib.h>
#include<gps.h>

int main(){
    int i = 0; 
    float Lat_avg, Lon_avg, Alt_avg, Spd_avg; 

    gps_init();                   // initialize the device
    loc_t gps;                    // a location structure


    // get the initial GPS location
    gps_location(&gps);           // determine the location data
    
    Lat_avg = gps.latitude; 
    Lon_avg = gps.longitude;
    Alt_avg = gps.altitude;
    Spd_avg = gps.speed;

    for (i = 0; i <= 100; i++)
    {
        gps_location(&gps);           // determine the location data
        Lat_avg = (Lat_avg + gps.latitude)/2.0;
        Lon_avg = (Lon_avg + gps.longitude)/2.0;
        Alt_avg = (Alt_avg + gps.altitude)/2.0;
        Spd_avg = (Spd_avg + gps.speed)/2.0;

        printf("The RPi location is (%lf,%lf) ", Lat_avg, Lon_avg);
        printf("Altitude: %lf m. Speed: %lf knots\n", Alt_avg, Spd_avg);
    }
    
    return 0;
}
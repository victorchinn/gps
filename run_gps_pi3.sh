#!/bin/bash
sudo systemctl stop serial-getty@ttyS0
sudo systemctl disable serial0getty@ttyS0
sudo python read_serial_gps-pi3.py
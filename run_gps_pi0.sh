#!/bin/bash
sudo systemctl stop serial-getty@ttyAMA0
sudo systemctl disable serial-getty@ttyAMA0
sudo python read_serial_gps-pi0.py
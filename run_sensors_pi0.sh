#!/bin/python
sudo systemctl stop serial-getty@ttyAMA0
sudo systemctl disable serial-getty@ttyAMA0
sudo python sense.py
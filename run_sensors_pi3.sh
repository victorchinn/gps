#!/bin/python
sudo systemctl stop serial-getty@ttyS0
sudo systemctl disable serial-getty@ttyS0
sudo python sense.py
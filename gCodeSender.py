#!/usr/bin/python

import serial
import time

s = serial.Serial("/dev/tty.usbserial-A505BPET", 115200)
f = open("test.nc", "r")

s.flushInput()
s.write("G1 X100".encode())
s.readline()

f.close()
s.close()


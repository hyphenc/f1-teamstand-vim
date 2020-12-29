#!/usr/bin/python3
import signal
import sys

import Adafruit_PN532 as PN532

# dgpio connection pins for software spi
CS   = 18
MOSI = 23
MISO = 24
SCLK = 25

# handle sigints
def handle_sigint(signal, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

# pn532 connection info
pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
pn532.begin()
pn532.SAM_configuration()

while True: # while no tag -> read for tag
    uid = pn532.read_passive_target(timeout_sec=0.5)
    if uid is not None:
        break

print("Found card with UID:", [hex(i) for i in uid], "\n\nprinting contents as ascii codes:\n")

# print contents of all user data pages (4 - 222)
for page in range(5, 223): # 222 = num of user data pages
    counter = 1 # to separate the blocks with commas
    for bit in pn532.mifare_classic_read_block(page): # returns single read bits in a stream, always reads 4 blocks in total
        print(bit, end="")
        if counter % 4 == 0 and counter != 16 and counter != 1:
            print(",", end="")
        counter+=1
    print("")
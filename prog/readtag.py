#!/usr/bin/python3
# prints the contents of an ntag216 (with 222 pages à 4 bytes, i.e. 888 bytes in total)
import signal
import sys

# pylint: disable=import-error
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

print("found card with uid:", [hex(i) for i in uid], "\n\nprinting contents as ascii codes:\n")

# print contents of all pure user data pages (5 - 225)
for block in range(5, 226):
    # returns single read bytes in a stream. always reads 4 pages when given a block address
    print(f"block #{block:03}: ", end="") # print with decimal padding for better alignment

    try:
        for byte in pn532.mifare_classic_read_block(block)[0:4]:
            print(byte, end=" ")
    except TypeError:
        print("\n\nerror: couldn't finish reading the tag's contents. try holding it closer to the reader.")
        break

    print("")
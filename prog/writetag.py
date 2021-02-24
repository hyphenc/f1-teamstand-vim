#!/usr/bin/python3
# write 4 bytes of data to page of block address N
from sys import argv
from sys import exit

# pylint: disable=import-error
import Adafruit_PN532 as PN532

# check for proper usage
if(len(argv) != 3):
    print("usage:\n python3 writetag.py BLOCK_ADDRESS 4_BYTE_STRING (to write 4 bytes to BLOCK_ADDRESS)\n python3 writetag.py BLOCK_ADDRESS erase (to erase data from BLOCK_ADDRESS)")
    exit(1)

blockaddr = int(argv[1])
assert blockaddr > 4 and blockaddr < 225, "block address is not in range (valid range: 5 to 225)"

# dgpio connection pins for software spi
CS   = 18
MOSI = 23
MISO = 24
SCLK = 25

# pn532 connection info
pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
pn532.begin()
pn532.SAM_configuration()

while True: # while no tag -> read for tag
    uid = pn532.read_passive_target(timeout_sec=0.5)
    if uid is not None:
        break

print("found card with uid:", [hex(i) for i in uid], "\n")


### BEGIN: WRITE FUNCTION ###

# source: https://github.com/adafruit/Adafruit_CircuitPython_PN532/blob/master/adafruit_pn532/adafruit_pn532.py
# Adafruit PN532 NFC/RFID control library.
# Author: Tony DiCola
#
# The MIT License (MIT)
#
# Copyright (c) 2015-2018 Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

MIFARE_ULTRALIGHT_CMD_WRITE = 0xA2
COMMAND_INDATAEXCHANGE = 0x40

def ntag2xx_write_block(block_number, data):
  assert data is not None and len(data) == 4, "Data must be an array of 4 bytes!"
  # Build parameters for InDataExchange command to do NTAG203 classic write.
  params = bytearray(3 + len(data))
  params[0] = 0x01  # Max card numbers
  params[1] = MIFARE_ULTRALIGHT_CMD_WRITE
  params[2] = block_number & 0xFF
  params[3:] = data
  # Send InDataExchange request.
  response = pn532.call_function(
      COMMAND_INDATAEXCHANGE, params=params, response_length=1
  )
  return response[0] == 0x00

### END: WRITE FUNCTION ###


# create bytearray of size 4
data = bytearray(4)

if (argv[2] == "erase"):
    data[0:4] = b"\x00\x00\x00\x00"
    print(f"erasing block #{blockaddr} ...") 
else:
    assert len(argv[2]) == 4, "data must be 4 bytes long"
    data[0:4] = bytes(argv[2], encoding="ascii")
    print(f"writing '{argv[2]}' to block #{blockaddr} ...")

ntag2xx_write_block(blockaddr, data)

print( # read back block address N
    f"reading 4 blocks, beginning with block address #{blockaddr}\n(info: \\x00 is hex for NULL, i.e. no data)\n\n",
    [chr(x) for x in pn532.mifare_classic_read_block(blockaddr)],
)
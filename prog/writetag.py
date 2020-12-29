#!/usr/bin/python3
import Adafruit_PN532 as PN532

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


# select block N
block = 13
# create bytearray of size 4
data = bytearray(4)
data[0:4] = b"5678"
# write 4 byte block
ntag2xx_write_block(block, data)

# read block N
print(
    f"reading 4 blocks, beginning with block #{block}\n\n",
    [chr(x) for x in pn532.mifare_classic_read_block(block)],
)
teamstand -- ViM
=================================================

kiosk-style video player der über nfc tags (ntag216), befestigt an tokens, gesteuert wird.

------

es werden quasi 
https://github.com/adafruit/Adafruit_CircuitPython_PN532/blob/master/examples/pn532_readwrite_ntag2xx.py
und
https://github.com/adafruit/Adafruit_Python_PN532/blob/master/Adafruit_PN532/PN532.py
vereint, da die obere zwar die neuere bibliothek ist, aber anscheined nur hardware spi verbindungen unterstützt.
da die funktionen sich aber allg. sehr ähneln, kann man code aus der beiden ganz gut zusammenbasteln.




vieles macht sinn, wenn man sich das spec sheet anguckt!
https://www.nxp.com/docs/en/data-sheet/NTAG213_215_216.pdf
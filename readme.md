# teamstand — ViM

> kiosk-style video player der über nfc tags (ntag216), befestigt an tokens, gesteuert wird.

---

## info

in diesem projekt werden quasi die [neue](https://github.com/adafruit/Adafruit_CircuitPython_PN532/blob/master/examples/pn532_readwrite_ntag2xx.py)
und die [alte](https://github.com/adafruit/Adafruit_Python_PN532/blob/master/Adafruit_PN532/PN532.py) library für den adafruit pn532 vereint, da die erstere zwar die neuere bibliothek ist, aber anscheined nur hardware spi verbindungen unterstützt, wobei das vorhandene setup software spi benötigt.
da die funktionen sich aber allgemein sehr ähneln, kann man den code der beiden ganz gut zusammenbasteln.

---

das [spec sheet](https://www.nxp.com/docs/en/data-sheet/NTAG213_215_216.pdf) ist sehr hilfreich.
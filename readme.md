# teamstand - ViM

> kiosk-style video player der über nfc tags (ntag216), befestigt an tokens, gesteuert wird.

## info

in diesem projekt werden quasi die [neue](https://github.com/adafruit/Adafruit_CircuitPython_PN532/blob/master/examples/pn532_readwrite_ntag2xx.py)
und die [alte](https://github.com/adafruit/Adafruit_Python_PN532/blob/master/Adafruit_PN532/PN532.py) library für den adafruit pn532 vereint, da die erstere zwar neuer ist, aber anscheined nur hardware spi verbindungen unterstützt, wobei das vorhandene setup software spi benötigt.
da die funktionen sich aber allgemein sehr ähneln, kann man den code der beiden ganz gut zusammenbasteln.

### trivia

das vorherige team hat das mit einer custom gui in gtk gemacht. das war mir zu anstrengend und da ich wusste, dass [mpv](https://github.com/mpv-player/mpv) auch bilder "abspielen" kann und relativ anpassbar ist, machen wir das jetzt damit, also über mpvs IPC socket über python-mpv.

transitions sind schöner (mit mpv 0.29.1), wenn bilder auch als videos behandelt werden, d.h. 300ms standbild als mp4 oder so.

## was benötigt wird
* raspberry pi 3
* archlinux arm
* aur helper (yay)
* pn532 nfc rfid module v3
* ntag216 nfc tags

## dateien

### `main.py`
macht das nfc scanning & die IPC mit mpv.

### `readtag.py`
separates helper script: liest die daten der user memory section eines ntags aus.

### `writetag.py`
separates helper script: schreibt 4 bytes an daten auf eine blockadresse oder setzt die dort vorhandenen daten auf `0x0`/`NULL`.

## etc

* anmerkung: ich bin/war kein mitglied des teams.
* [supported codecs](https://ffmpeg.org/general.html#Supported-File-Formats_002c-Codecs-or-Features)
* das [ntag216 spec sheet](https://www.nxp.com/docs/en/data-sheet/NTAG213_215_216.pdf) ist sehr hilfreich.


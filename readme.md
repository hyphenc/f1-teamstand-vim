# teamstand - ViM

> kiosk-style video player der über nfc tags, befestigt an tokens, gesteuert wird.

## geplante funktionsweise
wip

## umsetzung
wip

### erstkonzept
wip

### zweitkonzept
wip


## dateien

### `main.py`
* `prog/main.py` macht das nfc scanning und kontrolliert den videplayer (mpv). hier finden sich noch bugs und teilweise fehlen noch funktionsweisen, siehe dazu die [issues](https://github.com/hyphenc/f1-teamstand-vim/issues).

### helper
* `prog/readtag.py` liest die daten der user memory section eines ntags aus.
* `prog/writetag.py` schreibt 4 bytes an daten auf eine blockadresse oder setzt die dort vorhandenen daten auf `0x0`/`NULL`.

### beispiele
* `examples/seamless-playback.py` zeigt, wie flüssig der übergang zwischen video- bzw. bilddateien ist, wenn die hardware gut genug ist.
* zuerst wird eine bilddatei gezeigt und dann zwei videos. die farben wurden invertiert, damit man sehen kann, dass eine neue datei abgespielt wird.


## how to

### komponenten
* raspberry pi 3
* archlinux arm
* aur helper (yay)
* pn532 nfc rfid module v3
* ntag216 nfc tags

### guide
* `rpi/boot-config.txt` anpassen.
* `rpi/setup-guidance.sh` nicht einfach blind ausführen. es ist eher eine rekonstruktion der genutzten/benötigten commands.
* der rest sollte offensichtlich sein, wenn man mit gnu/linux vertraut ist.


## etc

### erkenntnisse
* der raspberry pi 3b+ ist _nicht wirklich_ für 1080p >30fps videoplayback geeignet
* der raspberry pi 3b+ überhitzt gerne, aufgrund von schlechtem hardwaredesign
* ggf. stürzt er deswegen auch mal ab
* mit alten libraries aus kompatibilitätsgründen programmversionen von vor 2 jahren zu kompilieren ist... nervig

### sonstiges
* anmerkung: ich bin/war kein mitglied des teams.
* das [ntag216 spec sheet](https://www.nxp.com/docs/en/data-sheet/NTAG213_215_216.pdf) ist sehr hilfreich.

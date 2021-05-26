# Teamstand - ViM

## Geplante Funktionsweise
* Die NFC-Tags werden an verschiedenen Fahrzeugteilen befestigt.
* Wenn man ein Fahrzeugteil auf den im Stand eingebauten Sensor stellt, liest das NFC-Modul die ID vom Tag und spielt das dazugehörige Video ab.
* Wenn zwischendurch ein anderes Fahrzeugteil auf den Sensor gestellt wird, wird das aktuelle Video unterbrochen und das neue beginnt.
* Wenn ein Video endet, wird auf ein statisches Bild gewechselt.

## Umsetzung

### Konzept
Passende Bibliotheken für die vorhandene Hardware, z.B. um vom NFC-Reader Daten empfangen zu können, suchen und mit [mpv](https://github.com/mpv-player/mpv), einem open-source Videoplayer der auch Bilder anzeigen kann, in einem Pythonscript verbinden. Für das Videoplayback verschiedene Threads benutzen. Das alles auf bereits vorhandener Hardware realisieren.

### Aktueller Status

-> [Issues](https://github.com/hyphenc/f1-teamstand-vim/issues)

Zwischendurch musste ich feststellen, dass der Raspberry Pi 3b+ hardwaretechnisch zu schwach ist und _nicht wirklich_ für 1080p >20 FPS Videoplayback geeignet ist, auch wegen fehlenden Videodecoder-Treibern. Das Konzept sollte funktionieren, jedoch hat der Code noch einige Bugs.

Weil der Wettbewerb dieses Jahr digital stattfindet und der Teamstand in einem gerenderten Video vorgestellt wird, ergibt es wenig Sinn hier noch weiterzuarbeiten.

_Besonders wenn der Raspberry Pi 3b+ gerne überhitzt und abstürzt und die Verbindung dann immer abbricht... nervig_ (┛◉Д◉)┛彡┻━┻

## Dateien

### Hauptscript
* `prog/main.py` macht das NFC scanning und kontrolliert den Videoplayer (mpv). Hier finden sich noch Bugs und teilweise fehlen noch Funktionen, siehe dazu die [issues](https://github.com/hyphenc/f1-teamstand-vim/issues).

### Helper
* `prog/readtag.py` liest die Daten der user memory section eines NTAGs aus.
* `prog/writetag.py` schreibt 4 Bytes an Daten auf eine Blockadresse oder setzt die dort vorhandenen Daten auf `0x0`/`NULL`.

### Beispiele
* `examples/seamless-playback.py` zeigt, wie flüssig der Übergang zwischen Video- bzw. Bilddateien ist, wenn die Hardware gut genug ist
* Zuerst wird eine Bilddatei gezeigt und dann zwei Videos. Die Farben wurden invertiert, damit man sehen kann, dass eine neue Datei abgespielt wird (`v2-inv.mov` hat eine niedrigere Bitrate wegen ffmpeg defaults)


## How-to

### Komponenten
* Raspberry Pi 3b+
* Archlinux ARM
* AUR Helper (yay)
* PN532 NFC RFID MODULE v3
* NTAG216 NFC-Tags

### Guide
* `rpi/boot-config.txt` anpassen.
* `rpi/setup-guidance.sh` nicht einfach blind ausführen. Es ist eher eine Rekonstruktion der genutzten/benötigten commands.
* Der Rest sollte offensichtlich sein, wenn man mit GNU/Linux vertraut ist.


## Et cetera
* Anmerkung: Ich bin/war kein Mitglied des Teams.
* Das [NTAG216 specsheet](https://www.nxp.com/docs/en/data-sheet/NTAG213_215_216.pdf) ist sehr hilfreich.

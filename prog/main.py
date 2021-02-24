#!/usr/bin/python3
import sys
from threading import Thread

# pylint: disable=import-error
import mpv
import Adafruit_PN532 as PN532

# ID stored on tag <-> media file
tags = { # examples for now
    "HOME": "home",
    "REIF": "reifen",
    "CHAS": "chassis",
    "SPOI": "spoiler"
}

# at what block address the 4 byte IDs are stored
block = 6

# for keeping track of our threads
new_tid = last_tid = None
tlist = list()

# dgpio connection pins for software spi
CS   = 18
MOSI = 23
MISO = 24
SCLK = 25

# pn532 connection info
pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
pn532.begin()
pn532.SAM_configuration()

def init_player():
    # pylint: disable=unused-variable
    global player
    player = mpv.MPV(ytdl=False, input_default_bindings=False,
    fullscreen=True, keep_open=True, osd_level=0, video_osd=False,
    osc=False, input_vo_keyboard=True, cursor_autohide="always",
    demuxer_thread="yes", merge_files=True, image_display_duration="inf")

    @player.on_key_press("q")
    def q_binding():
        player.quit()

    @player.on_key_press("ESC")
    def esc_binding():
        player.quit()

def start_play_thread(filename):
    player.loadfile(filename, mode="replace")
    return # yes, it's an ugly hack to return control to the "main" thread and not stop playback
    try: # pylint: disable=unreachable
        player.wait_for_playback()
    except mpv.ShutdownError:
        pass # allow shutdown (using keyboard input) while playback

def play(filename):
# for playback we start a new thread and join (aka terminate) the previously used thread
    global last_tid # tid = thread id
    global new_tid

    new_tid = Thread(target=start_play_thread(filename))
    new_tid.start()
    tlist.append(new_tid)

    if (last_tid == None): # we don't have an old thread yet
        pass
    elif (last_tid.is_alive()):
        last_tid.join() # join old thread

    last_tid = new_tid

def readtag():
# try to read the 4 byte id from the tag and play the corresponding file
    print("found card")
    recv=""

    try:
        for byte in pn532.mifare_classic_read_block(block)[0:4]:
            recv+= chr(byte) # ascii code to asii characters
    except TypeError:
        pass # couldn't finish reading block N. ignore

    try:
        play(tags[recv])
    except KeyError: # dict key doesn't exist
        pass # ignore possible other ntag2xx tags that have data in block address N


if __name__ == "__main__":
    init_player()
    play(tags["HOME"])

    while True: # main loop
        uid = pn532.read_passive_target(timeout_sec=0.5)
        if uid is not None:
            readtag()

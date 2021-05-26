#!/usr/bin/python3
import sys
import threading
import time

import mpv

last_tid = None
new_tid = None
tlist = list()

def init_player():
    global player
    player = mpv.MPV(ytdl=False, input_default_bindings=False,
    fullscreen=True, keep_open=True, osd_level=0, video_osd=False,
    osc=False, input_vo_keyboard=True, cursor_autohide="always",
    demuxer_thread="yes", merge_files=True, image_display_duration="inf")

    @player.on_key_press("q")
    def q_binding():
        player.quit()

    @player.on_key_press('ESC')
    def esc_binding():
        player.quit()

def start_play_thread(filename):
    player.loadfile(filename, mode="replace") 
    return
    try:
        player.wait_for_playback() # yes, it's an ugly hack to return control to the main thread and not stopping playback
    except mpv.ShutdownError:
        pass # handle shutdown event

def play(filename):
    global last_tid
    global new_tid

    new_tid = threading.Thread(target=start_play_thread(filename))
    print("starting new tid")
    new_tid.start()
    tlist.append(new_tid)

    if (last_tid == None):
        pass
    elif (last_tid.is_alive()): # we don't have an old thread yet
        print("joining lasttid")
        last_tid.join() # join old thread

    print("re-assigning lasttid")
    last_tid = new_tid

init_player()

play("res/v2-static.jpg")
time.sleep(3)
play("res/v2.mov")
time.sleep(5)
play("res/v2-inv.mov")
time.sleep(5)

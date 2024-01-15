#!/usr/local/bin/python3

import os
import tkinter as tk
from datetime import datetime, timedelta
import sys
import threading
import pygame

# Suppress the secure coding warning
os.environ['OBJC_DISABLE_INITIALIZE_FORK_SAFETY'] = 'YES'
# Suppress Tkinter deprecation warning
os.environ['TK_SILENCE_DEPRECATION'] = '1'

def play_alert_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("/usr/local/bin/TimerSounds/alarm-clock-1-29480.mp3")  # Provide the path to your sound file
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

class CountdownTimer:
    def __init__(self, master, duration):
        self.master = master
        self.target_time = datetime.now() + timedelta(minutes=duration)
        self.remaining_time = self.target_time - datetime.now()

        self.label = tk.Label(master, font=('Helvetica', 48))
        self.label.pack()

        self.update_timer()

    def update_timer(self):
        if self.remaining_time.total_seconds() <= 0:
            self.label.config(text="Time's up!")
            # Play alert sound when the timer expires
            play_alert_sound()
        else:
            self.label.config(text=str(self.remaining_time).split(".")[0])
            self.remaining_time -= timedelta(seconds=1)
            # Schedule the next update on the main thread
            self.master.after(1000, self.update_timer)

def run_gui(duration):
    root = tk.Tk()
    root.title("Command Line Countdown Timer")
    timer = CountdownTimer(root, duration)
    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python countdown_timer_cmdline.py <duration_in_minutes>")
        sys.exit(1)

    try:
        duration = int(sys.argv[1])
    except ValueError:
        print("Invalid duration. Please enter a valid number.")
        sys.exit(1)

    # Run the Tkinter GUI on the main thread
    run_gui(duration)


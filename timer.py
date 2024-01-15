import tkinter as tk
from datetime import datetime, timedelta
import sys

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
        else:
            self.label.config(text=str(self.remaining_time).split(".")[0])
            self.remaining_time -= timedelta(seconds=1)
            self.master.after(1000, self.update_timer)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python countdown_timer_cmdline.py <duration_in_minutes>")
        sys.exit(1)

    try:
        duration = int(sys.argv[1])
    except ValueError:
        print("Invalid duration. Please enter a valid number.")
        sys.exit(1)

    root = tk.Tk()
    root.title("Command Line Countdown Timer")

    timer = CountdownTimer(root, duration)

    root.mainloop()


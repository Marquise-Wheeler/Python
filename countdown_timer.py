import tkinter as tk
from datetime import datetime, timedelta

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        self.target_time = None
        self.remaining_time = None

        # Entry for user to input countdown time in minutes
        self.entry = tk.Entry(master)
        self.entry.pack()

        # Button to start the countdown
        self.start_button = tk.Button(master, text="Start Countdown", command=self.start_countdown)
        self.start_button.pack()

        # Label to display the countdown
        self.label = tk.Label(master, font=('Helvetica', 48))
        self.label.pack()

    def start_countdown(self):
        try:
            # Get user input for countdown time in minutes
            minutes = int(self.entry.get())
            self.target_time = datetime.now() + timedelta(minutes=minutes)
            self.remaining_time = self.target_time - datetime.now()

            # Disable entry and button after starting the countdown
            self.entry.config(state=tk.DISABLED)
            self.start_button.config(state=tk.DISABLED)

            # Start the countdown
            self.update_timer()

        except ValueError:
            # Handle invalid input
            self.label.config(text="Invalid input. Please enter a valid number.")

    def update_timer(self):
        if self.remaining_time.total_seconds() <= 0:
            self.label.config(text="Time's up!")
        else:
            self.label.config(text=str(self.remaining_time).split(".")[0])
            self.remaining_time -= timedelta(seconds=1)
            self.master.after(1000, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Dynamic Countdown Timer")

    timer = CountdownTimer(root)

    root.mainloop()

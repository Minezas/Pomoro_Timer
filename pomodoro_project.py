import tkinter as tk
from threading import Thread
import time
import winsound
import webbrowser

def play_beep(frequency, duration):
    """Play a beep sound."""
    winsound.Beep(frequency, duration)

def play_music():
    """Play background music."""
    music_url = "https://www.youtube.com/watch?v=Tq7523sJc6I&t=4s&ab_channel=MimiLofiChill"
    webbrowser.open(music_url, new=1)

def stop_music():
    """Stop the music playback."""
    # You may need to implement a way to stop the music playback from the browser
    pass

def play_pomodoro(focus_time, break_time, countdown_label):
    """Run the Pomodoro timer."""
    play_music()

    start_focus = time.time()
    end_focus = start_focus + (focus_time * 60)

    # Countdown for focus time
    while time.time() < end_focus:
        remaining_time = int(end_focus - time.time())
        countdown_label.config(text="Focus time remaining: {:02d}:{:02d}".format(remaining_time // 60, remaining_time % 60))
        time.sleep(1)

    stop_music()  # Stop music playback
    play_beep(200, 1000)  # Beep at the end of focus time
    countdown_label.config(text="Time for a break!")

    start_break = time.time()
    end_break = start_break + (break_time * 60)

    play_beep(1000, 1000)  # Beep at the start of break time

    # Countdown for break time
    while time.time() < end_break:
        remaining_time = int(end_break - time.time())
        countdown_label.config(text="Break time remaining: {:02d}:{:02d}".format(remaining_time // 60, remaining_time % 60))
        time.sleep(1)

    play_beep(200, 1000)  # Beep at the end of break time
    countdown_label.config(text="Break's over!")

def start_pomodoro(focus_entry, break_entry, countdown_label, end_button):
    """Start the Pomodoro timer."""
    focus_time = int(focus_entry.get()) if focus_entry.get() else 25  # Default focus time (25 minutes)
    break_time = int(break_entry.get()) if break_entry.get() else 5   # Default break time (5 minutes)

    # Create a thread to play the Pomodoro
    global pomodoro_thread
    pomodoro_thread = Thread(target=play_pomodoro, args=(focus_time, break_time, countdown_label))
    pomodoro_thread.start()

    end_button.config(state="normal")

def end_session(end_button):
    """End the Pomodoro session."""
    global pomodoro_thread
    if pomodoro_thread and pomodoro_thread.is_alive():
        pomodoro_thread.join()  # Wait for the Pomodoro thread to finish
        end_button.config(state="disabled")

def main():
    """Main function to set up the GUI."""
    root = tk.Tk()
    root.title("Pomodoro Timer")

    # Create a frame with gray background
    frame = tk.Frame(root, bg="#c0c0c0", padx=20, pady=20)
    frame.pack(fill="both", expand=True)

    # Set the retro font
    font_style = ("Courier", 12, "bold")

    # Create label and entry for focus time
    focus_label = tk.Label(frame, text="Focus Time (min):", bg="#c0c0c0", font=font_style)
    focus_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    focus_entry = tk.Entry(frame, font=font_style)
    focus_entry.grid(row=0, column=1, padx=10, pady=5)

    # Create label and entry for break time
    break_label = tk.Label(frame, text="Break Time (min):", bg="#c0c0c0", font=font_style)
    break_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    break_entry = tk.Entry(frame, font=font_style)
    break_entry.grid(row=1, column=1, padx=10, pady=5)

    # Create countdown label
    countdown_label = tk.Label(frame, text="", bg="#c0c0c0", font=font_style)
    countdown_label.grid(row=2, column=0, columnspan=2, pady=10)

    # Create start button
    start_button = tk.Button(frame, text="Start Pomodoro", command=lambda: start_pomodoro(focus_entry, break_entry, countdown_label, end_button),
                              font=font_style)
    start_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Create end session button
    end_button = tk.Button(frame, text="End Session", command=lambda: end_session(end_button), font=font_style, state="disabled")
    end_button.grid(row=4, column=0, columnspan=2, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()



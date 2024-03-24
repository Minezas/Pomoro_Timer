# Pomoro_Timer
This Python script provides a Pomodoro timer GUI built with Tkinter. The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. It uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks.

## Features
- **Customizable Timer**: Set your desired focus time and break time.
- **Auditory Cues**: Beeps signal the start and end of each focus and break period.
- **Optional Music**: Optionally plays music from a YouTube link during the focus period.
- **Threaded**: Timer runs in a separate thread, allowing you to interact with the GUI while the timer is running.

## Requirements
- Python 3.x
- Tkinter library (usually comes pre-installed with Python)
- Winsound library (for audio alerts, available on Windows)

## Usage
1. Ensure you have Python installed on your system.
2. Run the script using `pomodoro_project.py`.
3. Input your desired focus and break times (in minutes) into the respective entry fields.
4. Click "Start Pomodoro" to begin the timer.
5. During the focus period, work on your task until the timer completes.
6. Take a break during the break period, then resume work for the next focus period.
7. Click "End Session" to stop the timer prematurely.

## Notes
- If you wish to change the default music link, you can modify the music_url variable in the script.
- As of now, stopping the music playback is not implemented in the script. You may need to manually stop it from your browser.

## Version
This is version 1.01 of the Pomodoro Timer script.

## Future Updates
Future updates and improvements will be made to enhance functionality and user experience.

## Author
This Pomodoro Timer script is authored by Minezas (Gonçalo Araújo). If you have any questions or suggestions, feel free to reach out via goncaloaraujo1070@gmail.com.


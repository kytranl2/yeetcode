import pyautogui
import keyboard
import threading
import time

# Initial delay in seconds before holding down the 'F' key
initial_delay = 3

# Function to hold down the 'F' key after a delay
def hold_f_after_delay():
    time.sleep(initial_delay)
    print("Holding down 'F' key...")
    pyautogui.keyDown('f')

# Function to continuously check for the quit key
def check_quit():
    while True:
        if keyboard.is_pressed('t'):  # Press 't' to stop the script
            print("Quitting...")
            pyautogui.keyUp('f')
            break

def check_start():
    while True:
        if keyboard.is_pressed('p'):  # Press 't' to stop the script
            print("Holding down 'F' key...")
            pyautogui.keyDown('f')
            break

# Start the thread to hold the 'F' key after a delay
hold_thread = threading.Thread(target=hold_f_after_delay)
hold_thread.start()

# Start the thread to check for the quit key
quit_thread = threading.Thread(target=check_quit)
quit_thread.start()

start_thread = threading.Thread(target=check_start)
start_thread.start()
# Wait for the quit thread to finish

start_thread.join()
quit_thread.join()

print("Script stopped.")

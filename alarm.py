import time
import os
import winsound

def play_alarm():
    frequency = 2500 # Set Frequency To 2500 Hertz
    duration = 1000   # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

def main():
    current_time = time.localtime()
    print(f"Current Time: {current_time.tm_hour}:{current_time.tm_min}")

    if current_time.tm_hour == 9 and current_time.tm_min == 30: # Set Alarm Time (hour and minute)
        print("Alarm time!")
        play_alarm()
    else:
        print("Waiting for alarm time...")

    os.system("pause")

if __name__ == "__main__":
    main()
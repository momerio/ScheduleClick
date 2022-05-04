import pyautogui
import sys
import schedule
import time
print("Auto left click!")

# press mouse positon
mouse_position_x = -2030
mouse_poosition_y = 673
click = "left"  # left or right

# scheduled time
scheduled_time_str = "21:30"


def time_job():
    pyautogui.click(x=mouse_position_x, y=mouse_poosition_y, button=click)


schedule.every().day.at(scheduled_time_str).do(time_job)

while True:
    schedule.run_pending()
    time.sleep(1)

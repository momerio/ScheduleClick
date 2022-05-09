import pyautogui
import sys
import schedule
import time
from argparse import ArgumentParser
print("Auto left click!")


def get_option(default: int) -> ArgumentParser:
    argparser = ArgumentParser(default)
    argparser.add_argument('-x', '--positionx', type=int,
                           default=default,
                           help='x-coordinate position')
    argparser.add_argument('-y', '--positiony', type=int,
                           default=default,
                           help='y-coordinate position')
    argparser.add_argument('-c', '--click', type=str,
                           default="left",
                           help='click(left or right)')
    argparser.add_argument('-t', '--time', type=str,
                           help='click(left or right)')
    return argparser.parse_args()


args = get_option(0)

# press mouse positon
mouse_position_x = args.positionx
mouse_poosition_y = args.positiony
click = args.click  # left or right

# scheduled time
scheduled_time_str = args.time


def time_job():
    pyautogui.click(x=mouse_position_x, y=mouse_poosition_y, button=click)


schedule.every().day.at(scheduled_time_str).do(time_job)

while True:
    schedule.run_pending()
    time.sleep(1)

import time
import random

mouse.release_button(1)
time.sleep(float(random.randrange(100, 200)) / 1000.0)
mouse.press_button(1)
import time
import random

mouse.release_button(1)
time.sleep(float(random.randrange(10, 20)) / 1000.0)
mouse.press_button(1)
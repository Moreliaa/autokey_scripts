import time
import random
import math

number_of_clicks = 10
avg_delay_between_clicks_ms = 250
max_delay_spread_ms = 50

for i in range(number_of_clicks):
    min_delay_ms = math.floor((avg_delay_between_clicks_ms - max_delay_spread_ms) / 2)
    max_delay_ms = math.floor((avg_delay_between_clicks_ms + max_delay_spread_ms) / 2)
    time.sleep(float(random.randrange(min_delay_ms, max_delay_ms)) / 1000.0)
    mouse.press_button(1)
    time.sleep(float(random.randrange(min_delay_ms, max_delay_ms)) / 1000.0)
    mouse.release_button(1)
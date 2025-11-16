import time
import random

number_of_clicks = 10
avg_delay_between_clicks_ms = 250
max_delay_spread_ms = 50

keyboard.press_key(Key.CONTROL)

for i in range(number_of_clicks):
    mouse.click_relative_self(0, 0, 1)
    min_delay_ms = avg_delay_between_clicks_ms - max_delay_spread_ms
    max_delay_ms = avg_delay_between_clicks_ms + max_delay_spread_ms
    time.sleep(float(random.randrange(min_delay_ms, max_delay_ms)) / 1000.0)
    
keyboard.release_key(Key.CONTROL)

import time
import board
import pwmio
from analogio import AnalogIn


led = pwmio.PWMOut(board.D2, frequency=5000, duty_cycle=0)
led2 = pwmio.PWMOut(board.D3, frequency=5000, duty_cycle=0)
pot = AnalogIn(board.A1)

max_val = 65535
while True:
    led.duty_cycle = pot.value
    led2.duty_cycle = max_val - pot.value


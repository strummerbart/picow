from machine import Pin
from machine import Timer

led = Pin("LED", Pin.OUT);
timer = Timer();

def tick(timer):
    global led;
    led.toggle();

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=tick);


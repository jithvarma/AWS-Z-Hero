import time
import os

def cpu_spikage():
    start_time = time.time()
    while True:
        for i in range(10000000):
            # Do some calculations to waste CPU cycles
            result = 0
            for j in range(i):
                result += j * j
            # Print a progress indicator to avoid terminal freezing
            if i % 100000 == 0:
                print(f"Spiking CPU at {i / 1000000:.2f}M", end='\r')
        if time.time() - start_time > 10:  # Run for 10 seconds
            break

cpu_spikage()

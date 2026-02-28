# utils/interpolator.py
import time

class Interpolator:
    def __init__(self, start, end, duration):
        self.start = start
        self.end = end
        self.duration = duration
        self.start_time = time.time()
        self.finished = False

    def update(self, dt):
        now = time.time()
        elapsed = now - self.start_time
        t = min(elapsed / self.duration, 1.0)
        x = self.start[0] + (self.end[0] - self.start[0]) * t
        y = self.start[1] + (self.end[1] - self.start[1]) * t
        self.value = (x, y)
        if t >= 1.0:
            self.finished = True
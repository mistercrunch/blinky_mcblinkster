import time

class Show:
    def __init__(self, renderer, patterns, duration=10):
        self.renderer = renderer
        self.patterns = patterns
        self.duration = duration

    def run(self):
        while True:  # This creates an infinite loop. Adjust as needed for your application.
            for pattern in self.patterns:
                self.renderer.animate(pattern, self.duration)

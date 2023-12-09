class BaseRenderer:
    def animate(self, pattern):
        while True:
            pattern.next_frame()

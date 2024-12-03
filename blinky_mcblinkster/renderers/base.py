import time

class BaseRenderer:
    def animate(self, pattern, duration_sec=None):
        start_time = time.time()  # Record the start time

        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time

            # Check if the duration is exceeded
            if duration_sec is not None and elapsed_time > duration_sec:
                break

            pattern.next_frame()
            self.render_strand(pattern.strand)

            # Optional: You can add a small sleep here to control frame rate
            # time.sleep(0.1)


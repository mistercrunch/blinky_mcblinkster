class BaseRenderer:
    def animate(self, pattern):
        while True:
            pattern.next_frame()
            self.render_strand(pattern.strand)

    def render_strand(self):
        pass


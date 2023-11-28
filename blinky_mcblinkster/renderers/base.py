
class BaseRenderer:

    def animate(self, strand):
        while True:
            strand.compute_frame()
            self.render_frame(strand)

    def render_frame(self, strand):
        return NotImplementedError()

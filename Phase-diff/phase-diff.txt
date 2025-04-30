from gnuradio import gr
import numpy as np

class phase_detector(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name="Phase Detector",
            in_sig=[np.complex64, np.complex64],
            out_sig=[np.float32]
        )

    def work(self, input_items, output_items):
        x1 = input_items[0]
        x2 = input_items[1]

        phase_diff = np.angle(x1 * np.conj(x2))
        output_items[0][:] = phase_diff.astype(np.float32)
        return len(phase_diff)

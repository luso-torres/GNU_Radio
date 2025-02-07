import numpy as np
from gnuradio import gr

class ulaw_decoder(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    def __init__(self, mu=255):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='u-law Decoder',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.mu = mu

    def work(self, input_items, output_items):
        # Ensure input_items is properly indexed
        c0 = np.sign(input_items[0]) * (1/self.mu) * ((1 + self.mu)**np.abs(input_items[0]) - 1)
        output_items[0][:] = c0

        # Return the length of the output items produced
        return len(output_items[0])

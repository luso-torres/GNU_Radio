"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__ will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    def __init__(self, mu=255):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='u-law Compresser',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.ry = 0
        self.mu = mu

    def work(self, input_items, output_items):
        #buf = [0] * len(input_items[0])
        a0 = np.log10(1 + self.mu*np.abs(input_items))*np.sign(input_items)
        b0 = np.log10(1+self.mu)
 
        output_items[0][:] = a0 / b0
        # Return the length of the output items produced
	
        return len(output_items[0])
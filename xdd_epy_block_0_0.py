import numpy as np
from gnuradio import gr

class ulaw_decoder(gr.sync_block):
    def __init__(self, mu=255):
        gr.sync_block.__init__(
            self,
            name='u-law Decoder',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.mu = mu

    def ulaw_decode(self, x):
        # Ensure x is within the valid range and handle NaN and Inf values
        x = np.nan_to_num(x, nan=0.0, posinf=1.0, neginf=-1.0)  # Replace NaN and Inf values
        x = np.clip(x, -1.0, 1.0)  # Ensure values are within the range [-1, 1]

        # Perform u-law decoding
        decoded = np.sign(x) * (1 / self.mu) * ((1 + self.mu) ** np.abs(x) - 1)
        decoded = np.nan_to_num(decoded, nan=0.0, posinf=1.0, neginf=-1.0)  # Replace NaN and Inf values again
        return decoded

    def normalize_audio(self, audio):
        max_val = np.max(np.abs(audio))
        if np.isfinite(max_val) and max_val > 0:
            normalized_audio = audio / max_val
            print("Normalization factor:", max_val)
            return normalized_audio
        print("Invalid normalization factor:", max_val)
        return audio

    def work(self, input_items, output_items):
        # Apply u-law decoding
        decoded_signal = self.ulaw_decode(input_items[0])

        # Debug prints to check signal values before normalization
        print("Decoded Min:", np.min(decoded_signal), "Decoded Max:", np.max(decoded_signal))

        # Normalize the decoded signal
        normalized_signal = self.normalize_audio(decoded_signal)

        # Debug prints to check signal values after normalization
        print("Normalized Min:", np.min(normalized_signal), "Normalized Max:", np.max(normalized_signal))

        # Clip the values to avoid overflow
        output_items[0][:] = np.clip(normalized_signal, -1.0, 1.0)

        # Debug prints to check final signal values
        print("Output Min:", np.min(output_items[0]), "Output Max:", np.max(output_items[0]))

        return len(output_items[0])

import numpy as np
from gnuradio import gr
import scipy.signal as signal

class FrequencyBandFilter(gr.sync_block):
    def __init__(self, filter_length=101, sample_rate=32000, gains=None):
        gr.sync_block.__init__(self,
                               name="FrequencyBandFilter",
                               in_sig=[np.float32],
                               out_sig=[np.float32])

        self.filter_length = filter_length
        self.sample_rate = sample_rate

        # Frequências centrais das bandas
        self.freqs = np.array([32, 64, 128, 256, 512, 1000, 2000, 4000, 8000, 16000])

        # Cálculo das frequências de corte
        self.cutoff_freqs = [(self.freqs[i] / np.sqrt(2), self.freqs[i] * np.sqrt(2)) for i in range(len(self.freqs))]

        # Verifica se a lista de ganhos foi fornecida, caso contrário, define todos como 1 (sem alteração)
        if gains is None:
            gains = np.ones(len(self.freqs))

        # Normaliza os ganhos para que a soma dos valores não ultrapasse 1
        self.gains = np.array(gains)
        self.gains /= np.sum(self.gains)  # Ajusta proporcionalmente para garantir uma soma ≤ 1

        # Criando filtros FIR usando a janela de Hamming
        self.filters = []
        for i, (low, high) in enumerate(self.cutoff_freqs):
            if low < 1:
                low = 1  # Evita frequência 0 Hz
            if high >= self.sample_rate / 2:
                high = self.sample_rate / 2 - 1  # Limite Nyquist

            fir_coeffs = signal.firwin(self.filter_length, [low, high], pass_zero=False, fs=self.sample_rate, window="hamming")
            fir_coeffs /= np.sum(fir_coeffs)  # Normaliza os coeficientes
            self.filters.append(fir_coeffs * self.gains[i])  # Aplica ganho ajustado

    def work(self, input_items, output_items):
        output_signal = np.zeros_like(input_items[0])

        # Aplicando filtros com ganhos ajustados
        for fir_coeffs in self.filters:
            filtered_signal = signal.lfilter(fir_coeffs, 1.0, input_items[0])
            output_signal += filtered_signal  # Somando sinais filtrados

        output_items[0][:] = output_signal
        return len(output_items[0])
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: luso
# GNU Radio version: 3.10.10.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import audio
from gnuradio import blocks
import pmt
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip
import xdd_epy_block_0 as epy_block_0  # embedded python block
import xdd_epy_block_0_0 as epy_block_0_0  # embedded python block



class xdd(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "xdd")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000
        self.freq_9 = freq_9 = 0.1
        self.freq_8 = freq_8 = 0
        self.freq_7 = freq_7 = 0
        self.freq_6 = freq_6 = 0
        self.freq_5 = freq_5 = 0
        self.freq_4 = freq_4 = 0
        self.freq_3 = freq_3 = 0
        self.freq_2 = freq_2 = 0
        self.freq_1 = freq_1 = 0
        self.freq_0 = freq_0 = 0
        self.Volume = Volume = 0.01

        ##################################################
        # Blocks
        ##################################################

        self._freq_9_range = qtgui.Range(0, 1, .01, 0.1, 200)
        self._freq_9_win = qtgui.RangeWidget(self._freq_9_range, self.set_freq_9, "32 Hz", "dial", float, QtCore.Qt.Vertical)
        self.top_grid_layout.addWidget(self._freq_9_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_8_range = qtgui.Range(0, 1, 0.01, 0, 200)
        self._freq_8_win = qtgui.RangeWidget(self._freq_8_range, self.set_freq_8, "16000 Hz", "dial", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._freq_8_win, 1, 3, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_7_range = qtgui.Range(0, 1, .01, 0, 200)
        self._freq_7_win = qtgui.RangeWidget(self._freq_7_range, self.set_freq_7, "8000 Hz", "dial", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._freq_7_win, 1, 2, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_6_range = qtgui.Range(0, 1, .01, 0, 200)
        self._freq_6_win = qtgui.RangeWidget(self._freq_6_range, self.set_freq_6, "4000 Hz", "dial", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._freq_6_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_5_range = qtgui.Range(0, 1, 0.01, 0, 200)
        self._freq_5_win = qtgui.RangeWidget(self._freq_5_range, self.set_freq_5, "2000 Hz", "dial", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._freq_5_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_4_range = qtgui.Range(0, 1, .01, 0, 200)
        self._freq_4_win = qtgui.RangeWidget(self._freq_4_range, self.set_freq_4, "1000 Hz", "dial", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._freq_4_win, 0, 5, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(5, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_3_range = qtgui.Range(0, 1, 0.01, 0, 200)
        self._freq_3_win = qtgui.RangeWidget(self._freq_3_range, self.set_freq_3, "512 Hz", "dial", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._freq_3_win, 0, 4, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_2_range = qtgui.Range(0, 1, 0.010, 0, 200)
        self._freq_2_win = qtgui.RangeWidget(self._freq_2_range, self.set_freq_2, "256 Hz", "dial", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._freq_2_win, 0, 3, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_1_range = qtgui.Range(0, 1, .01, 0, 200)
        self._freq_1_win = qtgui.RangeWidget(self._freq_1_range, self.set_freq_1, "128 Hz", "dial", float, QtCore.Qt.Vertical)
        self.top_grid_layout.addWidget(self._freq_1_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_0_range = qtgui.Range(0, 1, .01, 0, 200)
        self._freq_0_win = qtgui.RangeWidget(self._freq_0_range, self.set_freq_0, "64 Hz", "dial", float, QtCore.Qt.Vertical)
        self.top_grid_layout.addWidget(self._freq_0_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Volume_range = qtgui.Range(0, 0.1, 0.01, 0.01, 200)
        self._Volume_win = qtgui.RangeWidget(self._Volume_range, self.set_Volume, "Volume", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Volume_win)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            2,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.epy_block_0_0 = epy_block_0_0.ulaw_decoder(mu=255)
        self.epy_block_0 = epy_block_0.FrequencyBandFilter(filter_length=1, sample_rate=samp_rate, gains=[freq_0,freq_9, freq_1,freq_2, freq_3, freq_4, freq_5, freq_6, freq_7,freq_8])
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff(Volume)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff((-.1))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, 'E:\\Repositorios\\GNU_Radio\\audio_converter\\output.wav', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.audio_sink_0 = audio.sink(samp_rate, '', True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.epy_block_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_1, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.audio_sink_0, 0))
        self.connect((self.epy_block_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.epy_block_0_0, 0), (self.epy_block_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "xdd")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.epy_block_0.sample_rate = self.samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)

    def get_freq_9(self):
        return self.freq_9

    def set_freq_9(self, freq_9):
        self.freq_9 = freq_9
        self.epy_block_0.gains = [self.freq_0,self.freq_9, self.freq_1,self.freq_2, self.freq_3, self.freq_4, self.freq_5, self.freq_6, self.freq_7,self.freq_8]

    def get_freq_8(self):
        return self.freq_8

    def set_freq_8(self, freq_8):
        self.freq_8 = freq_8
        self.epy_block_0.gains = [self.freq_0,self.freq_9, self.freq_1,self.freq_2, self.freq_3, self.freq_4, self.freq_5, self.freq_6, self.freq_7,self.freq_8]

    def get_freq_7(self):
        return self.freq_7

    def set_freq_7(self, freq_7):
        self.freq_7 = freq_7
        self.epy_block_0.gains = [self.freq_0,self.freq_9, self.freq_1,self.freq_2, self.freq_3, self.freq_4, self.freq_5, self.freq_6, self.freq_7,self.freq_8]

    def get_freq_6(self):
        return self.freq_6

    def set_freq_6(self, freq_6):
        self.freq_6 = freq_6
        self.epy_block_0.gains = [self.freq_0,self.freq_9, self.freq_1,self.freq_2, self.freq_3, self.freq_4, self.freq_5, self.freq_6, self.freq_7,self.freq_8]

    def get_freq_5(self):
        return self.freq_5

    def set_freq_5(self, freq_5):
        self.freq_5 = freq_5
        self.epy_block_0.gains = [self.freq_0,self.freq_9, self.freq_1,self.freq_2, self.freq_3, self.freq_4, self.freq_5, self.freq_6, self.freq_7,self.freq_8]

    def get_freq_4(self):
        return self.freq_4

    def set_freq_4(self, freq_4):
        self.freq_4 = freq_4
        self.epy_block_0.gains = [self.freq_0,self.freq_9, self.freq_1,self.freq_2, self.freq_3, self.freq_4, self.freq_5, self.freq_6, self.freq_7,self.freq_8]

    def get_freq_3(self):
        return self.freq_3

    def set_freq_3(self, freq_3):
        self.freq_3 = freq_3
        self.epy_block_0.gains = [self.freq_0,self.freq_9, self.freq_1,self.freq_2, self.freq_3, self.freq_4, self.freq_5, self.freq_6, self.freq_7,self.freq_8]

    def get_freq_2(self):
        return self.freq_2

    def set_freq_2(self, freq_2):
        self.freq_2 = freq_2
        self.epy_block_0.gains = [self.freq_0,self.freq_9, self.freq_1,self.freq_2, self.freq_3, self.freq_4, self.freq_5, self.freq_6, self.freq_7,self.freq_8]

    def get_freq_1(self):
        return self.freq_1

    def set_freq_1(self, freq_1):
        self.freq_1 = freq_1
        self.epy_block_0.gains = [self.freq_0,self.freq_9, self.freq_1,self.freq_2, self.freq_3, self.freq_4, self.freq_5, self.freq_6, self.freq_7,self.freq_8]

    def get_freq_0(self):
        return self.freq_0

    def set_freq_0(self, freq_0):
        self.freq_0 = freq_0
        self.epy_block_0.gains = [self.freq_0,self.freq_9, self.freq_1,self.freq_2, self.freq_3, self.freq_4, self.freq_5, self.freq_6, self.freq_7,self.freq_8]

    def get_Volume(self):
        return self.Volume

    def set_Volume(self, Volume):
        self.Volume = Volume
        self.blocks_multiply_const_vxx_0_0.set_k(self.Volume)




def main(top_block_cls=xdd, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()

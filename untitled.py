#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: ex1
# Author: luso
# GNU Radio version: 3.10.10.0

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
import sip



class untitled(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "ex1", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("ex1")
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

        self.settings = Qt.QSettings("GNU Radio", "untitled")

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
        self.frequency = frequency = 1000
        self.amplitude = amplitude = 0

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_sink_x_0 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        self._frequency_tool_bar = Qt.QToolBar(self)
        self._frequency_tool_bar.addWidget(Qt.QLabel("'frequency'" + ": "))
        self._frequency_line_edit = Qt.QLineEdit(str(self.frequency))
        self._frequency_tool_bar.addWidget(self._frequency_line_edit)
        self._frequency_line_edit.editingFinished.connect(
            lambda: self.set_frequency(eng_notation.str_to_num(str(self._frequency_line_edit.text()))))
        self.top_layout.addWidget(self._frequency_tool_bar)
        self.audio_source_0 = audio.source(samp_rate, '', True)
        self._amplitude_tool_bar = Qt.QToolBar(self)
        self._amplitude_tool_bar.addWidget(Qt.QLabel("'amplitude'" + ": "))
        self._amplitude_line_edit = Qt.QLineEdit(str(self.amplitude))
        self._amplitude_tool_bar.addWidget(self._amplitude_line_edit)
        self._amplitude_line_edit.editingFinished.connect(
            lambda: self.set_amplitude(eng_notation.str_to_num(str(self._amplitude_line_edit.text()))))
        self.top_layout.addWidget(self._amplitude_tool_bar)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.audio_source_0, 0), (self.qtgui_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "untitled")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        Qt.QMetaObject.invokeMethod(self._frequency_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.frequency)))

    def get_amplitude(self):
        return self.amplitude

    def set_amplitude(self, amplitude):
        self.amplitude = amplitude
        Qt.QMetaObject.invokeMethod(self._amplitude_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.amplitude)))




def main(top_block_cls=untitled, options=None):

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

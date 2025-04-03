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
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import numpy as np
import quad_demodgrc_epy_block_0 as epy_block_0  # embedded python block
import sip



class quad_demodgrc(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "quad_demodgrc")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.threshold = threshold = 0
        self.samp_rate = samp_rate = 3200000
        self.mode = mode = 1
        self.freq = freq = 10000
        self.f_c = f_c = 500000
        self.duration = duration = 1
        self.coeff = coeff = 0.15
        self.amplitude = amplitude = 0.09
        self.Ganho_discriminador = Ganho_discriminador = 10

        ##################################################
        # Blocks
        ##################################################

        self._threshold_range = qtgui.Range(0, 5, 1, 0, 6)
        self._threshold_win = qtgui.RangeWidget(self._threshold_range, self.set_threshold, "Threshold", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._threshold_win, 0, 5, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(5, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'VCO')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'Envelope')
        self.top_layout.addWidget(self.tab)
        # Create the options list
        self._mode_options = [0, 1]
        # Create the labels list
        self._mode_labels = ['Halfwave', 'Fullwave ']
        # Create the combo box
        # Create the radio buttons
        self._mode_group_box = Qt.QGroupBox("Rectifier" + ": ")
        self._mode_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._mode_button_group = variable_chooser_button_group()
        self._mode_group_box.setLayout(self._mode_box)
        for i, _label in enumerate(self._mode_labels):
            radio_button = Qt.QRadioButton(_label)
            self._mode_box.addWidget(radio_button)
            self._mode_button_group.addButton(radio_button, i)
        self._mode_callback = lambda i: Qt.QMetaObject.invokeMethod(self._mode_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._mode_options.index(i)))
        self._mode_callback(self.mode)
        self._mode_button_group.buttonClicked[int].connect(
            lambda i: self.set_mode(self._mode_options[i]))
        self.top_grid_layout.addWidget(self._mode_group_box, 0, 4, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_range = qtgui.Range(1000, 100000, 10000, 10000, 10)
        self._freq_win = qtgui.RangeWidget(self._freq_range, self.set_freq, "Frequency", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._freq_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._coeff_range = qtgui.Range(0.1, 1, .05, 0.15, 20)
        self._coeff_win = qtgui.RangeWidget(self._coeff_range, self.set_coeff, "RC Coefficient", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._coeff_win, 0, 3, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._amplitude_range = qtgui.Range(0, 0.1, .01, 0.09, 10)
        self._amplitude_win = qtgui.RangeWidget(self._amplitude_range, self.set_amplitude, "Amplitude", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._amplitude_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Ganho_discriminador_range = qtgui.Range(0, 100, 1, 10, 50)
        self._Ganho_discriminador_win = qtgui.RangeWidget(self._Ganho_discriminador_range, self.set_Ganho_discriminador, "Discriminator Gain", "dial", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._Ganho_discriminador_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
            (round(5*samp_rate/freq)), #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
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
        self.qtgui_time_sink_x_1.enable_control_panel(True)
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


        for i in range(1):
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
        self.tab_layout_0.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            (round(4*samp_rate/freq)), #size
            samp_rate, #samp_rate
            "", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Saída', 'Entrada', 'Signal 3', 'Signal 4', 'Signal 5',
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
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.tab_layout_1.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(True)
        self.qtgui_freq_sink_x_1.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.qwidget(), Qt.QWidget)
        self.tab_layout_0.addWidget(self._qtgui_freq_sink_x_1_win)
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
        self.qtgui_freq_sink_x_0.enable_control_panel(True)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not False)

        labels = ['Saída', 'Entrada', '', '', '',
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
        self.tab_layout_1.addWidget(self._qtgui_freq_sink_x_0_win)
        self.epy_block_0 = epy_block_0.blk(threshold=threshold, mode=mode, coeff=coeff)
        self.blocks_vco_f_0 = blocks.vco_f(samp_rate, (2*np.pi*f_c), 1)
        self.blocks_transcendental_0 = blocks.transcendental('atan', "float")
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(Ganho_discriminador)
        self.blocks_divide_xx_0 = blocks.divide_ff(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 4)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(1)
        self.band_pass_filter_0_1 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                (freq-(freq/1000*amplitude)),
                (freq+(freq/1000*amplitude)),
                (freq/20),
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                (f_c-freq),
                (f_c+freq),
                (freq/20),
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                (freq-(freq/1000*amplitude)),
                (freq+(freq/1000*amplitude)),
                (freq/20),
                window.WIN_HAMMING,
                6.76))
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, freq, amplitude, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.band_pass_filter_0, 0), (self.band_pass_filter_0_1, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.band_pass_filter_0_1, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.band_pass_filter_0_1, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_vco_f_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_divide_xx_0, 1))
        self.connect((self.blocks_divide_xx_0, 0), (self.blocks_transcendental_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.epy_block_0, 0))
        self.connect((self.blocks_transcendental_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_vco_f_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.blocks_vco_f_0, 0), (self.blocks_divide_xx_0, 0))
        self.connect((self.blocks_vco_f_0, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.blocks_vco_f_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.epy_block_0, 0), (self.band_pass_filter_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "quad_demodgrc")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_threshold(self):
        return self.threshold

    def set_threshold(self, threshold):
        self.threshold = threshold
        self.epy_block_0.threshold = self.threshold

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.freq-(self.freq/1000*self.amplitude)), (self.freq+(self.freq/1000*self.amplitude)), (self.freq/20), window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.f_c-self.freq), (self.f_c+self.freq), (self.freq/20), window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(1, self.samp_rate, (self.freq-(self.freq/1000*self.amplitude)), (self.freq+(self.freq/1000*self.amplitude)), (self.freq/20), window.WIN_HAMMING, 6.76))
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)

    def get_mode(self):
        return self.mode

    def set_mode(self, mode):
        self.mode = mode
        self._mode_callback(self.mode)
        self.epy_block_0.mode = self.mode

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.analog_sig_source_x_0_0.set_frequency(self.freq)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.freq-(self.freq/1000*self.amplitude)), (self.freq+(self.freq/1000*self.amplitude)), (self.freq/20), window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.f_c-self.freq), (self.f_c+self.freq), (self.freq/20), window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(1, self.samp_rate, (self.freq-(self.freq/1000*self.amplitude)), (self.freq+(self.freq/1000*self.amplitude)), (self.freq/20), window.WIN_HAMMING, 6.76))

    def get_f_c(self):
        return self.f_c

    def set_f_c(self, f_c):
        self.f_c = f_c
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.f_c-self.freq), (self.f_c+self.freq), (self.freq/20), window.WIN_HAMMING, 6.76))

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration

    def get_coeff(self):
        return self.coeff

    def set_coeff(self, coeff):
        self.coeff = coeff
        self.epy_block_0.coeff = self.coeff

    def get_amplitude(self):
        return self.amplitude

    def set_amplitude(self, amplitude):
        self.amplitude = amplitude
        self.analog_sig_source_x_0_0.set_amplitude(self.amplitude)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.freq-(self.freq/1000*self.amplitude)), (self.freq+(self.freq/1000*self.amplitude)), (self.freq/20), window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(1, self.samp_rate, (self.freq-(self.freq/1000*self.amplitude)), (self.freq+(self.freq/1000*self.amplitude)), (self.freq/20), window.WIN_HAMMING, 6.76))

    def get_Ganho_discriminador(self):
        return self.Ganho_discriminador

    def set_Ganho_discriminador(self, Ganho_discriminador):
        self.Ganho_discriminador = Ganho_discriminador
        self.blocks_multiply_const_vxx_0.set_k(self.Ganho_discriminador)




def main(top_block_cls=quad_demodgrc, options=None):

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

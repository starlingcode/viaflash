#!/bin/bash

pyside6-uic mainwindow.ui > ui_mainwindow.py
pyside6-uic gateseq_pattern_editor.ui > ui_gateseq_pattern_editor.py
pyside6-uic osc3_quantization_editor.ui > ui_osc3_quantization_editor.py
pyside6-uic sync3_scale_editor.ui > ui_sync3_scale_editor.py
pyside6-uic sync3_ratio.ui > ui_sync3_ratio.py
pyside6-uic sync3_ratio_add.ui > ui_sync3_ratio_add.py
pyside6-uic ratio_display.ui > ui_ratio_display.py
pyside6-uic wavetable_set_editor.ui > ui_wavetable_set_editor.py
pyside6-uic wavetable_browser.ui > ui_wavetable_browser.py

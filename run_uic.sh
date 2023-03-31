#!/bin/bash

pyside6-uic ui_resources/mainwindow.ui > ui_resources/ui_mainwindow.py
pyside6-uic ui_resources/gateseq_pattern_editor.ui > ui_resources/ui_gateseq_pattern_editor.py
pyside6-uic ui_resources/osc3_quantization_editor.ui > ui_resources/ui_osc3_quantization_editor.py
pyside6-uic ui_resources/sync3_scale_editor.ui > ui_resources/ui_sync3_scale_editor.py
pyside6-uic ui_resources/sync3_ratio_add.ui > ui_resources/ui_sync3_ratio_add.py
pyside6-uic ui_resources/ratio_display.ui > ui_resources/ui_ratio_display.py
pyside6-uic ui_resources/wavetable_set_editor.ui > ui_resources/ui_wavetable_set_editor.py
pyside6-uic ui_resources/wavetable_browser.ui > ui_resources/ui_wavetable_browser.py

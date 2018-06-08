#-------------------------------------------------
#
# Project created by QtCreator 2018-06-03T10:06:51
#
#-------------------------------------------------

QT       += core gui network

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = QtDownloadExample
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    filedownloader.cpp

HEADERS  += mainwindow.h \
    filedownloader.h

FORMS    += mainwindow.ui

RESOURCES += \
    resources.qrc

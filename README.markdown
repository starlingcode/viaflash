viaflash - dfu-util GUI Frontend for flashing VIA firmwares
=======================================

Qt utility for detecting and flashing VIA capable microcontrollers
adapted from [kii-dfu](http://github.com/kiibohd/kii-dfu)

Requires that the dfu-util binary/symlink be in the same directory as `./viaflash`

dfu-util can be found here: [dfu-util](http://dfu-util.gnumonks.org/)
Please use 0.8 or higher if possible.


Building
--------

### Linux

Requires: qt5, cmake 2.8.9+

```bash
mkdir build
cd build
make
```


### Mac

Requires: qt5, cmake 2.8.9+
(Works with Macports)

```bash
mkdir build
cd build
make
```


### Windows

Requires: [Qt5](http://qt-project.org/qt5 with mingw32), [cmake 3.0+](http://www.cmake.org/download/)

The easiest way is to use QtCreator.
Open up the CMakeLists.txt file with QtCreator (make sure to select a build directory different from the source directory)
Run build



Installation
------------

Linux/Mac just copy/symlink `dfu-util` to the same directory


### Windows

**Driver Installation, only do once**

Download and run [Zadig](http://zadig.akeo.ie/)
Unplug module power, hold down DFU button while plugging in USB.  The LED on the front should glow a dim aqua.

Install STM32 DFU Driver or use Zadig (Untested!) 

**Driver installation finished**


Then copy `dfu-util.exe` to the same directory as `viaflash.exe`



Usage
-----

Run `./viaflash` or `viaflash.exe`

For a custom upload, Browse to the *.dfu.bin* file to flash and select "custom firmware".

For a stock firmware, select the firmware you wish to flash.

With VIA removed from power, hold DFU button down and plug in USB cable.  RGB LED should glow a dim aqua.  Click "detect module" and it should display detected serial number, if not, check to ensure that module is plugged in and in DFU mode, and drivers are installed if necessary.

Click Flash


You may need to run the utility as root.


Linux
-----

For Linux it is also possible to a udev rules file to `/etc/udev/rules.d`
[98-kiibohd.rules](https://github.com/kiibohd/controller/blob/master/98-kiibohd.rules)

Then run:
```bash
udevadm control --reload-rules
```

And reconnect the USB device.
You should no longer require root to flash the keyboard


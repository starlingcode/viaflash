### Viaflash/Viatools

Helper applications for updating firmware and static resources on the Via modules.

## Building

You will need to make sure Python >= 3.8 is installed on your machine and you will need to have access to the binary of [dfu-util](http://dfu-util.sourceforge.net/) >= 0.9.

On Windows, you will need to [register your DFU device with the correct driver using Zadig](https://starling.space/via/platform-info#viaflash).

After cloning the source code and navigating to the top level directory of the project, it is recommended to create [a Python virtual environment](https://docs.python.org/3/library/venv.html).

From the top level of the source directory, with your vitual environment activated, download python dependencies with:
```pip -r requirements.txt```

Next, create a directory called vendor and copy or symlink the dfu-util binary into that folder (editorial, this feels sketchy but I suppose it will be handled when packaging the app)

You should now be able to run the application with:
```python main.py```

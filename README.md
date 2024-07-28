# Pico Ringer

This is a simple MicroPython project to forward a Ring chime from my [HomeNode](https://prasha.au/project/homenode) automation system to speakers.

A Pi Pico W listens for MQTT messages and uses a PCM5102A DAC to play the sound via a 3.5mm output.



## Setup development environment

### Python venv
1. Install `python3`
2. Create a virtualenv using `python -m venv .venv`
3. Activate the virtualenv using `source .venv/bin/activate` or `.venv/Scripts/activate.ps1`
4. Install the requirements using `pip install -r requirements.txt`


### Flash Micropython
You can grab the MicroPython firmware for a Pi Pico W from [this page](https://micropython.org/download/RPI_PICO_W/).
Drag/drop as per usual.


### Config file
Create a config file for credentials in `src/config.json`...
```json
{ "wifi_ssid": "", "wifi_psk": "", "mqtt_server": "192.168.1.4"}
```

### Setup Files
- Install libs using `mip.install('')`
- Copy over the audio file
- Copy config.json and helper files



## Developing
The easiest way to develop is to use `mpremote` to mount the src folder.


To begin clear out the `main.py` file and reboot. This allows you to use other commands without interference.
```python
import os
os.remove('main.py')
```


You can then mount the src folder...
```bash
mpremote mount src
```


From REPL you can start executing code. To "hot reload" a file you can run the following command.
This will let you import updated code.
```python
from utils import clear_mod
clear_mod(ringer)
```



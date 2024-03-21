
## Development

### Python venv
1. Install `python3`
2. Create a virtualenv using `python -m venv .venv`
3. Activate the virtualenv using `source .venv/bin/activate` or `.venv/Scripts/activate.ps1`
4. Install the requirements using `pip install -r requirements.txt`


### Flash Micropython
You can grab the MicroPython firmware from [this page](https://micropython.org/download/ESP8266_GENERIC/).
After that you can just load it using...
```
esptool.py --port COM6 --baud 115200 write_flash --flash_size=detect 0 [filepath]
```

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
The easiest way to develop is to use `mpremote` to mount the src folder. From there you can play around in REPL or import a whole script in.
```
mpremote connect COM6
mpremote soft-reset mount src
```

## Formatting
```
autopep8 src
```


### Python venv
1. Install `python3`
2. Create a virtualenv using `python -m venv .venv`
3. Activate the virtualenv using `source .venv/bin/activate` or `.venv/Scripts/activate.ps1`
4. Install the requirements using `pip install -r requirements.txt`

## Setup
- Install libs using `mip.install('')`
- Copy over the audio file
- Copy config.json and helper files


## Debugging
### OSX
```
screen  /dev/cu.usbserial-10 115200
```

## Formatting
```
autopep8 src
```

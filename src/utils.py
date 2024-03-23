import json
import network
import sys
import gc


def get_config():
  return json.load(open('config.json'))


def connect_to_wifi():
  config = get_config()
  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect(config['wifi_ssid'], config['wifi_psk'])
    while not wlan.isconnected():
      pass
  print('network config:', wlan.ifconfig())


def turn_off_ap():
  ap_if = network.WLAN(network.AP_IF)
  ap_if.active(False)


def clear_mod(mod):
  del sys.modules[mod.__name__]
  gc.collect()

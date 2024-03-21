
from utils import get_config, connect_to_wifi, turn_off_ap
from lib.umqtt.robust import MQTTClient
from ringer import ring
import json

turn_off_ap()

config = get_config()

connect_to_wifi()

mqtt = MQTTClient("picoring", config['mqtt_server'])


def update_state():
  global mqtt
  mqtt.publish(b'device/update/ringer', json.dumps({
      'name': 'Ringer',
      'controls': {
          'ring': {'type': 'simple', 'label': 'Ring'},
      },
      'sensors': {}
  }))


def sub_cb(topic, msg):
  if topic == b'device/requestRegister':
    update_state()
    return
  elif topic == b'device/runAction/ringer':
    data = json.loads(msg)
    control = data['data']['control']
    if control == 'ring':
      ring()


mqtt.set_callback(sub_cb)
mqtt.connect()
mqtt.subscribe(b'device/runAction/ringer')
mqtt.subscribe(b'device/requestRegister')

update_state()

while True:
  mqtt.wait_msg()

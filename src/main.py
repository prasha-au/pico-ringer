
from utils import get_config, connect_to_wifi, turn_off_ap
from lib.umqtt.robust2 import MQTTClient
from ringer import ring
import json
import utime

turn_off_ap()

config = get_config()

connect_to_wifi()

mqtt = MQTTClient('ringer', config['mqtt_server'], keepalive=10)

mqtt.set_last_will('device/lwt', 'ringer')

def update_state():
  global mqtt
  mqtt.publish(b'device/update/ringer', json.dumps({
      'name': 'Ringer',
      'controls': {
          'ring': {'type': 'simple', 'label': 'Ring'},
      },
      'sensors': {}
  }))


def sub_cb(topic, msg, _retained, _duplicate):
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

loopcount = 0
while True:
  loopcount = (loopcount + 1) % 100
  utime.sleep_ms(500)
  if mqtt.is_conn_issue():
    while mqtt.is_conn_issue():
      mqtt.reconnect()
      update_state()
    else:
      mqtt.resubscribe()

  if loopcount % 5 == 0:
    mqtt.ping()

  for _ in range(100):
    mqtt.check_msg()
    if not mqtt.things_to_do():
      break
    utime.sleep_ms(1)

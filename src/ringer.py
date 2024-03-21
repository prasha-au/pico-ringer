import os
from machine import Pin, I2S


SCK_PIN = 16
WS_PIN = 17
SD_PIN = 18
I2S_ID = 0
BUFFER_LENGTH_IN_BYTES = 2048

WAV_FILE = "ring_chime_16_16.wav"
WAV_SAMPLE_SIZE_IN_BITS = 16
FORMAT = I2S.MONO
SAMPLE_RATE_IN_HZ = 16000

audio_out = I2S(
  I2S_ID,
  sck=Pin(SCK_PIN),
  ws=Pin(WS_PIN),
  sd=Pin(SD_PIN),
  mode=I2S.TX,
  bits=WAV_SAMPLE_SIZE_IN_BITS,
  format=FORMAT,
  rate=SAMPLE_RATE_IN_HZ,
  ibuf=BUFFER_LENGTH_IN_BYTES,
)

wav = open(WAV_FILE, "rb")

wav_samples = bytearray(BUFFER_LENGTH_IN_BYTES / 2)
wav_samples_mv = memoryview(wav_samples)


def ring():
  wav.seek(256)
  while True:
    num_read = wav.readinto(wav_samples_mv)
    if num_read == 0:
      break
    else:
      audio_out.write(wav_samples_mv[:num_read])

import numpy as np
import pyaudio
import sounddevice as sd
import json

def get_input_device(string):
  p = pyaudio.PyAudio()
  info = p.get_host_api_info_by_index(0)
  numdevices = info.get('deviceCount')
  for i in range(0, numdevices):
    name = p.get_device_info_by_host_api_device_index(0, i).get('name')
    if string in name:
      print("Input Device id ", i, " - ", name, p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels'))
      return i

  print("No input device found with string:", string)


def get_output_device(string):
  devices = sd.query_devices()

  for i, device in enumerate(devices):
      if string in device['name']:
          print("Output Device id ", i, " - ", device['name'])
          return i

  print("No output device found with string:", string)

# Read the JSON file
with open('params.json', 'r') as file:
    data = json.load(file)

# Define the parameters
SWEEP_DURATION = data['SWEEP_DURATION']
TIMING_REFERENCE_DURATION = data['TIMING_REFERENCE_DURATION']
HEADROOM_DB = data['HEADROOM_DB']
MIN_TONE = data['MIN_TONE']
MAX_TONE = data['MAX_TONE']
RECORDING_SAMPLE_RATE = data['RECORDING_SAMPLE_RATE']

TOTAL_PLAY_TIME = 0

ORDERED_FREQUENCY_LIST = []

TOTAL_PLAY_TIME = SWEEP_DURATION + TIMING_REFERENCE_DURATION

print("Expected total play time:", TOTAL_PLAY_TIME)
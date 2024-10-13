import numpy as np
import sounddevice as sd
import soundfile as sf
from list_audio_devices import get_output_device, TIME_PER_TONE, PAUSE_TIME, PLAY_IDENTITY, ORDERED_FREQUENCY_LIST, HEADROOM_GAIN, HEADROOM_DB  
import matplotlib.pyplot as plt
import time
from tqdm import tqdm

import time

# Audio output device
output_device_index = get_output_device("USB SPDIF Adapter")

filepath = 'stimulus.wav'
data, samplerate = sf.read(filepath)
length_in_seconds = len(data) / samplerate
print('Expected total play time:', length_in_seconds)

sd.play(data, samplerate, device=output_device_index)

with tqdm(total=length_in_seconds, unit='s') as pbar:
    for _ in range(int(length_in_seconds)):
        time.sleep(1)  # wait for 1 second
        pbar.update(1)  # update progress bar

sd.wait()

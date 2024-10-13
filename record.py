import pyaudio
import soundfile as sf
import numpy as np
from list_audio_devices import get_input_device, TOTAL_PLAY_TIME, RECORDING_SAMPLE_RATE

CHUNK = 4096
FORMAT = pyaudio.paFloat32  # Changed to float32 for soundfile compatibility
CHANNELS = 2
EXTRA_RECORDING_SECONDS_AFTER_TONES_COMPLETED = 5
RECORD_SECONDS = TOTAL_PLAY_TIME + EXTRA_RECORDING_SECONDS_AFTER_TONES_COMPLETED
FLAC_OUTPUT_FILENAME = "measurement.wav"

p = pyaudio.PyAudio()

try:
    # Audio input device
    input_device_index = get_input_device("Record") # For E1DA Cosmos ADC

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RECORDING_SAMPLE_RATE,
                    input=True,
                    input_device_index=input_device_index,
                    frames_per_buffer=CHUNK)

    print("* recording")

    # Pre-allocate numpy array
    total_frames = int(RECORDING_SAMPLE_RATE / CHUNK * RECORD_SECONDS)
    audio_data = np.zeros((total_frames * CHUNK, CHANNELS), dtype=np.float32)

    for i in range(total_frames):
        data = stream.read(CHUNK)
        frame_data = np.frombuffer(data, dtype=np.float32).reshape(-1, CHANNELS)
        audio_data[i*CHUNK:(i+1)*CHUNK] = frame_data

    print("* done recording")

    # Write to FLAC file
    sf.write(FLAC_OUTPUT_FILENAME, audio_data, RECORDING_SAMPLE_RATE, format='PCM_24')

finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
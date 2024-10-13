import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Function to generate a logarithmic sweep
def generate_log_sweep(f1, f2, t, Fs):

    # Fade in time (s)
    fade_in = 0.1
    fade_out = 0.1

    times = np.arange(0, t, 1/Fs)
    x = signal.chirp(times, f1, t, f2, method='logarithmic')
    for i in range(int(fade_in*Fs)):
        x[i] = x[i] * i/(fade_in*Fs)
    for i in range(int(fade_out*Fs)):
        x[-i] = x[-i] * i/(fade_out*Fs)
    plt.plot(times, x)
    plt.show()
    return x
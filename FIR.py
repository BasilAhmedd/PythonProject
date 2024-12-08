# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.signal import firwin, freqz
#
# # Filter specifications
# num_taps = 10001  # Filter order (number of taps)
# cutoff_frequency = 1500  # Cutoff frequency as a fraction of Nyquist rate (1.0 is the Nyquist frequency)
# sampling_rate = 20000  # In the same units as the input signal
#
# # Design the filter
# fir_coeff = firwin(num_taps,cutoff_frequency/(0.5 * sampling_rate),window='hann')
# # Frequency response
# w, h = freqz(fir_coeff, worN=8000)
# plt.plot(0.5 * sampling_rate * w / np.pi, np.abs(h), 'b')
# plt.title('Low-pass FIR Filter Frequency Response')
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Gain')
# plt.grid()
# plt.show()

# The fir_coeff variable now holds the filter coefficients

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

num_taps = 100001
cutoff = 5000
fs = 48000

fir_coeff = firwin(num_taps,cutoff/(0.5 * fs),window='hann')
w, h = freqz(fir_coeff, worN=8000)
plt.plot(0.5 * fs * w / np.pi, np.abs(h), 'b')
plt.title('Low-pass FIR Filter Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.grid()
plt.show()
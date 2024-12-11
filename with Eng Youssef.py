import  numpy as np
import scipy.io.wavfile as wavfile
from scipy.signal import wiener

fs,noisy_signal=wavfile.read('noisy_audio_Final.wav')

noisy_signal = noisy_signal/np.max(np.abs(noisy_signal))

filtered_sound = wiener(noisy_signal,noise=1e0)

filtered_sound = (filtered_sound * 32767).astype(np.int16)

wavfile.write('filtered_signal0.wav',fs,filtered_sound)
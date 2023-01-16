from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

PATH = "F:/parsa/daneshgah/signal/Project"

sr, sig_audio = wavfile.read(PATH + "/Voices/1.wav")
time = sig_audio.shape[0]/sr
sample = sig_audio.shape[0]
t = np.arange(0, time, 1/sr)

sig_fr = np.fft.fft(sig_audio)

sig_out = np.fft.ifft(sig_fr)

sig_out = sig_out.astype(sig_audio.dtype)

wavfile.write(PATH + "/Voices/output.wav", sr, sig_out.astype(sig_audio.dtype))
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

PATH = "F:/parsa/daneshgah/signal/Project"


j = complex(0, 1)
sr, sig_audio = wavfile.read(PATH + "/Voices/1.wav")

#t for plotting in time
time = sig_audio.shape[0]/sr
t = np.arange(0, time, 1/sr)

#sig_freq for plotting in frequency
sig_fr = np.fft.rfft(sig_audio)
sig_freq = np.fft.rfftfreq(sig_audio.shape[0], 1/sr)


phase = np.angle(sig_fr)
sig_abs = np.abs(sig_fr)


#a
sig_fr_a = sig_abs * np.exp(j * -1 * phase)
sig_out_a = np.fft.irfft(sig_fr_a)

#b
sig_fr_b = sig_abs * np.exp(j * 0)
sig_out_b = np.fft.irfft(sig_fr_b)


#c
N = sig_audio.shape[0]
sig_fr_c1 = sig_abs * np.exp(j * phase) * np.exp(j * N/4)
sig_fr_c2 = sig_abs * np.exp(j * phase) * np.exp(j * N/2)
sig_fr_c3 = sig_abs * np.exp(j * phase - N/4) * np.exp(-1 * j * N/4)
sig_out_c1 = np.fft.irfft(sig_fr_c1)
sig_out_c2 = np.fft.irfft(sig_fr_c2)
sig_out_c3 = np.fft.irfft(sig_fr_c3)
figure, axis = plt.subplots(2,2)
#axis[0][0].plot(sig_freq, sig_fr_c1)
#axis[0][1].plot(sig_freq, sig_fr_c2)
#axis[1][0].plot(sig_freq, sig_fr_c3)
#plt.show()

#d
sig_fr_d = 2 * sig_abs * np.exp(j * phase)
sig_out_d = np.fft.irfft(sig_fr_d)

#e
mean_abs = sig_abs.mean()
sig_fr_e = mean_abs * np.exp(j * phase)
sig_out_e = np.fft.irfft(sig_fr_e)

#f 
sr2, sig_audio2 = wavfile.read(PATH + "/Voices/2.wav")
sig_audio2 = sig_audio2[0 : len(sig_audio)]
sig_fr2 = np.fft.rfft(sig_audio2)
phase2 = np.angle(sig_fr2)
sig_abs2 = np.abs(sig_fr2)
sig_fr_f1 = sig_abs2 * np.exp(j * phase2)
sig_out_f1 = np.fft.irfft(sig_fr_f1)
sig_fr_f2 = sig_abs * np.exp(j * phase)
sig_out_f2 = np.fft.irfft(sig_fr_f2)


#OUTPUT
wavfile.write(PATH + "/Voices/output_a.wav", sr, sig_out_a.astype(sig_audio.dtype))
wavfile.write(PATH + "/Voices/output_b.wav", sr, sig_out_b.astype(sig_audio.dtype))
wavfile.write(PATH + "/Voices/output_c1.wav", sr, sig_out_c1.astype(sig_audio.dtype))
wavfile.write(PATH + "/Voices/output_c2.wav", sr, sig_out_c2.astype(sig_audio.dtype))
wavfile.write(PATH + "/Voices/output_c3.wav", sr, sig_out_c3.astype(sig_audio.dtype))
wavfile.write(PATH + "/Voices/output_d.wav", sr, sig_out_d.astype(sig_audio.dtype))
wavfile.write(PATH + "/Voices/output_e.wav", sr, sig_out_e.astype(sig_audio.dtype))
wavfile.write(PATH + "/Voices/output_f1.wav", sr, sig_out_f1.astype(sig_audio.dtype))
wavfile.write(PATH + "/Voices/output_f2.wav", sr, sig_out_f2.astype(sig_audio.dtype))

#plt.plot(sig_freq, np.abs(sig_fr))
#plt.show()
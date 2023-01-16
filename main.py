from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

PATH = "F:/parsa/daneshgah/signal/Project"

sr, sig_audio = wavfile.read(PATH + "/Voices/1.wav")

sig_out = sig_audio

wavfile.write(PATH + "/Voices/output.wav", sr, sig_out.astype(sig_audio.dtype))
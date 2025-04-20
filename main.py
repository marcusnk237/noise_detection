# Script to detect Noise in signal
"""
@author: Marc Junior Nkengue
"""
import numpy as np
def noise_detection (signal, signal_duration, frequency):
    idx_begin = int (signal_duration[0] * frequency) # Index of the first signal pont
    noise_signal = signal.std(axis=0).max() # Signal Noise
    mean_signal = signal.mean(axis=0)  # Signal Mean
    center_signal = signal - mean_signal # Centered signal
    idx_noise = np.where(center_signal[idx_begin:] > noise_signal)[0] + idx_begin # Seek signal points where noise is above the signal noise level
    noise_duration = [idx_noise[0] / frequency , idx_noise[-1]/frequency] # In seconds
    noise = signal[idx_noise[0] : idx_noise[-1]]
    return noise , noise_duration



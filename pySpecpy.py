# Spectrogram and Audio Analysis Toolit
# Brother Comrade's Unified WAV Analyzer Suite

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import spectrogram

os.makedirs("/home/wav_A_results", exist_ok = True)

def analyze_wav(filepath):
    try:
        rate, data = wavfile.read(filepath)
        name = os.path.splitext(os.path.basename(filepath))[0]

        if len(data.shape) > 1:
            data = data[:, 0]

        stats = {
            "Samples": len(data),
            "Duration_sec": len(data),
            "Mean": np.mean(data),
            "Std": np.std(data),
            "Max": np.max(data),
            "Min": np.min(data),
            "RMS": np.sqrt(np.mean(np.square(data))),
        }
        print("*" * 48)
        print(name, stats)
        with open(f"/home/wav_A_results/{name}_summary.txt", "w") as f:
            f.write(f"Rate: {rate}\n")
            for k, v in stats.items():
                f.write(f"{k}: {v}\n")

        f, t, Sxx = spectrogram(data, fs = rate)
        plt.figure(figsize = (10, 4))
        plt.pcolormesh(t, f, 10 + np.log10(Sxx + 1e-10), shading = "gouraud")
        plt.ylabel("Frequency [Hz]")
        plt.xlabel("Time [s]")
        plt.title(f"Spectrogram: {name}")
        plt.colorbar(label = "dB")
        plt.tight_layout()
        plt.savefig(f"/home/wav_A_results/{name}_spectrogram.png")
        plt.close()

        print(f"Analyzed: {name}")
    except Exception as e:
        print(f"Error with {filepath}: {e}")


def batch_analyze(base_folder):
    for root, _, files in os.walk(base_folder):
        for file in files:
            if file.lower().endswith(".wav"):
                analyze_wav(os.path.join(root, file))


if __name__ == "__main__":
    input_wav_folder = "/home/wav"
    batch_analyze(input_wav_folder)
    print("\nAll .wav files have been processed.")

# This script analyzes .wav files in the specified directory, generating spectrograms and summary statistics.
# It uses the scipy library for audio processing and matplotlib for plotting.
# The script is designed to be run in a Python environment with the necessary libraries installed.
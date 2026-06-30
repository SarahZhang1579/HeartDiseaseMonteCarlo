"""
Author: Sarah Zhang
Date: 2026/06/28
Description: Load ECG (Electrocardiogram) data from Fantasia and BIDMC Congestive Heart Failure
files.
"""
import wfdb
import numpy as np
# import neurokit2 as nk
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

record = wfdb.rdrecord("../data/fantasia/f1o01")

ecg_index = record.sig_name.index("ECG")
ecg = record.p_signal[:, ecg_index]

fs = record.fs  # 250 Hz

plt.figure(figsize=(12, 4))
plt.plot(ecg[:4 * fs])   # First 4 seconds
plt.title("ECG (First 4 Seconds)")
plt.xlabel("Sample")
plt.ylabel("Voltage (mV)")
plt.show()

annotation = wfdb.rdann("../data/fantasia/f1o01", "ecg")

print(annotation.sample[:20])

time = annotation.sample / record.fs
RR = np.diff(time)

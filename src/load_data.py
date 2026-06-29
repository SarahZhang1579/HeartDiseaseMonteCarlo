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

print(record)

ecg = record.p_signal

print(ecg.shape)

plt.figure(figsize=(12, 4))
plt.plot(ecg[:5000, 0])
plt.xlabel("Sample")
plt.ylabel("Voltage")
plt.title("ECG")
plt.show()

annotation = wfdb.rdann("../data/fantasia/f1o01", "ecg")

print(annotation.sample[:20])

time = annotation.sample / record.fs
RR = np.diff(time)

"""
Author: Sarah Zhang
Date: 2026/06/28
Description: Compute HRV metrics for each patient using ECG data
"""
import math
import numpy as np


def extract_rr(annotation, record):
    """
    Extract the RR intervals from a patient
    :param annotation:
    :param record:
    :return:
    """
    time = annotation.sample / record.fs
    rr = np.diff(time)
    return rr


def filter_nn(rr: list) -> list:
    """
    Helper function for compute_sdnn. Removes premature beats, artifacts, or missed beats and
    leaves Normal-to-Normal intervals.
    :param rr:
    :return:
    """


def compute_hr(ecg: list):
    """

    :param ecg:
    :return:
    """


def compute_sdnn(nn: list) -> float:
    """ Computes Standard Deviation of NN intervals (SDNN) from a 5 minute (Short-Term) recording
    time. This recording time is commonly used for standardized clinical and wearable assessments.
    Primarily captures parasympathetic (vagal) activity.
    """
    return np.std(nn)


def compute_rmssd(rr: list) -> float:
    """ Computes Root Mean Square of Successive Differences (RMSSD).
    """
    data = []
    for i in range(len(rr) - 1):
        rr_interval = rr[i + 1] - rr[i]  # calculate successive rr intervals
        data.append(rr_interval**2)  # square the difference
    mean = np.mean(data)  # find the mean of  the squared differences
    return math.sqrt(mean)  # return RMSSD

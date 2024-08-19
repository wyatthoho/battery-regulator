from math import pi
import csv

import matplotlib.pyplot as plt
import numpy as np

FREQ_MIN, FREQ_MAX, INC_NUM = 7, 200, 1000
G = 9806.65  # mm/s2
ACC_TGT = 2 * G
ACC_MIN = 1 * G
DISP_MAX = 0.8  # mm

FIG_SIZE = [4.8, 3.0]
FIG_TITLE = 'Acceleration for UN38.3'
FIG_LABEL_X = 'Frequency, Hz'
FIG_LABEL_Y = 'Acceleration, g'
FIG_YLIM = [0, 2.2]

CSV_NAME = 'un383_acceleration.csv'
CSV_FIELD_1, CSV_FIELD_2 = 'freq(Hz)', 'acceleration(g)'
CSV_ROUND = 5


def get_disp(freq: float, a_amp: float) -> float:
    return a_amp / (2 * pi * freq)**2


def get_acc(freq: float, d_amp: float) -> float:
    return d_amp * (2 * pi * freq)**2


def get_accs(freqs: np.ndarray) -> np.ndarray:
    accs = []
    for freq in freqs:
        disp = get_disp(freq, ACC_TGT)
        if disp > DISP_MAX:
            acc = get_acc(freq, DISP_MAX)
        else:
            acc = ACC_TGT
        if acc < ACC_MIN:
            acc = ACC_MIN
        accs.append(acc/G)
    return np.array(accs)


def plot_accs(freqs: np.ndarray, accs: np.ndarray) -> None:
    plt.figure(figsize=FIG_SIZE, tight_layout=True)
    ax = plt.axes()
    ax.plot(freqs, accs)
    ax.set_title(FIG_TITLE)
    ax.set_xlabel(FIG_LABEL_X)
    ax.set_ylabel(FIG_LABEL_Y)
    ax.set_xlim([FREQ_MIN, FREQ_MAX])
    ax.set_ylim(FIG_YLIM)
    ax.grid()
    plt.show()


def output_csv(csv_name: str, freqs: np.ndarray, accs: np.ndarray):
    with open(csv_name, 'w', newline='') as f:
        fieldnames = [CSV_FIELD_1, CSV_FIELD_2]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for freq, acc in zip(freqs, accs):
            row = {
                CSV_FIELD_1: round(freq, CSV_ROUND),
                CSV_FIELD_2: round(acc, CSV_ROUND)
            }
            writer.writerow(row)


def main():
    freqs = np.linspace(FREQ_MIN, FREQ_MAX, INC_NUM)
    accs = get_accs(freqs)
    plot_accs(freqs, accs)
    output_csv(CSV_NAME, freqs, accs)


if __name__ == '__main__':
    main()

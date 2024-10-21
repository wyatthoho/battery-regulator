import csv
import math

import matplotlib.pyplot as plt
import numpy as np

FREQ_MIN, FREQ_MAX, INC_NUM = 0.3, 50, 15
FREQ_1, FREQ_2, FREQ_3 = 1.1, 8.0, 33.0
G = 9806.65  # mm/s2
DAMPING = 2  # %

FIG_SIZE = [4.8, 3.0]
FIG_TITLE = 'Required Response Spectum'
FIG_LABEL_X = 'Frequency, Hz'
FIG_LABEL_Y = 'Acceleration, g'
FIG_XLIM = [0.1, 100.0]
FIG_YLIM = [0.5, 3.5]

CSV_NAME = 'ieee_693_spectrum.csv'
CSV_FIELD_1, CSV_FIELD_2 = 'freq(Hz)', 'acceleration(g)'
CSV_ROUND = 5


def get_freqs() -> np.ndarray:
    freqs_sec1 = np.linspace(FREQ_MIN, FREQ_1, INC_NUM)
    freqs_sec2 = np.linspace(FREQ_1, FREQ_2, INC_NUM)
    freqs_sec3 = np.linspace(FREQ_2, FREQ_3, INC_NUM)
    freqs_sec4 = np.linspace(FREQ_3, FREQ_MAX, INC_NUM)
    return np.concatenate((freqs_sec1[:-1], freqs_sec2[:-1], freqs_sec3[:-1], freqs_sec4))


def get_accs(freqs: np.ndarray) -> np.ndarray:
    beta = (3.21 - 0.68 * math.log(DAMPING)) / 2.1156
    accs = np.array([])
    for freq in freqs:
        if freq <= FREQ_1:
            acc = 2.288 * beta * freq
        elif freq <= FREQ_2:
            acc = 2.5 * beta
        elif freq <= FREQ_3:
            acc = (26.4 * beta - 10.56) / freq - 0.8*beta + 1.32
        else:
            acc = 1.0
        accs = np.append(accs, acc)
    return accs


def plot_accs(freqs: np.ndarray, accs: np.ndarray) -> None:
    plt.figure(figsize=FIG_SIZE, tight_layout=True)
    ax = plt.axes()
    ax.semilogx(freqs, accs)
    ax.set_title(FIG_TITLE)
    ax.set_xlabel(FIG_LABEL_X)
    ax.set_ylabel(FIG_LABEL_Y)
    ax.set_xlim(FIG_XLIM)
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
    freqs = get_freqs()
    accs = get_accs(freqs)
    plot_accs(freqs, accs)
    output_csv(CSV_NAME, freqs, accs)


if __name__ == '__main__':
    main()

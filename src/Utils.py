# utils.py

import os
import matplotlib.pyplot as plt

def save_plot(filename, folder='../outputs/plots', dpi=300, tight=True, show=True):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)

    if tight:
        plt.tight_layout()

    plt.savefig(path, dpi=dpi)

    if show:
        plt.show()
    else:
        plt.close()


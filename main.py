import matplotlib.pyplot as plt
import numpy as np


x = np.array([2023, 2024,2025,2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 23, 38, 5])



plt.plot(x,y1, marker=".",
                    ms=30,
                    mfc="#1cd3fc",
                    mec="#1cd3fc",
                    ls="solid",
                    lw=4,
                    color="#1c5bfc")

plt.plot(x,y2, marker=".",
                      ms=30,
                      mfc="#1cd3fc",
                      mec="#1cd3fc",
                      ls="solid",
                      lw=4,
                      color="#1c5bfc")

plt.show()




import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

src = "./results"
for file_name in os.listdir(src):
    path = src + "/" + file_name
    df = pd.read_csv(path)

    y = df["validation error1"].values.tolist()
    plt.plot(y, label=file_name.split(".")[0])

x = np.linspace(0, 100, 100)
y = [6 for i in range(100)]
plt.plot(x, y, ':r')
plt.xlabel("epoch")
plt.ylabel("validation error")
plt.ylim(0, 30)
plt.legend()
plt.savefig("experiment.png")
print("Experiment plot is successfully generated")

import numpy as np
abc = np.load("jobs.npz", allow_pickle=True)

def findPraktikum():
    for i in abc["saved"]:
        if "Internship Machine Learning for Human Action Recognition" in i:
            print(i)


findPraktikum()
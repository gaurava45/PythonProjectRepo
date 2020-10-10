import pickle

with open("myiris.pkl", "rb") as f:
    print(pickle.load(f))
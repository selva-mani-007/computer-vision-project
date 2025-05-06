import pickle

# Save test data
test_data = {"key": "value"}

with open("test.pkl", "wb") as f:
    pickle.dump(test_data, f)

# Load the saved test data
with open("test.pkl", "rb") as f:
    loaded_data = pickle.load(f)

print(loaded_data)

import os
import warnings

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
warnings.filterwarnings("ignore", category=FutureWarning)

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Input
from keras.callbacks import EarlyStopping

print("\n--- Keras Demo  ---")

# Data
X = np.array([[1], [2], [3]], dtype=float)
y = np.array([[2], [4], [6]], dtype=float)

# Model
model = Sequential([
    Input(shape=(1,)),
    Dense(1)   # simple linear model
])

# Compile
model.compile(optimizer='adam', loss='mse')

# Train
model.fit(
    X, y,
    epochs=500,
    verbose=0,
    callbacks=[EarlyStopping(monitor="loss", patience=20)]
)

# Predict
pred = model.predict(np.array([[4]], dtype=float), verbose=0)
print("Prediction for 4:", pred)

# Save
model.save("keras_model.keras")
print("Model saved successfully")

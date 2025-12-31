import os
import warnings

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
warnings.filterwarnings("ignore", category=FutureWarning)

import numpy as np
import tensorflow as tf

print("\n--- TensorFlow Demo ---")

X = np.array([[1], [2], [3]], dtype=float)
y = np.array([[2], [4], [6]], dtype=float)

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer="adam", loss="mse")
model.fit(X, y, epochs=300, verbose=0)

pred = model.predict(np.array([[4]], dtype=float), verbose=0)
print("Prediction:", pred , "\n")

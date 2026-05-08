from tensorflow import keras

# Load the model
model = keras.models.load_model("BCE.keras")

# Print model summary
model.summary()

# Check details
print("Loss function:", model.loss)
print("Metrics:", model.metrics_names)
print("Input shape:", model.input_shape)
print("Output shape:", model.output_shape)

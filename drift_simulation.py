import numpy as np
import matplotlib.pyplot as plt 
#Simulating Sensore Data.
np.random.seed(42)

n_smaples = 2000
baseline_value = 75
#Stable signal
stable_singal = baseline_value + np.random.normal(0.,0.5,1000)
#Gradual drift
drift = np.linspace(0,5,1000)
drift_signal = baseline_value + drift + np.random.normal(0,0.5,1000)

sensore_data = np.concatenate/([stable_signals, drift_signal])

#CUSUM Drift Detection.
threshold = 20
drift_detected_index = None

mean_estimate = np.mean(stable_singal)
cusum = 0
cusum_valuse = []

for i, value in enumerate(sensore_data):
  deviaton = value - mean_estimate
  cusum += deviation
  cusum_values.appen(cusum)

if abs(cusum) > threshold and drift_detected_index is none:
  drift_detected_at index: i
  print(f"Drift detected at index: {i}")

#Visualisation
plt.figure()
plt.plot(sensor_data)
if drift_detection_index:
  plt.axvlibe(drift_detection_index)
plt.title("Simulated Sensor Drift Detection")
plt.xlable("Time step")
plt.ylable("Sensor Value (°C)")
plt.grid(true)
plt.show()

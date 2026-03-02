# Sensor-Drift-Detection
This project simulates gradual sensor drift and applies a statistical detection method (CUSUM) to identify deviations from baseline behavior.  
Sensor drift is a critical issue in automotive and industrial systems. Gradual bias in temperature, vibration, or pressure sensors can lead to inaccurate control decisions, reduced efficiency, or safety risk.  
This project demonstrates a simplified monitoring inspried by industrial quality control methods.

## Problem Context
**In automotive systems, sensor montior:**  
-Engine temperature  
-Battery health  
-Vibration Levels  
-Pressure systems

**Overtime, sensors may drift due to:**  
-Component wear  
-Environmental exposure  
-Calibration degradation  
Detecting drift early enable predicive maintenance and prevents systems failures

## Methodology
1. Simulated a stable sensore signal with Gaussian noise.
2. Introduced gradual liner drift after a stable period.
3. Applied the CUSUM (Cumulative Sum) alogorithem to detect sustained deviation from baseline.
4. Flagged drift when cumulative deviation exceeded a threshold.
CUSUM is widely used in the industrial deviation monitoring and quality assurance.

## Results
**The algorithm successfully detects gradual drift before extreme deviation, occurs,
demonstrating its suitability for:**  
Vehicle sensor diagnostics  
Manufaturing quality monitoring  
Predictive maintenance systems

## Technologies Used
Python  
Numpy  
Matplotlib

# Future Improvements
Adaptive thresolds  
Real-world sensor dataset integration  
Multivariate drift detection  
Real-time monitoring system

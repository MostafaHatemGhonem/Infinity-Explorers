# Rocket-GPS-INS-Fusion 🚀

A comprehensive Data Acquisition (DAQ) and Sensor Fusion system for rocket trajectory tracking. This project integrates GPS and Inertial Navigation System (INS) data using a Kalman Filter to provide accurate real-time position, velocity, and acceleration estimates during flight.

## 🌟 Overview

Check out our **[Live Interactive Demo](https://rocketgpsinsfusion-opal.vercel.app/)** to explore the hardware architecture, software pipeline, and test the Kalman logic directly in your browser.

The system consists of two main components:
1. **Hardware/Firmware:** An Arduino-based DAQ system reading data from an MPU6050 (Accelerometer/Gyroscope) and a GPS module, transmitting binary data over serial.
2. **Software (Python):** A desktop application that receives the serial data, processes it through kinematics algorithms and a Kalman Filter, and visualizes the flight trajectory and telemetry in real-time.

## 📁 Project Structure

- `firmware/`: Arduino sketches for data acquisition and sensor interfacing.
  - `daq_system/`: Main Arduino code for reading MPU6050 and GPS sensors.
- `src/`: Core Python source code.
  - `kinematics.py`: INS calculations and basic kinematic integrations.
  - `kalman_filter.py`: Implementation of the Kalman Filter for sensor fusion.
  - `visualizer.py`: Real-time plotting and 3D visualization of the rocket's trajectory.
  - `data_types.py`: Data structures and classes for handling sensor data.
  - `main.py`: Entry point for the Python application.
- `tests/`: Scripts and mock data for testing the system without physical hardware.

## 🛠️ Hardware Requirements

- Microcontroller (e.g., Arduino Nano / Uno)
- MPU6050 (6-DOF Accelerometer and Gyroscope)
- GPS Module (e.g., NEO-6M, connected via SoftwareSerial)
- Appropriate wiring and power supply

## 🚀 Getting Started

### 1. Firmware Setup
1. Open the `firmware/daq_system/daq_system.ino` in the Arduino IDE.
2. Install the required libraries via the Arduino Library Manager: 
   - `Adafruit MPU6050`
   - `Adafruit Unified Sensor`
   - `TinyGPSPlus`
3. Compile and upload the code to your Arduino board.

### 2. Software Setup
Ensure you have Python 3.8+ installed.

1. Navigate to the project directory:
   ```bash
   cd GNC/Rocket-GPS-INS-Fusion
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the main application:
   ```bash
   python src/main.py
   ```

## 👥 Contributors / فريق العمل

- **Omar (عمر)**: Arduino Firmware & Sensor Integration / أكواد الأردوينو والمستشعرات
- **Mariam (مريم)**: INS & Kinematics Calculations / حسابات INS
- **Tasneem (تسنيم)**: Kalman Filter Implementation / مرشح كالمان
- **Alaa (ألاء)**: Data Visualization / الرسم البياني
- **Mostafa (مصطفى)**: Main Application & System Integration / نقطة الإدخال ودمج النظام

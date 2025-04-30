# 🔊 Audio Amplifier Circuit using 2N2222 Transistors

This project is a 3-stage BJT amplifier circuit designed to amplify low-level AC signals (e.g., audio input from a mobile phone or signal generator) to drive a small speaker.

## ⚙️ Components and Their Functions

| Label | Component Type     | Value     | Function                                                                 |
|-------|--------------------|-----------|--------------------------------------------------------------------------|
| C1    | Capacitor (Electrolytic) | 22μF      | Coupling capacitor – blocks DC and allows AC audio signal to pass.       |
| C2–C4 | Capacitors          | 22μF each | Inter-stage coupling between transistor stages – blocks DC bias shift.   |
| R1, R7, R11 | Resistors    | 47kΩ      | Collector pull-up resistors – provides Vcc to collector.                 |
| R2, R6, R10 | Resistors     | 4.7kΩ     | Bias resistors – sets base bias for Q1, Q2, Q3 respectively.             |
| R3, R8, R12 | Resistors     | 4.7kΩ     | Bias resistors – part of voltage divider with R2/R6/R10.                 |
| R4, R5, R9 | Resistors      | 820Ω      | Emitter resistors – improves stability and sets gain.                    |
| Q1–Q3 | BJT Transistors     | 2N2222    | NPN transistor amplifiers – provide signal gain.                         |
| LS1   | Speaker             | —         | Audio output – converts the amplified signal into sound.                 |
| Rout  | Resistor            | 47kΩ      | Pull-down resistor for speaker load stability.                           |

## 🔌 Signal Flow

1. The audio signal enters via C1 from AUX or function generator.
2. Q1 amplifies the signal and passes it through C2 to the next stage.
3. Q2 and Q3 provide further gain through the same mechanism.
4. Output is coupled via C4 to LS1 (speaker), while DC is blocked.
5. 


# 🔊 Audio Amplifier Using 2N2222 Transistors

## 📌 Project Description

This project is a simple 3-stage audio amplifier circuit using 2N2222 bipolar junction transistors (BJTs). It amplifies a low-level input audio signal (such as from a phone via AUX) to drive a small speaker and produce audible sound.

---

## 🖼️ Circuit Diagram

> See the included image for the full schematic.


## ⚙️ How It Works

1. The audio input (e.g., from a phone’s AUX) enters the circuit through capacitor C1, which blocks DC.
2. The signal passes through three amplification stages (Q1 → Q2 → Q3).
3. Each stage increases the voltage and power of the signal.
4. Coupling capacitors (C2, C3, C4) isolate DC biasing between the stages.
5. The final amplified signal is fed to the speaker through capacitor C4.

---

## 🔌 Connections

- Audio Input: Connect AUX input (tip = signal, sleeve = GND) through capacitor C1.
- Output: The speaker (LS1) connects after the final stage through C4.
- Vcc: Connect to the top rails of R1, R7, and R11 (positive terminal of the power supply).
- GND: Ground all lower connections including the negative terminal of AUX and the emitter resistors.

---

## ✅ Notes

- Ensure correct polarity for electrolytic capacitors.
- Use a regulated DC power supply (9V–12V recommended).
- You may replace the audio input with a function generator (sine wave input).
- The output volume can be adjusted by changing the gain (resistor values).
- The circuit is suitable for small speakers; not designed for high power output.

---

## 🧠 Developed by

- ✍️ Infity Explorers

## 🧠 Applications

- Basic analog amplifier teaching circuit.
- Audio pre-amplifier in DIY audio electronics.
- Phase-shift and signal observation at each stage.


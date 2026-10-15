# IoT Hardware Architecture & Embedded System Specifications

This directory contains the engineering specifications, sensor fusion matrices, and priority arbitration hierarchies for the smart lamppost infrastructure model proposed in:
**"An IoT-Based Infrastructure Model for Reducing Urban Light Pollution: Empirical Assessment and System Design in Dhaka"**
by Md Reyad Hasan and Ishrat Jahan Riya.

---

## 🏛️ Vertically Stratified Four-Zone Lamppost Topology

To avoid optical and thermal cross-interference between sensors and luminaires, each lamppost node is partitioned into four vertical functional zones along the pole shaft:

```
[Zone 1: Apex Top Cap]   --> Sky-facing BH1750 ALS + DS3231 RTC + BME280 Atmospheric Sensor
                                  │
[Zone 2: Luminaire Head] --> Full-Cutoff Shielded LED Array (PWM 0-255) + INA219 Power Monitor
                                  │
[Zone 3: Mid-Shaft (3-4m)]--> ESP32-S3 Sense + OV2640 Camera (TinyML) + HB100 Microwave Radar
                                  │
[Zone 4: Base Zone (1-1.5m)]-> AM312 Passive Infrared (PIR) Sidewalk Pedestrian Array
```

---

## 📄 Hardware Artifacts & Engineering Schematics

| Document / Schematic | Description |
| :--- | :--- |
| [`sensor_architecture_matrix.pdf`](file:///c:/Code/Light-Pollution/hardware/sensor_architecture_matrix.pdf) | **Multi-Modal AI Sensor-Fusion Architecture Matrix:** Maps all seven sensing modalities (HB100 Radar, PIR Array, OV2640 Edge Camera, BH1750 ALS, DS3231 RTC, BME280, INA219) to their hardware interfaces, target differentiation logic, and vehicle vs. pedestrian rules. |
| [`priority_arbitration_hierarchy.pdf`](file:///c:/Code/Light-Pollution/hardware/priority_arbitration_hierarchy.pdf) | **Deterministic Priority Arbitration Hierarchy:** Detailed decision matrix specifying winning behaviors, PWM duty cycles, decay timers, and engineering rationales for simultaneous multi-sensor conflicts across Ranks 1 to 6. |
| [`smart_lamppost_data_dictionary.pdf`](file:///c:/Code/Light-Pollution/hardware/smart_lamppost_data_dictionary.pdf) | **Multi-Functional Smart Lamppost Data Dictionary:** Comprehensive technical specifications, communication interface standards, and positioning device attributes. |

---

## ⚡ Key Embedded Hardware Specifications

- **Microcontroller:** Seeed Studio XIAO ESP32-S3 Sense (Dual-core Xtensa LX7 @ 240 MHz, 8 MB Octal PSRAM, SIMD Vector Instructions).
  - *Core 0:* Deterministic ISRs for HB100 Doppler frequency counting, PIR interrupts, $\text{I}^2\text{C}$ sensor polling, and connectionless ESP-NOW broadcasting.
  - *Core 1:* Dedicated INT8-quantized TinyML vision inference (YOLOv8-nano / MobileNet @ 2–5 FPS, $96 \times 96$ input tensor) for target classification (`car`, `truck`, `person`) and false-trigger rejection ($>85\%$ confidence threshold).
- **Communication Protocol:** OSI Layer-2 ESP-NOW peer-to-peer broadcasts ($<10\text{ ms}$ latency; restricted vehicular slip to $10\text{--}13\text{ cm}$ at $60\text{--}80\text{ km/h}$).
- **Energy Baseline:** 10% eco-mode baseline ($\text{PWM} = 26$) during vacant periods; dynamic $30\text{--}40\text{ m}$ look-ahead bubble ($100\%$ PWM) ahead of approaching vehicles; $40\%\text{--}50\%$ localized safety envelope for pedestrians.
- **Fail-Safe Mechanism:** Hardware watchdog with automatic $100\%$ full-beam fallback ($\text{PWM} = 255$) upon catastrophic sensor-bus hang or processor stall.


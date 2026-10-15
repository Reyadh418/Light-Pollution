# An IoT-Based Infrastructure Model for Reducing Urban Light Pollution: Empirical Assessment and System Design in Dhaka

[![DOI](https://zenodo.org/badge/1263758734.svg)](https://doi.org/10.5281/zenodo.23399530)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Open Access](https://img.shields.io/badge/Open_Access-FAIR_Compliant-blue.svg)](https://www.go-fair.org/fair-principles/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

---

## 📖 Executive Summary & Abstract

Unregulated **artificial light at night (ALAN)** across rapidly expanding megacities produces severe atmospheric skyglow, ecological degradation, human circadian disruption, and extensive municipal energy waste. Ground-level photometric data in developing South Asian urban centers remains scarce, and municipal roadway lighting continues to operate on static, all-night full-beam regimes.

This repository provides an integrated empirical dataset and an autonomous, decentralized Internet of Things (IoT) streetlight infrastructure model tailored for Dhaka, Bangladesh:
1. **Empirical Photometric Audit:** $N = 220$ ground-level lux measurements across 13 distinct functional urban sectors in Dhaka, alongside 12 controlled benchtop luminaire experiments evaluating luminaire tilt angle, mounting elevation, LED spectral wavelength, optical cutoff shielding, and architectural window glazing.
2. **Four-Zone Edge AI Sensor-Fusion Node:** An autonomous lamppost node powered by the dual-core **ESP32-S3 Sense** microcontroller (utilizing hardware SIMD vector instructions) fusing seven sensing modalities: an OV2640 camera running quantized TinyML vision models (YOLOv8-nano / MobileNet), an HB100 microwave Doppler radar, a sidewalk-directed PIR array, a sky-facing BH1750 ambient light sensor, a BME280 atmospheric module, a DS3231 TCXO real-time clock, and an INA219 power telemetry monitor.
3. **Sub-10 ms Predictive Look-Ahead via ESP-NOW:** Bypassing heavy TCP/IP stacks in favor of connectionless OSI Layer-2 ESP-NOW action frames ($<10\text{ ms}$ latency), detecting nodes awaken a dynamic **"rolling luminescence bubble"** 30–40 m ahead of approaching vehicles, restricting vehicular slip distance to just 10–13 cm at 60–80 km/h.
4. **Deterministic Conflict Resolution & Fail-Safe State Machine:** A deterministic six-rank priority hierarchy and edge-case state machine enforcing automated post-midnight 50% skyglow curfews, weather-adaptive safety scaling, and a 100% full-beam fail-safe fallback during hardware anomalies.

---

## 👥 Authors & Affiliations

- **Md Reyad Hasan** (Corresponding Author: [`reyadh418@gmail.com`](mailto:reyadh418@gmail.com))  
  *Government Science College, Dhaka, Bangladesh*
- **Ishrat Jahan Riya** ([`ishratjahanriya123@gmail.com`](mailto:ishratjahanriya123@gmail.com))  
  *Mavenwood International School, Dhaka, Bangladesh*

**Date of Release:** August 23, 2026  
**Primary Repository:** [https://github.com/Reyadh418/Light-Pollution](https://github.com/Reyadh418/Light-Pollution)

---

## 📊 Key Empirical Findings

### Field Audit Across 13 Urban Sectors ($N = 220$)
- **Overall Mean Illuminance:** **802.5 lx** across all surveyed sites—exceeding international roadway safety baselines (IES RP-8 upper threshold of 30.0 lx) by more than **$26\times$**.
- **Extreme Commercial Trespass:** Unshielded commercial retail corridors drive severe lateral light pollution:
  - **Fashion & Apparel:** Mean $1{,}401.3\text{ lx}$, peaking at **$4{,}925.0\text{ lx}$** ($164.2\times$ roadway standard).
  - **Mobile & Electronics Showrooms:** Mean $1{,}458.4\text{ lx}$, peaking at **$3{,}200.0\text{ lx}$**.
  - **Super Shops & Malls:** Mean $755.9\text{ lx}$, peaking at **$4{,}303.0\text{ lx}$**.
- **Erratic Municipal Roadways ($n = 21$):** Severe spatial non-uniformity ranging from hazardous, dark transit pockets (**5.0 lx** at Kallyanpur Bus Stand) to glaring **500.0 lx** concentrations on arterial main roads (mean: 74.0 lx), operating at static 100% output with zero low-traffic dimming.
- **Sensitive Baselines:** Residential buildings ($79.5\text{ lx}$), educational institutions ($65.1\text{ lx}$), and offices ($61.5\text{ lx}$) remain under 80 lx, leaving occupants vulnerable to commercial facade trespass.

### Controlled Benchtop Luminaire Trials ($n = 12$)
- **Mounting Geometry:** Elevating the luminaire to 8.0 in with a horizontal cutoff profile ($0^\circ$) reduces concentrated ground hotspot intensity by **58.6%** (from 632.4 lx to 261.7 lx) compared to a $90^\circ$ vertical emission.
- **Spectral Selection:** Warm yellow/amber LEDs (390.9 lx mean) prevent the severe **+90.0% peak glare surge** induced by short-wavelength blue emitters (865.5 lx peak).
- **Optical Shielding:** Triangular and square cutoff hoods concentrate redirected downward lumens by **+11.9% to +13.7%**, suppressing stray lateral flux.
- **Architectural Glazing:** Tinted attenuating window glazing reduces indoor light trespass by **46.7%** (from 122.3 lx to 65.2 lx) relative to standard transparent glass.

---

## 🏛️ System Architecture

### Vertically Stratified Four-Zone Topology
```
[Zone 1: Apex Top Cap]   --> Sky-facing BH1750 ALS + DS3231 RTC + BME280 Atmospheric Sensor
                                  │
[Zone 2: Luminaire Head] --> Full-Cutoff Shielded LED Array (PWM 0-255) + INA219 Power Telemetry
                                  │
[Zone 3: Mid-Shaft (3-4m)]--> ESP32-S3 Sense + OV2640 Camera (TinyML) + HB100 Microwave Radar
                                  │
[Zone 4: Base Zone (1-1.5m)]-> AM312 Passive Infrared (PIR) Sidewalk Pedestrian Array
```

### Dual-Core Processing Partitioning
- **Core 0 (Deterministic ISRs & Networking):** Microwave Doppler frequency counting, PIR GPIO interrupts, $\text{I}^2\text{C}$ sensor polling, hardware timer PWM dimming, and connectionless Layer-2 ESP-NOW broadcasting.
- **Core 1 (Accelerated TinyML Vision):** INT8-quantized YOLOv8-nano / MobileNet inference at 2–5 FPS on downscaled $96 \times 96$ tensors, classifying road users (`car`, `truck`, `person`) and filtering out non-human false triggers ($>85\%$ confidence).

### Predictive Look-Ahead & Energy Savings
- **Layer-2 ESP-NOW Mesh:** Wakes downstream lampposts in $<10\text{ ms}$, restricting vehicular slip distance to **$0.10\text{--}0.13\text{ m}$** (compared to $7.0\text{--}9.3\text{ m}$ for 4G/LTE cloud brokers and $>20\text{ m}$ for LoRaWAN).
- **Net Electricity Reduction:** Reduces municipal streetlight power draw by **49.0%** on arterial corridors, **61.5%** on collector roads, and **75.9%** on residential streets.
- **Post-Midnight Skyglow Curtailment:** Suppresses upward and lateral luminous flux by **78.8% to 88.3%** during the critical biological window (00:00–06:00).

---

## 📁 Repository Structure

```
Light-Pollution/
├── .zenodo.json                         # Zenodo schema metadata for automated DOI minting
├── CITATION.cff                         # Citation File Format (CFF v1.2.0)
├── LICENSE                              # Creative Commons Attribution 4.0 International (CC-BY-4.0)
├── README.md                            # Primary project documentation
├── .gitignore                           # Excludes build artifacts while preserving source & data
│
├── paper/                               # Publication manuscript
│   ├── README.md                        # LaTeX compilation instructions
│   ├── finalPaper.tex                   # Self-contained LaTeX manuscript source
│   └── Light_Pollution.pdf              # Publication-ready compiled 21-page PDF
│
├── data/                                # FAIR-compliant open research data
│   ├── README.md                        # Comprehensive data dictionary and variable codebook
│   ├── dhaka_photometric_survey.csv     # Curated 220 in-situ measurements across 13 urban sectors
│   ├── benchtop_experiments.csv         # 12 controlled benchtop photometric experiments
│   └── raw/
│       └── Database (Light Pollution).xlsx # Original multi-sheet Excel field workbook
│
├── scripts/                             # Reproducibility and data processing pipelines
│   ├── reproduce_tables.py              # Generates Table 1 & Table 2 summary statistics
│   └── export_datasets.py               # Extraction pipeline converting raw Excel to standardized CSVs
│
├── hardware/                            # IoT system specifications and decision logic
│   ├── README.md                        # Hardware topology and component overview
│   ├── sensor_architecture_matrix.pdf   # 7-modality sensor selection and logic matrix (Table 3)
│   ├── priority_arbitration_hierarchy.pdf # Deterministic 6-tier conflict-resolution hierarchy (Table 5)
│   └── smart_lamppost_data_dictionary.pdf # Multifunctional smart lamppost engineering specifications
└── references/                          # Academic literature bibliography
    └── REFERENCES.md                    # Bibliographic index with DOIs and official access links
```

---

## 🔬 Data Access & Reproduction

### 1. Requirements
Ensure Python 3.10 or higher is installed with `openpyxl`:
```bash
pip install openpyxl
```

### 2. Reproduce Summary Tables
To recalculate and display the exact statistical metrics for **Table 1** (cross-sectoral field survey) and **Table 2** (benchtop luminaire trials):
```bash
python scripts/reproduce_tables.py
```

### 3. Re-export CSVs from Raw Excel
To execute the raw data parsing and standardization pipeline:
```bash
python scripts/export_datasets.py
```

---

## 🛠️ Compiling the Manuscript

The manuscript source is located in [`paper/finalPaper.tex`](file:///c:/Code/Light-Pollution/paper/finalPaper.tex). To compile using `latexmk`:

```bash
cd paper
latexmk -pdf finalPaper.tex
```

Or using `pdflatex`:
```bash
cd paper
pdflatex finalPaper.tex
pdflatex finalPaper.tex
```

The pre-compiled PDF is accessible directly at [`paper/Light_Pollution.pdf`](file:///c:/Code/Light-Pollution/paper/Light_Pollution.pdf).

---

## 📜 Citation

If you utilize this dataset, hardware design, or paper in your research, please cite:

### BibTeX
```bibtex
@article{hasan2026lightpollution,
  title={An {IoT}-Based Infrastructure Model for Reducing Urban Light Pollution: Empirical Assessment and System Design in {Dhaka}},
  author={Hasan, Md Reyad and Riya, Ishrat Jahan},
  year={2026},
  month={aug},
  doi={10.5281/zenodo.placeholder},
  url={https://github.com/Reyadh418/Light-Pollution},
  note={Open access research repository and dataset deposited on Zenodo}
}
```

### APA Style
> Hasan, M. R., & Riya, I. J. (2026). *An IoT-Based Infrastructure Model for Reducing Urban Light Pollution: Empirical Assessment and System Design in Dhaka*. Zenodo. https://doi.org/10.5281/zenodo.placeholder

---

## ⚖️ License & Open Access

This project is released under the **Creative Commons Attribution 4.0 International Public License (CC-BY-4.0)**. You are free to share, copy, adapt, and build upon this work for any purpose, including commercially, provided appropriate attribution is given to the original authors.

See the full license terms in [`LICENSE`](file:///c:/Code/Light-Pollution/LICENSE).

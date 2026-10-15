# Empirical Datasets & Data Dictionary

This directory contains the primary research datasets supporting the study:
**"An IoT-Based Infrastructure Model for Reducing Urban Light Pollution: Empirical Assessment and System Design in Dhaka"**
by Md Reyad Hasan and Ishrat Jahan Riya.

All data are provided under the **Creative Commons Attribution 4.0 International (CC-BY-4.0)** license.

---

## 📁 Directory Contents

| File | Format | Description |
| :--- | :--- | :--- |
| [`dhaka_photometric_survey.csv`](file:///c:/Code/Light-Pollution/data/dhaka_photometric_survey.csv) | Open CSV (UTF-8) | In-situ ground-level photometric audit across 13 urban sectors in Dhaka, Bangladesh ($N = 214$ curated observations). |
| [`benchtop_experiments.csv`](file:///c:/Code/Light-Pollution/data/benchtop_experiments.csv) | Open CSV (UTF-8) | Controlled benchtop trials testing mounting orientation, height, LED spectral color, cutoff shielding, and glazing ($n = 12$). |
| [`raw/Database (Light Pollution).xlsx`](file:///c:/Code/Light-Pollution/data/raw/Database%20(Light%20Pollution).xlsx) | Microsoft Excel | Original multi-sheet raw field database preserved for archival provenance. |

---

## 📊 Data Dictionary: `dhaka_photometric_survey.csv`

This dataset contains field-measured illuminance levels recorded using a calibrated digital lux meter across major commercial, transit, residential, and institutional corridors in Dhaka (including Shyamoli, Mirpur-1, Mirpur-2, Mohammadpur, Kallyanpur, Kawran Bazar, Farmgate, Shahbagh, Shere Bangla Nagar, Kakrail, Saydabad, and Jatrabari), with suburban baselines in Gazipur and Cumilla.

### Field Attributes

| Column Name | Data Type | Units / Range | Description & Notes |
| :--- | :--- | :--- | :--- |
| `record_id` | String | e.g., `DH-FASH-001` | Unique site identifier formatted as `DH-[SECTOR_CODE]-[INDEX]`. |
| `sector` | String | 13 categories | Functional urban land-use classification (see list below). |
| `site_name` | String | Text | Establishment name, facility identifier, or roadway label (e.g., *Cats Eye*, *DPRC Hospital*, *Hanif Flyover*). |
| `area` | String | Text | Specific neighborhood, arterial road, or municipality in Dhaka / Greater Dhaka. |
| `measurement_position`| String | Text | Spatial sensor placement (e.g., `Outdoor`, `Entry`, `Sidewalk`, `Middle Road`, `Dining Table`). |
| `light_color` | String | Categorical | Dominant emitter visual spectrum (`White` [cool-white CCT], `Yellow` [warm-amber CCT], `Yellow+White`, `Blue`, `Multi-color`, or `Unspecified`). |
| `illuminance_lower_lx` | Float | Lux ($\text{lx}$) | Minimum directional illuminance measured at the location. |
| `illuminance_higher_lx`| Float | Lux ($\text{lx}$) | Maximum directional illuminance / localized peak recorded. |
| `illuminance_average_lx`| Float | Lux ($\text{lx}$) | Spatial mean illuminance calculated across directional passes. |

### Urban Sectors Represented
1. **Fashion & Apparel Retail** ($n = 62$)
2. **Variety Shops & Commercial Markets** ($n = 28$)
3. **Food & Restaurants** ($n = 26$)
4. **Roadways & Transit Nodes** ($n = 21$)
5. **Mobile & Electronics Showrooms** ($n = 20$)
6. **Hospitals & Healthcare Facilities** ($n = 14$)
7. **Super Shops & Shopping Malls** ($n = 11$)
8. **Residential Buildings & Housing** ($n = 11$)
9. **Schools, Coaching & Learning Centers** ($n = 9$)
10. **Vehicular & Automotive Corridors** ($n = 6$)
11. **Cinemas & Entertainment Complexes** ($n = 3$)
12. **Offices & Commercial Banking** ($n = 2$)
13. **Visitable Places & Cultural Heritage** ($n = 1$)

---

## 🔬 Data Dictionary: `benchtop_experiments.csv`

Controlled benchtop photometric trials isolating physical engineering variables that govern stray light emission, lateral trespass, and ocular glare.

### Field Attributes

| Column Name | Data Type | Units | Description & Notes |
| :--- | :--- | :--- | :--- |
| `experiment_id` | String | `A1`–`D2` | Systematic experiment code mapped directly to Table 2 of the manuscript. |
| `experiment_group` | String | Group A–D | Experimental category (see descriptions below). |
| `configuration_tested` | String | Text | Specific luminaire posture, emitter spectrum, optical shield, or glazing type. |
| `standoff_distance_inch`| Float | Inches ($\text{in}$) | Standoff distance between luminaire emission point and lux meter sensor head. |
| `tilt_angle_deg` | String / Float | Degrees ($^\circ$) | Luminaire tilt angle ($90^\circ$ = vertical nadir, $45^\circ$ = forward tilt, $0^\circ$ = horizontal cutoff; `N/A` for non-tilt groups). |
| `light_color` | String | Categorical | Emitter spectral color (`White`, `Yellow`, `Blue`). |
| `illuminance_min_lx` | Float | Lux ($\text{lx}$) | Minimum observed illuminance in trial. |
| `illuminance_mean_lx` | Float | Lux ($\text{lx}$) | Mean observed illuminance across trial run. |
| `illuminance_peak_lx` | Float | Lux ($\text{lx}$) | Peak glare intensity recorded at center of beam profile. |

### Experimental Groups
- **Group A: Mounting Orientation & Vertical Elevation ($n = 3$):** Isolates the effect of tilting and elevating the luminaire head from $90^\circ$ vertical (632.4 lx mean) to horizontal cutoff at 8.0 in elevation (261.7 lx mean, a 58.6% reduction in ground hotspot glare).
- **Group B: LED Spectral Wavelength Impact ($n = 3$):** Compares cool-white (448.0 lx), warm-yellow (390.9 lx), and short-wavelength blue emitters (surging to 638.0 lx mean, +63.2%, and 865.5 lx peak, demonstrating severe ocular glare).
- **Group C: Optical Cutoff Shielding Geometry ($n = 4$):** Evaluates unshielded bare emitters vs. planar (2D), triangular (conical), and square cutoff hoods, demonstrating redirected downward concentration ($+7.7\%$ to $+13.7\%$).
- **Group D: Architectural Window Glazing Attenuation ($n = 2$):** Measures light trespass transmission 2.0 in inside a window pane under standard transparent glass (122.3 lx mean) vs. attenuating tinted glass (65.2 lx mean, a 46.7% light trespass reduction).

---

## 🛠️ Reproduction & Data Validation

To re-generate summary statistics matching Table 1 and Table 2 in the paper, execute the reproduction script:

```bash
python scripts/reproduce_tables.py
```


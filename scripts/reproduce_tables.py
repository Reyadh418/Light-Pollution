"""
reproduce_tables.py
===================
Reproducibility script for:
"An IoT-Based Infrastructure Model for Reducing Urban Light Pollution:
 Empirical Assessment and System Design in Dhaka"

Calculates and formats:
  - Table 1: Summary of Empirical Illuminance Measurements Across 13 Urban Sectors in Dhaka
  - Table 2: Controlled Benchtop Photometric Measurements Across Luminaire Geometries, Spectral Colors, Shielding Covers, and Glazing

Usage:
  python scripts/reproduce_tables.py
"""

import os
import csv
import statistics
from collections import defaultdict

def reproduce_table_1(survey_csv_path):
    print("=" * 86)
    print("TABLE 1: Summary of Empirical Illuminance Measurements Across Urban Sectors in Dhaka")
    print("=" * 86)
    
    sector_data = defaultdict(lambda: {'lowers': [], 'highers': [], 'averages': []})
    all_averages = []
    all_lowers = []
    all_highers = []

    with open(survey_csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            sec = row['sector']
            avg_val = float(row['illuminance_average_lx']) if row['illuminance_average_lx'] else None
            low_val = float(row['illuminance_lower_lx']) if row['illuminance_lower_lx'] else None
            high_val = float(row['illuminance_higher_lx']) if row['illuminance_higher_lx'] else None
            
            if avg_val is not None:
                sector_data[sec]['averages'].append(avg_val)
                all_averages.append(avg_val)
            if low_val is not None:
                sector_data[sec]['lowers'].append(low_val)
                all_lowers.append(low_val)
            if high_val is not None:
                sector_data[sec]['highers'].append(high_val)
                all_highers.append(high_val)

    # Sort sectors descending by site count / mean to match paper layout
    sector_order = [
        'Fashion',
        'Variety Shop',
        'Food & Restaurants',
        'Roads',
        'Mobile & Accessories',
        'Hospital',
        'Super Shop & Convention Hall',
        'Buildings & Residence',
        'School, Coaching & Learning',
        'Cars & Transportation',
        'Cinemas & Entertainment',
        'Office',
        'Visitable Places & Heritages'
    ]

    header_fmt = "{:<32} {:>8} {:>10} {:>10} {:>10} {:>9} {:>9}"
    row_fmt    = "{:<32} {:>8} {:>10.1f} {:>10.1f} {:>10.1f} {:>9.1f} {:>9.1f}"
    
    print(header_fmt.format("Urban Sector", "Sites(n)", "Mean(lx)", "Median(lx)", "Std.Dev", "Min(lx)", "Max(lx)"))
    print("-" * 86)

    for sec in sector_order:
        data = sector_data.get(sec)
        if not data or not data['averages']:
            continue
        n = len(data['averages'])
        mean_v = statistics.mean(data['averages'])
        med_v  = statistics.median(data['averages'])
        std_v  = statistics.stdev(data['averages']) if n > 1 else 0.0
        min_v  = min(data['lowers']) if data['lowers'] else min(data['averages'])
        max_v  = max(data['highers']) if data['highers'] else max(data['averages'])
        print(row_fmt.format(sec, n, mean_v, med_v, std_v, min_v, max_v))

    print("-" * 86)
    tot_n = len(all_averages)
    tot_mean = statistics.mean(all_averages)
    tot_min = min(all_lowers) if all_lowers else min(all_averages)
    tot_max = max(all_highers) if all_highers else max(all_averages)
    print("{:<32} {:>8} {:>10.1f} {:>10} {:>10} {:>9.1f} {:>9.1f}".format(
        "Total / Overall", tot_n, tot_mean, "---", "---", tot_min, tot_max
    ))
    print("=" * 86)
    print()


def reproduce_table_2(benchtop_csv_path):
    print("=" * 95)
    print("TABLE 2: Controlled Benchtop Photometric Measurements Across Parameters (n = 12)")
    print("=" * 95)
    
    header_fmt = "{:<4} {:<38} {:>9} {:>9} {:<7} {:>8} {:>8} {:>8}"
    row_fmt    = "{:<4} {:<38} {:>9} {:>9} {:<7} {:>8.1f} {:>8.1f} {:>8.1f}"

    print(header_fmt.format("ID", "Configuration / Parameter Tested", "Standoff", "Tilt(deg)", "Color", "Min(lx)", "Mean(lx)", "Peak(lx)"))
    print("-" * 95)

    last_group = None
    with open(benchtop_csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            grp = row['experiment_group']
            if grp != last_group:
                print(f"[{grp}]")
                last_group = grp
                
            eid   = row['experiment_id']
            cfg   = row['configuration_tested']
            dist  = f"{row['standoff_distance_inch']} in"
            tilt  = f"{row['tilt_angle_deg']} deg" if row['tilt_angle_deg'] != 'N/A' else '---'
            color = row['light_color']
            min_v = float(row['illuminance_min_lx'])
            avg_v = float(row['illuminance_mean_lx'])
            max_v = float(row['illuminance_peak_lx'])
            print(row_fmt.format(eid, cfg, dist, tilt, color, min_v, avg_v, max_v))

    print("=" * 95)
    print()


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    survey_csv = os.path.join(base_dir, 'data', 'dhaka_photometric_survey.csv')
    benchtop_csv = os.path.join(base_dir, 'data', 'benchtop_experiments.csv')
    
    if not os.path.exists(survey_csv) or not os.path.exists(benchtop_csv):
        print("CSV files not found. Running export_datasets.py first...")
        from export_datasets import export_photometric_survey, export_benchtop_experiments
        import openpyxl
        raw_excel = os.path.join(base_dir, 'Documents', 'Database (Light Pollution).xlsx')
        if not os.path.exists(raw_excel):
            raw_excel = os.path.join(base_dir, 'data', 'raw', 'Database (Light Pollution).xlsx')
        wb = openpyxl.load_workbook(raw_excel, data_only=True)
        export_photometric_survey(wb, survey_csv)
        export_benchtop_experiments(wb, benchtop_csv)

    reproduce_table_1(survey_csv)
    reproduce_table_2(benchtop_csv)

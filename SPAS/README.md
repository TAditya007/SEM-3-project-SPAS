# Smart Parking Allocation System (SPAS)

A Python-based academic project that allocates vehicles to suitable parking slots using constraint-based reasoning and utility-based decision making.

## Project Overview

The Smart Parking Allocation System (SPAS) is designed to simulate intelligent parking allocation for different types of vehicles under realistic constraints. The system checks whether a vehicle can be assigned to a slot based on size compatibility, VIP reservation rules, electric charging needs, and slot availability. When multiple valid slots are possible, the system evaluates them using a utility score to select the most suitable assignment.

This project is structured for academic demonstration and report submission. It produces organized outputs including case-wise text results, case-wise CSV comparison files, utility charts, and a final summary report.

## Objectives

- Model vehicles and parking slots using Python classes.
- Apply constraint satisfaction logic for valid slot assignment.
- Use utility-based scoring to improve decision quality.
- Evaluate the system using multiple academic test cases.
- Generate clear output files for submission, screenshots, and viva explanation.

## Features

- Modular Python implementation.
- Multi-case testing support.
- Constraint-based parking allocation.
- Utility-based decision scoring.
- CSV output generation.
- Result visualization using charts.
- Final summary generation for evaluator review.

## Technologies Used

- Python 3.x
- CSV module
- Matplotlib
- Object-Oriented Programming (OOP)
- Constraint-based reasoning

## Project Structure

```text
SPAS/
├── data/
│   └── test_cases.py
├── modules/
│   ├── parking.py
│   ├── vehicle.py
│   ├── slot.py
│   ├── constraints.py
│   ├── solver.py
│   ├── decision.py
│   ├── visualization.py
│   └── summary.py
├── output/
│   ├── charts/
│   ├── comparisons/
│   ├── final/
│   └── results/
├── main.py
├── pipeline.py
└── README.md
```

## Working Principle

1. Vehicles and parking slots are loaded from predefined test cases.
2. The system validates assignments using parking constraints.
3. The solver allocates feasible slots to vehicles.
4. Utility is calculated for assigned slots.
5. Case-wise results are saved as text and CSV files.
6. Charts are generated for utility and final comparison.
7. A final summary file is generated for all test cases.

## Constraints Considered

- Vehicle size must match slot size.
- Reserved slots are prioritized for VIP vehicles.
- Electric vehicles require charger-supported slots when needed.
- Slots cannot be assigned to multiple vehicles at the same time.
- Unavailable or invalid slots are rejected.

## Utility-Based Decision Logic

The system improves allocation quality using a utility function. A higher utility score indicates a more suitable assignment. The utility score may consider:

- Distance of slot from entry or preferred area.
- Vehicle priority.
- Charger availability for EVs.
- Suitability of special slot requirements.

## Test Cases

The project includes multiple academic test scenarios:

- `case1_normal` — standard parking allocation.
- `case2_vip_priority` — VIP-focused parking behavior.
- `case3_ev_charging` — electric vehicle charging allocation.
- `case4_no_slot` — failure case when valid slots are not available.
- `case5_mixed_complex` — mixed-constraint scenario for stronger evaluation.

## Output Files Generated

After running the project, the system generates:

### Case-wise outputs

- `output/results/results_case*.txt`
- `output/comparisons/comparison_case*.csv`
- `output/charts/utility_chart_case*.png`

### Final outputs

- `output/final/final_summary.csv`
- `output/final/final_results.txt`
- `output/charts/allocation_rate_comparison.png`
- `output/charts/average_utility_comparison.png`
- `output/charts/allocation_outcome_comparison.png`

## How to Run

1. Open the project folder in VS Code or terminal.
2. Activate the virtual environment if created.
3. Run the main file:

```bash
python main.py
```

 Check the `output/` folder for generated files.

## Expected Academic Outcomes

This project demonstrates:

- problem representation,
- constraint satisfaction,
- algorithmic decision-making,
- utility-based optimization,
- multi-case testing,
- structured result presentation.

## Conclusion

SPAS is a clean academic implementation of intelligent parking allocation. It combines modular Python design, realistic parking constraints, utility-based reasoning, and organized output generation to create a submission-ready project for demonstration and evaluation

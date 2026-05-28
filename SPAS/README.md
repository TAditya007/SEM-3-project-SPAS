# Smart Parking Allocation System (SPAS)

A Python-based academic project that allocates vehicles to suitable parking slots using constraint-based reasoning and utility-based decision making for final CFAI Term 3 submission.

## Live Links

- GitHub Repository: [SEM-3-project-SPAS](https://github.com/TAditya007/SEM-3-project-SPAS)
- GitHub Pages Demo: [SPAS Project Showcase](https://taditya007.github.io/SEM-3-project-SPAS/)
- Project README: [README.md](https://github.com/TAditya007/SEM-3-project-SPAS/blob/main/SPAS/README.md)

## Project Overview

The Smart Parking Allocation System (SPAS) simulates intelligent parking allocation for different types of vehicles under realistic parking constraints. The system checks whether a vehicle can be assigned to a slot based on size compatibility, VIP reservation rules, electric charging requirements, and slot availability, and then uses utility-based scoring to select the most suitable valid slot [file:3].

This project is organized as a modular Python system for academic demonstration and submission. It generates case-wise text outputs, comparison CSV files, utility charts, and final summary files through the project pipeline itself, supporting explainable and structured academic evaluation [file:1].

## Project Objectives

- Model vehicles and parking slots using Python dataclasses and modular files .
- Apply constraint satisfaction logic for valid slot assignment.
- Use utility-based scoring to improve decision quality.
- Evaluate the system using multiple academic test cases and output files.
- Produce clean outputs for submission, screenshots, viva explanation, and evaluator review .

## CO Mapping

| CO | Academic expectation | SPAS implementation status |
| --- | --- | --- |
| CO1 | Problem formulation, representation, PEAS, constraints, Python data structures | **Implemented** through vehicle/slot modeling, parking rules, modular Python classes, and structured test cases |
| CO2 | Search algorithms, heuristics, empirical profiling | **Partially demonstrated** through structured candidate evaluation and multi-case analysis; can be strengthened further with explicit search-comparison metrics |
| CO3 | CSP modeling, backtracking/constraint reasoning, explainability | **Implemented** through rule-based allocation constraints and valid-slot filtering for parking assignment |
| CO4 | Utility-based decision making, bounded selection logic | **Implemented** through utility scoring based on priority, distance, VIP preference, and EV charging preference |
| CO5 | Reasoning under uncertainty, probabilistic update | **Partially supported** in project architecture and extendable for uncertain slot availability; visible probabilistic module can further strengthen submission |
| CO6 | Integrated AI pipeline with explainable outputs | **Implemented** through `main.py`, `pipeline.py`, case-wise outputs, charts, final summaries, and integrated project workflow |

## Features

- Modular Python implementation
- Constraint-based parking allocation
- Utility-based slot selection
- Multi-case testing support
- Text and CSV result generation
- Utility chart generation
- Final summary generation
- GitHub Pages academic showcase
- Submission-ready project structure

## Technologies Used

- Python 3.x
- Matplotlib
- CSV module
- Object-Oriented Programming (OOP)
- Constraint-based reasoning
- Utility-based decision making
- Git and GitHub
- GitHub Pages for static showcase deployment

## Project Structure

```text
software/
├── index.html
├── assets/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
└── SPAS/
    ├── README.md
    ├── main.py
    ├── pipeline.py
    ├── requirements.txt
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
    └── output/
        ├── charts/
        ├── comparisons/
        ├── final/
        └── results/
```

## Working Principle

1. Vehicles and parking slots are loaded from predefined academic test cases or a custom case input.
2. The system checks slot feasibility using parking constraints such as size, reservation, charger support, and availability.
3. Valid slots are considered for each vehicle.
4. Utility is calculated to rank feasible assignments.
5. The best valid slot is selected for each vehicle.
6. Case-wise outputs are saved as text, CSV, and charts.
7. Final summary files are generated across all cases for academic review .

## Constraints Considered

- Vehicle size must fit slot size.
- Reserved slots are allowed only for eligible VIP vehicles.
- Electric vehicles should be assigned charger-supported slots when required.
- A slot cannot be assigned to multiple vehicles simultaneously.
- Unavailable slots are rejected before allocation.

## Utility Logic

The project uses a simple utility function to rank valid parking slots after constraint checking. The score currently combines vehicle priority, slot distance, VIP-reserved compatibility, and EV-charger compatibility to improve the quality of final allocation decisions .

## Test Cases

The project includes multiple academic test scenarios for evaluation and demonstration:

- `case1_normal` - Standard parking allocation
- `case2_vip_priority` - VIP-focused parking behavior
- `case3_ev_charging` - Electric vehicle charging allocation
- `case4_no_slot` - Failure case when valid slots are not available
- `case5_mixed_complex` - Mixed-constraint scenario for stronger evaluation

## Output Files Generated

After running the project, the system generates structured outputs through its own pipeline for academic review and final submission.

### Case-wise outputs

- `output/results/results_case*.txt`
- `output/comparisons/comparison_case*.csv`
- `output/charts/utility_chart_case*.png`

### Final outputs

- `output/final/final_summary.csv`
- `output/final/final_results.txt`
- Final comparison charts in `output/charts/`

## How to Run

1. Open the project folder in VS Code or terminal.
2. Change into the SPAS project directory if needed.
3. Activate the virtual environment if created.
4. Run:

```bash
python main.py
```

1. Check the `output/` folder for generated files.

## Academic Notes

This project is strongest in problem representation, parking constraint validation, utility-based decision support, modular implementation, and structured output generation. Based on the current handout expectations, CO2 and CO5 can be strengthened further by adding explicit search-comparison metrics and a lightweight uncertainty reasoning module, while the present version already serves as a solid and submission-ready SPAS academic prototype.

## Deployment

The project includes a GitHub Pages showcase page for academic presentation and quick online review:

- Live Demo: [SPAS Project Showcase](https://taditya007.github.io/SEM-3-project-SPAS/)
- Repository: [SEM-3-project-SPAS](https://github.com/TAditya007/SEM-3-project-SPAS)

This deployment is a static project showcase page and does not replace the Python execution pipeline. Final outputs are generated by running the project through `main.py`, ensuring the academic evidence comes from the project itself [cite:17].

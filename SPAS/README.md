# Smart Parking Allocation System (SPAS)

A Python-based academic project that allocates vehicles to suitable parking slots using constraint-based reasoning and utility-based decision making.

## Live Links

- GitHub Repository: [SEM-3-project-SPAS](https://github.com/TAditya007/SEM-3-project-SPAS)
- GitHub Pages Demo: [SPAS Project Showcase](https://taditya007.github.io/SEM-3-project-SPAS/)
- Project README: [README.md](https://github.com/TAditya007/SEM-3-project-SPAS/blob/main/SPAS/README.md) 

## Project Overview

The Smart Parking Allocation System (SPAS) is designed to simulate intelligent parking allocation for different types of vehicles under realistic constraints. The system checks whether a vehicle can be assigned to a slot based on size compatibility, VIP reservation rules, electric charging needs, and slot availability. When multiple valid slots are possible, the system evaluates them using a utility score to select the most suitable assignment.

This project is structured for academic demonstration and submission. The implementation follows a modular Python design and generates organized outputs such as case-wise text results, comparison CSV files, utility charts, and final summary files through the project pipeline itself.

## Project Objectives

- Model vehicles and parking slots using Python classes.
- Apply constraint satisfaction logic for valid slot assignment.
- Use utility-based scoring to improve decision quality.
- Evaluate the system using multiple academic test cases.
- Generate clear output files for submission, screenshots, viva explanation, and evaluator review.

## Academic CO / Module Coverage

| Module / CO Area | Academic Expectation | SPAS Coverage |
| --- | --- | --- |
| Problem formulation and representation | Represent entities, rules, state, and goal clearly | Vehicles, parking slots, constraints, and allocation objective are modeled in a structured way. |
| Search / algorithmic reasoning | Evaluate solution paths or options systematically | The project follows a structured allocation flow and case-wise evaluation process. |
| CSP allocation | Enforce constraints and valid assignments | Slot feasibility is checked through rule-based parking constraints. |
| Decision making | Choose the best result using utility or scoring | Utility-based scoring ranks feasible slots and selects the best assignment. |
| Reasoning under uncertainty | Consider uncertain or dynamic conditions | The architecture is extendable toward uncertain parking conditions and adaptive logic. |
| Integrated AI pipeline | Combine all modules into one complete system | `main.py` and `pipeline.py` coordinate testing, allocation, outputs, summaries, and charts. |

## Features

- Modular Python implementation
- Multi-case testing support
- Constraint-based parking allocation
- Utility-based decision scoring
- CSV output generation
- Result visualization using charts
- Final summary generation for evaluator review
- GitHub Pages project showcase for online presentation

## Technologies Used

- Python 3.x
- CSV module
- Matplotlib
- Object-Oriented Programming (OOP)
- Constraint-based reasoning
- Git and GitHub
- GitHub Pages for static deployment

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

1. Vehicles and parking slots are loaded from predefined test cases.
2. The system validates assignments using parking constraints.
3. The solver allocates feasible slots to vehicles.
4. Utility is calculated for assigned slots.
5. Case-wise results are saved as text and CSV files.
6. Charts are generated for utility and final comparison.
7. Final summary files are generated for all test cases.

## Constraints Considered

- Vehicle size must match slot size
- Reserved slots are prioritized for VIP vehicles
- Electric vehicles require charger-supported slots when needed
- Slots cannot be assigned to multiple vehicles at the same time
- Unavailable or invalid slots are rejected

## Utility-Based Decision Logic

The system improves allocation quality using a utility function. A higher utility score indicates a more suitable assignment. The utility evaluation may consider parking suitability, vehicle priority, EV charging support, and preference-oriented conditions to select the best valid slot.

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
- `output/charts/allocation_rate_comparison.png`
- `output/charts/average_utility_comparison.png`
- `output/charts/allocation_outcome_comparison.png`

## How to Run

1. Open the project folder in VS Code or terminal.
2. Change into the SPAS project directory if needed.
3. Activate the virtual environment if created.
4. Run the main file:

```bash
python main.py
```

Check the `output/` folder for generated files.

## Expected Academic Outcomes

This project demonstrates:

- Problem representation
- Constraint satisfaction
- Algorithmic decision-making
- Utility-based optimization
- Multi-case testing
- Structured result presentation

## Deployment

The project also includes a GitHub Pages showcase page for academic presentation and quick online review:

- Live Demo: [https://taditya007.github.io/SEM-3-project-SPAS/](https://taditya007.github.io/SEM-3-project-SPAS/)
- Repository: [https://github.com/TAditya007/SEM-3-project-SPAS](https://github.com/TAditya007/SEM-3-project-SPAS)

This deployment is a static academic showcase page and does not replace the Python execution pipeline. The actual outputs must still be generated by running the project through `main.py`.

## Conclusion

SPAS is a clean academic implementation of intelligent parking allocation. It combines modular Python design, realistic parking constraints, utility-based reasoning, organized output generation, and a public project showcase page to create a submission-ready system for demonstration and evaluation.

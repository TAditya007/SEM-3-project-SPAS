import csv
import os


def calculate_case_summary(case_name, vehicles, assignment, slot_map, calculate_utility):
    total_vehicles = len(vehicles)
    allocated_vehicles = 0
    unallocated_vehicles = 0
    utility_values = []

    for vehicle in vehicles:
        slot_id = assignment.get(vehicle.vehicle_id)

        if slot_id:
            allocated_vehicles += 1
            slot = slot_map[slot_id]
            utility = calculate_utility(vehicle, slot)
            utility_values.append(utility)
        else:
            unallocated_vehicles += 1

    average_utility = round(sum(utility_values) / len(utility_values), 2) if utility_values else 0
    highest_utility = max(utility_values) if utility_values else 0
    allocation_rate = round((allocated_vehicles / total_vehicles) * 100, 2) if total_vehicles else 0

    return {
        "Case Name": case_name,
        "Total Vehicles": total_vehicles,
        "Allocated Vehicles": allocated_vehicles,
        "Unallocated Vehicles": unallocated_vehicles,
        "Allocation Rate (%)": allocation_rate,
        "Average Utility": average_utility,
        "Highest Utility": highest_utility,
    }


def save_final_summary(summary_rows, output_file="output/final/final_summary.csv"):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[
            "Case Name",
            "Total Vehicles",
            "Allocated Vehicles",
            "Unallocated Vehicles",
            "Allocation Rate (%)",
            "Average Utility",
            "Highest Utility",
        ])
        writer.writeheader()
        writer.writerows(summary_rows)


def save_final_results(summary_rows, output_file="output/final/final_results.txt"):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    best_allocation_case = max(summary_rows, key=lambda x: x["Allocation Rate (%)"])
    best_utility_case = max(summary_rows, key=lambda x: x["Highest Utility"])
    most_constrained_case = max(summary_rows, key=lambda x: x["Unallocated Vehicles"])

    lines = []
    lines.append("SMART PARKING ALLOCATION SYSTEM (SPAS)")
    lines.append("Polished Final Output Notes")
    lines.append("=" * 40)
    lines.append("")
    lines.append("Submission status")
    lines.append("-" * 20)
    lines.append("This project is in a submission-ready academic state.")
    lines.append("The output package is organized to help evaluators verify correctness,")
    lines.append("constraints, utility-based decision logic, and multi-case testing quality.")
    lines.append("")
    lines.append("CO coverage summary")
    lines.append("-" * 20)
    lines.append("CO1 - Problem representation: Covered using modular Python classes for vehicles, slots, and parking system entities.")
    lines.append("CO2 - Constraint satisfaction: Covered through valid slot allocation under size, reservation, EV, and availability rules.")
    lines.append("CO3 - Algorithmic reasoning: Covered through the solver workflow that produces valid or failure-aware allocations.")
    lines.append("CO4 - Decision support: Covered through utility-based scoring for assigned slots.")
    lines.append("CO5 - Testing and analysis: Covered through multiple academic test cases and cross-case comparison.")
    lines.append("CO6 - Result presentation: Covered through readable TXT outputs, final CSV summaries, and polished charts.")
    lines.append("")
    lines.append("Evaluator highlights")
    lines.append("-" * 20)
    lines.append(f"Best allocation rate case: {best_allocation_case['Case Name']}")
    lines.append(f"Highest observed utility case: {best_utility_case['Case Name']}")
    lines.append(f"Most constrained case: {most_constrained_case['Case Name']}")
    lines.append("")
    lines.append("Recommended final showcase set")
    lines.append("-" * 20)
    lines.append("1. final_results.txt")
    lines.append("2. final_summary.csv")
    lines.append("3. allocation_rate_comparison.png")
    lines.append("4. average_utility_comparison.png")
    lines.append("5. allocation_outcome_comparison.png")
    lines.append("")
    lines.append("Short viva line")
    lines.append("-" * 20)
    lines.append("The SPAS project models vehicles and slots in Python, applies CSP-style parking constraints,")
    lines.append("ranks valid assignments using utility scoring, and compares multiple test cases using")
    lines.append("structured output files and charts.")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
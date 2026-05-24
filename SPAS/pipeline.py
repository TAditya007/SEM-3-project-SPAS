from modules.parking import ParkingSystem
from modules.solver import ParkingSolver
from modules.decision import calculate_utility
from modules.visualization import plot_utility_scores, plot_final_comparison_charts
from modules.summary import calculate_case_summary, save_final_summary, save_final_results
from data.test_cases import TEST_CASES
import csv
import os


def run_pipeline(case_name="case1_normal"):
    if case_name not in TEST_CASES:
        raise ValueError(f"Test case '{case_name}' not found. Available cases: {list(TEST_CASES.keys())}")

    test_case = TEST_CASES[case_name]
    vehicles = test_case["vehicles"]
    slots = test_case["slots"]

    os.makedirs("output/results", exist_ok=True)
    os.makedirs("output/comparisons", exist_ok=True)
    os.makedirs("output/charts", exist_ok=True)
    os.makedirs("output/final", exist_ok=True)

    parking_system = ParkingSystem(vehicles, slots)
    solver = ParkingSolver(parking_system.vehicles, parking_system.slots)
    assignment = solver.solve()

    slot_map = {slot.slot_id: slot for slot in slots}
    lines = []
    lines.append(f"Parking Allocation Result - {case_name}")
    lines.append("-" * 120)

    vehicle_ids = []
    utility_scores = []

    for vehicle in vehicles:
        slot_id = assignment.get(vehicle.vehicle_id)

        vip_text = "VIP" if vehicle.is_vip else "Regular"
        ev_text = "Electric" if vehicle.is_electric else "Non-Electric"

        if slot_id:
            slot = slot_map[slot_id]
            reserved_text = "Reserved" if slot.is_reserved else "General"
            charger_text = "Charger" if slot.has_charger else "No-Charger"
            utility = calculate_utility(vehicle, slot)

            vehicle_ids.append(vehicle.vehicle_id)
            utility_scores.append(utility)

            line = (
                f"Vehicle {vehicle.vehicle_id} ({vehicle.vehicle_type}, {vehicle.size}, {vip_text}, {ev_text}, priority={vehicle.priority}) "
                f"-> Slot {slot.slot_id} ({slot.size}, {reserved_text}, {charger_text}, distance={slot.distance}, utility={utility})"
            )
        else:
            line = (
                f"Vehicle {vehicle.vehicle_id} ({vehicle.vehicle_type}, {vehicle.size}, {vip_text}, {ev_text}, priority={vehicle.priority}) "
                f"-> No slot available"
            )

        print(line)
        lines.append(line)

    results_file = f"output/results/results_{case_name}.txt"
    csv_file = f"output/comparisons/comparison_{case_name}.csv"
    chart_file = f"output/charts/utility_chart_{case_name}.png"

    with open(results_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "Vehicle ID",
            "Vehicle Type",
            "Size",
            "VIP Status",
            "Electric Status",
            "Priority",
            "Assigned Slot",
            "Slot Size",
            "Reserved",
            "Charger",
            "Distance",
            "Utility"
        ])

        for vehicle in vehicles:
            slot_id = assignment.get(vehicle.vehicle_id)

            if slot_id:
                slot = slot_map[slot_id]
                utility = calculate_utility(vehicle, slot)
                writer.writerow([
                    vehicle.vehicle_id,
                    vehicle.vehicle_type,
                    vehicle.size,
                    "VIP" if vehicle.is_vip else "Regular",
                    "Electric" if vehicle.is_electric else "Non-Electric",
                    vehicle.priority,
                    slot.slot_id,
                    slot.size,
                    "Yes" if slot.is_reserved else "No",
                    "Yes" if slot.has_charger else "No",
                    slot.distance,
                    utility
                ])
            else:
                writer.writerow([
                    vehicle.vehicle_id,
                    vehicle.vehicle_type,
                    vehicle.size,
                    "VIP" if vehicle.is_vip else "Regular",
                    "Electric" if vehicle.is_electric else "Non-Electric",
                    vehicle.priority,
                    "No slot available",
                    "-",
                    "-",
                    "-",
                    "-",
                    "-"
                ])

    plot_utility_scores(vehicle_ids, utility_scores, chart_file)

    summary_row = calculate_case_summary(case_name, vehicles, assignment, slot_map, calculate_utility)

    print(f"\nUtility chart saved to {chart_file}")
    print(f"Results saved to {results_file}")
    print(f"Comparison saved to {csv_file}")

    return summary_row


def run_all_cases():
    all_summaries = []

    for case_name in TEST_CASES.keys():
        print(f"\n{'=' * 30} Running {case_name} {'=' * 30}")
        summary = run_pipeline(case_name)
        all_summaries.append(summary)

    save_final_summary(all_summaries, "output/final/final_summary.csv")
    save_final_results(all_summaries, "output/final/final_results.txt")
    plot_final_comparison_charts(all_summaries, "output/charts")

    print("\nFinal summary saved to output/final/final_summary.csv")
    print("Final results saved to output/final/final_results.txt")
    print("Final comparison charts saved to output/charts/")
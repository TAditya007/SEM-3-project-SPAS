from modules.parking import ParkingSystem
from modules.solver import ParkingSolver
from modules.decision import calculate_utility
from modules.visualization import plot_utility_scores, plot_final_comparison_charts
from modules.summary import calculate_case_summary, save_final_summary, save_final_results
from data.test_cases import TEST_CASES
import csv
import os


def ensure_output_folders():
    os.makedirs("output/results", exist_ok=True)
    os.makedirs("output/comparisons", exist_ok=True)
    os.makedirs("output/charts", exist_ok=True)
    os.makedirs("output/final", exist_ok=True)
    os.makedirs("output/traces", exist_ok=True)


def build_case_data(case_name=None, custom_case=None):
    if custom_case is not None:
        return "custom_case", custom_case["vehicles"], custom_case["slots"]

    if case_name not in TEST_CASES:
        raise ValueError(
            f"Test case '{case_name}' not found. Available cases: {list(TEST_CASES.keys())}"
        )

    test_case = TEST_CASES[case_name]
    return case_name, test_case["vehicles"], test_case["slots"]


def generate_reasoning_trace(case_name, vehicles, assignment, slot_map):
    trace_lines = []
    trace_lines.append(f"Reasoning Trace - {case_name}")
    trace_lines.append("=" * 100)
    trace_lines.append("Step 1: Input vehicles and parking slots loaded.")
    trace_lines.append("Step 2: Parking system initialized.")
    trace_lines.append("Step 3: Solver applied CSP-style allocation logic.")
    trace_lines.append("Step 4: Valid assignments checked against parking constraints.")
    trace_lines.append("Step 5: Utility scores computed for assigned slots.")
    trace_lines.append("Step 6: Final allocation decisions recorded.")
    trace_lines.append("-" * 100)

    for vehicle in vehicles:
        slot_id = assignment.get(vehicle.vehicle_id)
        if slot_id:
            slot = slot_map[slot_id]
            utility = calculate_utility(vehicle, slot)
            trace_lines.append(
                f"Vehicle {vehicle.vehicle_id} assigned to Slot {slot.slot_id} "
                f"after satisfying size/priority/feature constraints with utility score {utility}."
            )
        else:
            trace_lines.append(
                f"Vehicle {vehicle.vehicle_id} was not assigned because no valid slot satisfied all constraints."
            )

    return trace_lines


def save_case_outputs(case_name, vehicles, slots, assignment):
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
    trace_file = f"output/traces/trace_{case_name}.txt"

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

    trace_lines = generate_reasoning_trace(case_name, vehicles, assignment, slot_map)
    with open(trace_file, "w", encoding="utf-8") as f:
        f.write("\n".join(trace_lines))

    summary_row = calculate_case_summary(case_name, vehicles, assignment, slot_map, calculate_utility)

    print(f"\nUtility chart saved to {chart_file}")
    print(f"Results saved to {results_file}")
    print(f"Comparison saved to {csv_file}")
    print(f"Reasoning trace saved to {trace_file}")

    return summary_row


def run_pipeline(case_name="case1_normal", custom_case=None):
    ensure_output_folders()

    resolved_case_name, vehicles, slots = build_case_data(case_name, custom_case)

    parking_system = ParkingSystem(vehicles, slots)
    solver = ParkingSolver(parking_system.vehicles, parking_system.slots)
    assignment = solver.solve()

    summary_row = save_case_outputs(resolved_case_name, vehicles, slots, assignment)
    return summary_row


def run_all_cases():
    all_summaries = []

    for case_name in TEST_CASES.keys():
        print(f"\n{'=' * 30} Running {case_name} {'=' * 30}")
        summary = run_pipeline(case_name=case_name)
        all_summaries.append(summary)

    save_final_summary(all_summaries, "output/final/final_summary.csv")
    save_final_results(all_summaries, "output/final/final_results.txt")
    plot_final_comparison_charts(all_summaries, "output/charts")

    print("\nFinal summary saved to output/final/final_summary.csv")
    print("Final results saved to output/final/final_results.txt")
    print("Final comparison charts saved to output/charts/")


def run_custom_case(custom_case):
    print(f"\n{'=' * 30} Running custom_case {'=' * 30}")
    summary = run_pipeline(custom_case=custom_case)
    return summary


def generate_final_outputs():
    print("\nGenerating complete final output package...")
    run_all_cases()
    print("All final outputs generated successfully.")
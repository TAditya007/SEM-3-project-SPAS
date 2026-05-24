import os
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt


def plot_utility_scores(vehicle_ids, utility_scores, output_file="output/charts/utility_chart.png"):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    plt.figure(figsize=(9, 5.5))
    bars = plt.bar(vehicle_ids, utility_scores, color="#4C78A8", edgecolor="black")

    plt.xlabel("Vehicle ID")
    plt.ylabel("Utility Score")
    plt.title("Parking Allocation Utility Scores")
    plt.grid(axis="y", linestyle="--", alpha=0.3)

    for bar, score in zip(bars, utility_scores):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            str(score),
            ha="center",
            va="bottom",
            fontsize=9
        )

    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    plt.close()


def plot_final_comparison_charts(summary_rows, output_dir="output/charts"):
    os.makedirs(output_dir, exist_ok=True)

    case_names = [row["Case Name"] for row in summary_rows]
    allocation_rates = [row["Allocation Rate (%)"] for row in summary_rows]
    avg_utilities = [row["Average Utility"] for row in summary_rows]
    allocated = [row["Allocated Vehicles"] for row in summary_rows]
    unallocated = [row["Unallocated Vehicles"] for row in summary_rows]

    short_case_names = [name.replace("case1_", "").replace("case2_", "").replace("case3_", "").replace("case4_", "").replace("case5_", "").replace("_", " ").title() for name in case_names]

    # Allocation rate chart
    plt.figure(figsize=(10, 5.5))
    bars = plt.bar(short_case_names, allocation_rates, color="#2F6B8A", edgecolor="black")
    plt.xlabel("Test Case")
    plt.ylabel("Allocation Rate (%)")
    plt.title("Allocation Rate by Test Case")
    plt.ylim(0, 110)
    plt.grid(axis="y", linestyle="--", alpha=0.3)
    for bar, value in zip(bars, allocation_rates):
        plt.text(bar.get_x() + bar.get_width() / 2, value + 1, f"{value:.2f}%", ha="center", va="bottom", fontsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "allocation_rate_comparison.png"), dpi=300, bbox_inches="tight")
    plt.close()

    # Average utility chart
    plt.figure(figsize=(10, 5.5))
    bars = plt.bar(short_case_names, avg_utilities, color="#4C78A8", edgecolor="black")
    plt.xlabel("Test Case")
    plt.ylabel("Average Utility")
    plt.title("Average Utility by Test Case")
    plt.grid(axis="y", linestyle="--", alpha=0.3)
    for bar, value in zip(bars, avg_utilities):
        plt.text(bar.get_x() + bar.get_width() / 2, value + 0.6, f"{value:.2f}", ha="center", va="bottom", fontsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "average_utility_comparison.png"), dpi=300, bbox_inches="tight")
    plt.close()

    # Allocation outcome chart
    x = range(len(short_case_names))
    width = 0.35

    plt.figure(figsize=(10, 5.5))
    bars1 = plt.bar([i - width / 2 for i in x], allocated, width=width, label="Allocated", color="#4C9F70", edgecolor="black")
    bars2 = plt.bar([i + width / 2 for i in x], unallocated, width=width, label="Unallocated", color="#D46A6A", edgecolor="black")

    plt.xlabel("Test Case")
    plt.ylabel("Number of Vehicles")
    plt.title("Allocation Outcome by Test Case")
    plt.xticks(list(x), short_case_names)
    plt.grid(axis="y", linestyle="--", alpha=0.3)
    plt.legend()

    for bar in bars1:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05, str(int(bar.get_height())), ha="center", va="bottom", fontsize=9)
    for bar in bars2:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05, str(int(bar.get_height())), ha="center", va="bottom", fontsize=9)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "allocation_outcome_comparison.png"), dpi=300, bbox_inches="tight")
    plt.close()
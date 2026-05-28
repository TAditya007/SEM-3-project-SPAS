from pipeline import run_all_cases, run_custom_case, generate_final_outputs
from modules.vehicle import Vehicle
from modules.slot import Slot


def show_menu():
    print("\nSMART PARKING ALLOCATION SYSTEM (SPAS)")
    print("1. Run all predefined validation cases")
    print("2. Run one custom parking allocation case")
    print("3. Generate final polished outputs")
    print("4. Exit")


def get_yes_no(prompt):
    value = input(prompt).strip().lower()
    return value in ["yes", "y", "true", "1"]


def get_custom_vehicle():
    print("\nEnter custom vehicle details:")
    vehicle_id = input("Vehicle ID: ").strip()
    vehicle_type = input("Vehicle Type: ").strip()
    size = input("Vehicle Size (small/medium/large): ").strip().lower()
    priority = int(input("Priority (1-5): ").strip())
    is_vip = get_yes_no("Is VIP? (yes/no): ")
    is_electric = get_yes_no("Is Electric? (yes/no): ")

    return Vehicle(
        vehicle_id=vehicle_id,
        vehicle_type=vehicle_type,
        size=size,
        priority=priority,
        is_vip=is_vip,
        is_electric=is_electric
    )


def get_custom_slots():
    slots = []
    num_slots = int(input("\nHow many parking slots do you want to enter? ").strip())

    for i in range(num_slots):
        print(f"\nEnter details for Slot {i + 1}:")
        slot_id = input("Slot ID: ").strip()
        size = input("Slot Size (small/medium/large): ").strip().lower()
        distance = float(input("Distance from entrance: ").strip())
        is_available = get_yes_no("Is Available? (yes/no): ")
        is_reserved = get_yes_no("Is Reserved? (yes/no): ")
        has_charger = get_yes_no("Has Charger? (yes/no): ")

        slot = Slot(
            slot_id=slot_id,
            size=size,
            distance=distance,
            is_available=is_available,
            is_reserved=is_reserved,
            has_charger=has_charger
        )
        slots.append(slot)

    return slots


def build_custom_case():
    vehicle = get_custom_vehicle()
    slots = get_custom_slots()
    return {
        "vehicles": [vehicle],
        "slots": slots
    }


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\nRunning predefined validation cases...")
            run_all_cases()
            print("Completed predefined case execution.")

        elif choice == "2":
            custom_case = build_custom_case()
            print("\nRunning custom parking allocation case...")
            run_custom_case(custom_case)
            print("Custom case completed.")

        elif choice == "3":
            print("\nGenerating final polished outputs...")
            generate_final_outputs()
            print("Final outputs generated successfully.")

        elif choice == "4":
            print("Exiting SPAS.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
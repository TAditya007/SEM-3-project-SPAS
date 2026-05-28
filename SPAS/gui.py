import tkinter as tk
from tkinter import ttk, messagebox

from modules.vehicle import Vehicle
from modules.slot import Slot
from modules.constraints import valid_allocation


SMALL_TYPES = [
    "Microcars",
    "City cars",
    "Hatchbacks",
    "Compact sedans",
    "Subcompact SUVs",
    "Coupes",
    "Roadsters"
]

MEDIUM_TYPES = [
    "Midsize sedans",
    "Station wagons",
    "Crossovers",
    "Compact SUVs",
    "Sports cars",
    "Muscle cars",
    "Convertibles"
]

LARGE_TYPES = [
    "Full-size sedans",
    "Minivans",
    "Full-size SUVs",
    "Luxury SUVs",
    "Pickup trucks",
    "Grand tourers",
    "Vans"
]

ALL_VEHICLE_TYPES = SMALL_TYPES + MEDIUM_TYPES + LARGE_TYPES


def get_size_from_vehicle_type(vehicle_type):
    if vehicle_type in SMALL_TYPES:
        return "small"
    if vehicle_type in MEDIUM_TYPES:
        return "medium"
    return "large"


def create_predefined_slots():
    slots = []

    for i in range(1, 101):
        slots.append(
            Slot(
                slot_id=f"A{i}",
                size="large",
                distance=5 + (i * 0.1),
                is_available=True,
                is_reserved=True,
                has_charger=False
            )
        )

    for i in range(1, 201):
        slots.append(
            Slot(
                slot_id=f"B{i}",
                size="large",
                distance=10 + (i * 0.1),
                is_available=True,
                is_reserved=False,
                has_charger=False
            )
        )

    for i in range(1, 301):
        if i <= 100:
            size = "small"
        elif i <= 200:
            size = "medium"
        else:
            size = "large"

        slots.append(
            Slot(
                slot_id=f"C{i}",
                size=size,
                distance=15 + (i * 0.05),
                is_available=True,
                is_reserved=False,
                has_charger=False
            )
        )

    for i in range(1, 51):
        slots.append(
            Slot(
                slot_id=f"E{i}",
                size="large",
                distance=7 + (i * 0.1),
                is_available=True,
                is_reserved=False,
                has_charger=True
            )
        )

    return slots


def get_selected_category(is_vip, is_reservable, is_ev):
    if is_vip:
        return "VIP"
    if is_reservable:
        return "Reservable"
    if is_ev:
        return "EV"
    return "General"


def get_vehicle_flags(category):
    return {
        "is_vip": category == "VIP",
        "is_electric": category == "EV"
    }


def get_candidate_prefix(category):
    if category == "VIP":
        return "A"
    if category == "Reservable":
        return "B"
    if category == "EV":
        return "E"
    return "C"


def allocate_slot_fifo(vehicle, category, slots):
    prefix = get_candidate_prefix(category)

    for slot in slots:
        if not slot.slot_id.startswith(prefix):
            continue

        if not slot.is_available:
            continue

        if valid_allocation(vehicle, slot):
            slot.is_available = False
            return slot

    return None


class SPASGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Parking Allocation System (SPAS)")
        self.root.geometry("1180x780")
        self.root.configure(bg="#f4f6f8")

        self.slots = create_predefined_slots()
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(
            self.root,
            text="Smart Parking Allocation System",
            font=("Arial", 20, "bold"),
            bg="#f4f6f8",
            fg="#1f3b57"
        )
        title.pack(pady=15)

        subtitle = tk.Label(
            self.root,
            text="Predefined Slot Allocation with FIFO Rule",
            font=("Arial", 11),
            bg="#f4f6f8",
            fg="#444444"
        )
        subtitle.pack(pady=5)

        info_label = tk.Label(
            self.root,
            text="A1-A100 VIP | B1-B200 Reservable | C1-C300 General | E1-E50 EV",
            font=("Arial", 10),
            bg="#f4f6f8",
            fg="#333333"
        )
        info_label.pack(pady=5)

        form_frame = tk.LabelFrame(
            self.root,
            text="Vehicle Entry",
            font=("Arial", 12, "bold"),
            bg="white",
            padx=10,
            pady=10
        )
        form_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(form_frame, text="Vehicle Number", bg="white", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.vehicle_number_entry = tk.Entry(form_frame, width=25)
        self.vehicle_number_entry.grid(row=0, column=1, padx=10, pady=10)
        self.vehicle_number_entry.bind("<KeyRelease>", self.enforce_vehicle_number)

        tk.Label(form_frame, text="Owner Name", bg="white", font=("Arial", 11)).grid(row=0, column=2, padx=10, pady=10, sticky="w")
        self.owner_name_entry = tk.Entry(form_frame, width=25)
        self.owner_name_entry.grid(row=0, column=3, padx=10, pady=10)
        self.owner_name_entry.bind("<KeyRelease>", self.enforce_owner_name)

        tk.Label(form_frame, text="Phone Number", bg="white", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.phone_entry = tk.Entry(form_frame, width=25)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)
        self.phone_entry.bind("<KeyRelease>", self.enforce_phone_number)

        tk.Label(form_frame, text="Vehicle Type", bg="white", font=("Arial", 11)).grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.vehicle_type_var = tk.StringVar(value=ALL_VEHICLE_TYPES[0])
        self.vehicle_type_combo = ttk.Combobox(
            form_frame,
            textvariable=self.vehicle_type_var,
            values=ALL_VEHICLE_TYPES,
            state="readonly",
            width=22
        )
        self.vehicle_type_combo.grid(row=1, column=3, padx=10, pady=10)

        tk.Label(form_frame, text="Special Category", bg="white", font=("Arial", 11)).grid(row=2, column=0, padx=10, pady=10, sticky="w")

        checkbox_frame = tk.Frame(form_frame, bg="white")
        checkbox_frame.grid(row=2, column=1, columnspan=3, padx=10, pady=10, sticky="w")

        self.vip_var = tk.BooleanVar(value=False)
        self.reservable_var = tk.BooleanVar(value=False)
        self.ev_var = tk.BooleanVar(value=False)

        tk.Checkbutton(
            checkbox_frame,
            text="VIP",
            variable=self.vip_var,
            bg="white",
            font=("Arial", 11),
            command=lambda: self.handle_category_selection("VIP")
        ).pack(side="left", padx=10)

        tk.Checkbutton(
            checkbox_frame,
            text="Reservable",
            variable=self.reservable_var,
            bg="white",
            font=("Arial", 11),
            command=lambda: self.handle_category_selection("Reservable")
        ).pack(side="left", padx=10)

        tk.Checkbutton(
            checkbox_frame,
            text="EV",
            variable=self.ev_var,
            bg="white",
            font=("Arial", 11),
            command=lambda: self.handle_category_selection("EV")
        ).pack(side="left", padx=10)

        hint_label = tk.Label(
            form_frame,
            text="Leave all unchecked for GENERAL",
            bg="white",
            fg="#666666",
            font=("Arial", 10, "italic")
        )
        hint_label.grid(row=3, column=0, columnspan=4, padx=10, pady=5, sticky="w")

        button_frame = tk.Frame(self.root, bg="#f4f6f8")
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Assign Slot",
            font=("Arial", 12, "bold"),
            bg="#1f78b4",
            fg="white",
            width=18,
            command=self.assign_slot
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            button_frame,
            text="Clear Form",
            font=("Arial", 12, "bold"),
            bg="#777777",
            fg="white",
            width=14,
            command=self.clear_form
        ).grid(row=0, column=1, padx=10)

        tk.Button(
            button_frame,
            text="Delete Selected Entry",
            font=("Arial", 12, "bold"),
            bg="#c0392b",
            fg="white",
            width=20,
            command=self.delete_selected_entry
        ).grid(row=0, column=2, padx=10)

        list_frame = tk.LabelFrame(
            self.root,
            text="Allocated Vehicles List",
            font=("Arial", 12, "bold"),
            bg="white",
            padx=10,
            pady=10
        )
        list_frame.pack(fill="both", expand=True, padx=20, pady=10)

        columns = (
            "vehicle_number",
            "owner_name",
            "phone_number",
            "vehicle_type",
            "category",
            "assigned_slot",
            "slot_size"
        )

        self.assignment_tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=18)

        self.assignment_tree.heading("vehicle_number", text="Vehicle Number")
        self.assignment_tree.heading("owner_name", text="Owner Name")
        self.assignment_tree.heading("phone_number", text="Phone Number")
        self.assignment_tree.heading("vehicle_type", text="Vehicle Type")
        self.assignment_tree.heading("category", text="Category")
        self.assignment_tree.heading("assigned_slot", text="Assigned Slot")
        self.assignment_tree.heading("slot_size", text="Slot Size")

        self.assignment_tree.column("vehicle_number", width=140, anchor="center")
        self.assignment_tree.column("owner_name", width=160, anchor="center")
        self.assignment_tree.column("phone_number", width=140, anchor="center")
        self.assignment_tree.column("vehicle_type", width=180, anchor="center")
        self.assignment_tree.column("category", width=120, anchor="center")
        self.assignment_tree.column("assigned_slot", width=110, anchor="center")
        self.assignment_tree.column("slot_size", width=100, anchor="center")

        self.assignment_tree.pack(fill="both", expand=True)

        self.status_label = tk.Label(
            self.root,
            text="Ready for allocation.",
            font=("Arial", 10, "italic"),
            bg="#f4f6f8",
            fg="#444444"
        )
        self.status_label.pack(pady=5)

    def handle_category_selection(self, selected_category):
        if selected_category == "VIP" and self.vip_var.get():
            self.reservable_var.set(False)
            self.ev_var.set(False)
        elif selected_category == "Reservable" and self.reservable_var.get():
            self.vip_var.set(False)
            self.ev_var.set(False)
        elif selected_category == "EV" and self.ev_var.get():
            self.vip_var.set(False)
            self.reservable_var.set(False)

    def enforce_vehicle_number(self, event=None):
        current = self.vehicle_number_entry.get()
        cleaned = "".join(ch for ch in current if ch.isalnum()).upper()

        if current != cleaned:
            self.vehicle_number_entry.delete(0, tk.END)
            self.vehicle_number_entry.insert(0, cleaned)

    def enforce_owner_name(self, event=None):
        current = self.owner_name_entry.get()
        cleaned = "".join(ch for ch in current.upper() if ch.isalpha() or ch == " ")

        if current != cleaned:
            self.owner_name_entry.delete(0, tk.END)
            self.owner_name_entry.insert(0, cleaned)

    def enforce_phone_number(self, event=None):
        current = self.phone_entry.get()
        cleaned = "".join(ch for ch in current if ch.isdigit())[:10]

        if current != cleaned:
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, cleaned)

    def assign_slot(self):
        vehicle_number = self.vehicle_number_entry.get().strip().upper()
        owner_name = self.owner_name_entry.get().strip().upper()
        phone_number = self.phone_entry.get().strip()
        vehicle_type = self.vehicle_type_var.get().strip()
        vehicle_size = get_size_from_vehicle_type(vehicle_type)

        category = get_selected_category(
            self.vip_var.get(),
            self.reservable_var.get(),
            self.ev_var.get()
        )

        if not vehicle_number or not owner_name or not phone_number or not vehicle_type:
            messagebox.showerror(
                "Missing Input",
                "Please enter Vehicle Number, Owner Name, Phone Number, and Vehicle Type."
            )
            return

        if not vehicle_number.isalnum():
            messagebox.showerror("Invalid Vehicle Number", "Vehicle Number must contain only letters and numbers.")
            return

        if not all(ch.isalpha() or ch == " " for ch in owner_name):
            messagebox.showerror("Invalid Owner Name", "Owner Name must contain only letters and spaces.")
            return

        if len(phone_number) != 10:
            messagebox.showerror("Invalid Phone Number", "Phone Number must be exactly 10 digits.")
            return

        flags = get_vehicle_flags(category)

        vehicle = Vehicle(
            vehicle_id=vehicle_number,
            vehicle_type=vehicle_type,
            size=vehicle_size,
            priority=1,
            is_vip=flags["is_vip"],
            is_electric=flags["is_electric"]
        )

        assigned_slot = allocate_slot_fifo(vehicle, category, self.slots)

        if assigned_slot is None:
            self.status_label.config(
                text=f"No valid slot found for vehicle {vehicle_number} in category {category}.",
                fg="red"
            )
            return

        self.assignment_tree.insert(
            "",
            tk.END,
            values=(
                vehicle_number,
                owner_name,
                phone_number,
                vehicle_type,
                category,
                assigned_slot.slot_id,
                assigned_slot.size
            )
        )

        self.status_label.config(
            text=f"Vehicle {vehicle_number} assigned to slot {assigned_slot.slot_id}.",
            fg="green"
        )

        self.clear_form()

    def delete_selected_entry(self):
        selected_item = self.assignment_tree.selection()

        if not selected_item:
            messagebox.showwarning("No Selection", "Please select an entry to delete.")
            return

        item_id = selected_item[0]
        row_values = self.assignment_tree.item(item_id, "values")
        assigned_slot_id = row_values[5]

        for slot in self.slots:
            if slot.slot_id == assigned_slot_id:
                slot.is_available = True
                break

        self.assignment_tree.delete(item_id)

        self.status_label.config(
            text=f"Entry deleted and slot {assigned_slot_id} is available again.",
            fg="green"
        )

    def clear_form(self):
        self.vehicle_number_entry.delete(0, tk.END)
        self.owner_name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.vehicle_type_var.set(ALL_VEHICLE_TYPES[0])
        self.vip_var.set(False)
        self.reservable_var.set(False)
        self.ev_var.set(False)


if __name__ == "__main__":
    root = tk.Tk()
    app = SPASGui(root)
    root.mainloop()
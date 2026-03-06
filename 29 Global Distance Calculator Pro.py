# Import all libraries
import tkinter as tk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Geolocation service
geolocator = Nominatim(user_agent="distance_app", timeout=10)


def get_coordinates(place):
    try:
        location = geolocator.geocode(place)
        if location:
            return (location.latitude, location.longitude)
    except:
        return None


def calculate_distance():

    place1 = city1_entry.get()
    place2 = city2_entry.get()
    mode = transport_var.get()

    coord1 = get_coordinates(place1)
    coord2 = get_coordinates(place2)

    if not coord1 or not coord2:
        messagebox.showerror("Error", "❌ Location not found!")
        return

    air_distance = geodesic(coord1, coord2).km

    if mode == "Plane ✈":
        distance_text = f"{air_distance:.2f} KM (Air Distance)"

    elif mode == "Bus 🚌":
        bus_distance = air_distance * 1.3
        distance_text = f"{bus_distance:.2f} KM (Estimated Road Distance)"

    elif mode == "Train 🚆":
        train_distance = air_distance * 1.2
        distance_text = f"{train_distance:.2f} KM (Estimated Train Distance)"

    output_box.config(state="normal")
    output_box.delete(1.0, tk.END)

    result_text = f"""
🌍 GLOBAL DISTANCE RESULT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📍 FROM   : {place1}
📍 TO     : {place2}

🚗 MODE   : {mode}

📏 DISTANCE
   • {distance_text}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✨ Powered by Python + GeoPy
"""

    output_box.insert(tk.END, result_text)
    output_box.config(state="disabled")


# Main Window
root = tk.Tk()
root.title("🌍 Global Distance Calculator Pro")

# Bigger window so no scrolling needed
root.geometry("650x600")
root.config(bg="#1e1e2f")

# Title
title = tk.Label(
    root,
    text="🌍 Global Distance Calculator",
    font=("Segoe UI", 22, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=20)

# Input Frame
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=10)

# First Location
tk.Label(
    frame,
    text="Enter First Location",
    font=("Segoe UI", 12),
    bg="#1e1e2f",
    fg="white"
).grid(row=0, column=0, pady=10, padx=10)

city1_entry = tk.Entry(frame, width=35, font=("Segoe UI", 12))
city1_entry.grid(row=0, column=1)

# Second Location
tk.Label(
    frame,
    text="Enter Second Location",
    font=("Segoe UI", 12),
    bg="#1e1e2f",
    fg="white"
).grid(row=1, column=0, pady=10, padx=10)

city2_entry = tk.Entry(frame, width=35, font=("Segoe UI", 12))
city2_entry.grid(row=1, column=1)

# Transport selection
tk.Label(
    frame,
    text="Select Transport Type",
    font=("Segoe UI", 12),
    bg="#1e1e2f",
    fg="white"
).grid(row=2, column=0, pady=10)

transport_var = tk.StringVar()

transport = ttk.Combobox(
    frame,
    textvariable=transport_var,
    width=32,
    state="readonly",
    font=("Segoe UI", 11)
)

transport["values"] = (
    "Bus 🚌",
    "Train 🚆",
    "Plane ✈"
)

transport.current(0)
transport.grid(row=2, column=1)

# Calculate Button
calc_btn = tk.Button(
    root,
    text="🚀 Calculate Distance",
    font=("Segoe UI", 13, "bold"),
    bg="#00b894",
    fg="white",
    padx=12,
    pady=6,
    command=calculate_distance
)

calc_btn.pack(pady=20)

# Result Box (bigger so everything fits)
output_box = tk.Text(
    root,
    height=15,
    width=60,
    font=("Segoe UI", 12),
    bg="#111827",
    fg="#E5E7EB",
    bd=0,
    relief="flat",
    padx=25,
    pady=20
)

output_box.pack(pady=10)
output_box.config(state="disabled")

# Footer
footer = tk.Label(
    root,
    text="Developed with Python 🐍",
    font=("Segoe UI", 10),
    bg="#1e1e2f",
    fg="gray"
)

footer.pack(pady=10)

root.mainloop()

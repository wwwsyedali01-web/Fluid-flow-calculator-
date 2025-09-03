# Fluid Flow Calculator with Validity Checks
# Author: Syed Hassan Ali (Mechanical Engineering Student)

import math

def fluid_velocity(flow_rate, diameter):
    area = (math.pi * diameter**2) / 4
    velocity = flow_rate / area
    return velocity

def head_pressure(velocity, g=9.81):
    return (velocity**2) / (2 * g)

def friction_loss(f, L, D, velocity, g=9.81):
    return f * (L / D) * (velocity**2) / (2 * g)

def pump_power(rho, g, flow_rate, total_head, efficiency=1.0):
    return (rho * g * flow_rate * total_head) / efficiency

def check_range(value, min_val, max_val, name):
    if value < min_val or value > max_val:
        print(f"⚠ Warning: {name} = {value:.3f} is outside standard range ({min_val}-{max_val}).")
    return

print("---- Fluid Flow Calculator ----")
# Inputs
flow_rate = float(input("Enter flow rate (m^3/s): "))
diameter = float(input("Enter pipe diameter (m): "))
pipe_length = float(input("Enter pipe length (m): "))
friction_factor = float(input("Enter Darcy friction factor (f): "))
rho = float(input("Enter fluid density (kg/m^3): "))
efficiency = float(input("Enter pump efficiency (0-1): "))

# Calculations
velocity = fluid_velocity(flow_rate, diameter)
hv = head_pressure(velocity)
hf = friction_loss(friction_factor, pipe_length, diameter, velocity)
total_head = hv + hf
power = pump_power(rho, 9.81, flow_rate, total_head, efficiency)

# Results
print("\n---- Results ----")
print(f"Fluid Velocity        = {velocity:.3f} m/s")
print(f"Velocity Head (hv)    = {hv:.3f} m")
print(f"Frictional Head (hf)  = {hf:.3f} m")
print(f"Total Head (H)        = {total_head:.3f} m")
print(f"Pump Power Required   = {power:.2f} W")

# Validation checks
print("\n---- Validation ----")
check_range(velocity, 0.5, 10, "Fluid Velocity")
check_range(hv, 0.01, 30, "Velocity Head")
check_range(hf, 0.01, 50, "Frictional Head")
check_range(total_head, 1, 100, "Total Head")
check_range(power, 10, 1e6, "Pump Power")

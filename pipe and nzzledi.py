import numpy as np
import matplotlib.pyplot as plt

# Given Data from EnduroMAX 100 HP pump
MotoPOW = 100  
JetPOW = 85  
OP_psi = 60000  
OP_pa = OP_psi * 6894.76 
FlowRate_gpm = 2.25  
FlowRate_lpm = 8.52  
Pump_FP = (1118, 1575, 1118)  #  in mm

MotoPOW_wt = MotoPOW * 745.7  # Convert HP to Watts
JetPOW_wt = JetPOW * 745.7  # Convert HP to Watts


H_efficiency = (JetPOW_wt / MotoPOW_wt) * 100  # Efficiency 

FlowRate_std = FlowRate_lpm / 60000  # Convert LPM to m³/s

RPumpPOW_w = FlowRate_std * OP_pa  # Power required in Watts
RPumpPOW_hp= RPumpPOW_w / 745.7  # Convert to HP

Density = 1000 
orifice_dia_m = 0.001  
Area1 = np.pi * (orifice_dia_m / 2)**2
velocity_exit = FlowRate_std / Area1  # Exit velocity (m/s)

# 7. Calculate Power Loss in Pump
power_loss_w = MotoPOW_wt - JetPOW_wt  # Power lost in the pump
power_loss_percentage = (power_loss_w / MotoPOW_wt) * 100  # Percentage Loss

# 8. Print Key Design Parameters
print(f"Motor Power: {MotoPOW} HP ({MotoPOW_wt:.2f} W)")
print(f"Max Jet Power: {JetPOW} HP ({JetPOW_wt:.2f} W)")
print(f"Output Pressure: {OP_psi} psi ({OP_pa:.2f} Pa)")
print(f"Flow Rate: {FlowRate_gpm} GPM ({FlowRate_lpm} LPM, {FlowRate_std:.6f} m³/s)")
print(f"Hydraulic Efficiency: {H_efficiency:.2f}%")
print(f"Required Pump Power: {RPumpPOW_hp:.2f} HP ({RPumpPOW_w:.2f} W)")
print(f"Nozzle Exit Velocity: {velocity_exit:.2f} m/s")
print(f"Power Loss in Pump: {power_loss_w:.2f} W ({power_loss_percentage:.2f}%)")
print(f"Pump Footprint (L × W × H): {Pump_FP[0]} mm × {Pump_FP[1]} mm × {Pump_FP[2]} mm")

# 9. Generate Graph Data
flow_rates = np.linspace(5, 15, 50) 
efficiencies = []
nozzle_velocities = []
power_losses = []

for flow_rate in flow_rates:
    FlowRate_std = flow_rate / 60000  # Convert LPM to m³/s
    velocity = FlowRate_std / Area1  # Nozzle exit velocity
    hydraulic_eff = (JetPOW_wt / MotoPOW_wt) * 100
    power_loss = MotoPOW_wt - JetPOW_wt

    efficiencies.append(hydraulic_eff)
    nozzle_velocities.append(velocity)
    power_losses.append(power_loss / 1000)  # Convert to kW

# 10. Plot Graphs
fig, ax1 = plt.subplots(figsize=(10, 5))

# Graph 1: Efficiency vs. Flow Rate
ax1.set_xlabel("Flow Rate (LPM)")
ax1.set_ylabel("Hydraulic Efficiency (%)", color="tab:blue")
ax1.plot(flow_rates, efficiencies, label="Efficiency", color="tab:blue")
ax1.tick_params(axis="y", labelcolor="tab:blue")

# Graph 2: Nozzle Velocity vs. Flow Rate
ax2 = ax1.twinx()
ax2.set_ylabel("Nozzle Exit Velocity (m/s)", color="tab:red")
ax2.plot(flow_rates, nozzle_velocities, label="Nozzle Velocity", color="tab:red", linestyle="dashed")
ax2.tick_params(axis="y", labelcolor="tab:red")

# Graph 3: Power Loss
fig, ax3 = plt.subplots(figsize=(10, 5))
ax3.set_xlabel("Flow Rate (LPM)")
ax3.set_ylabel("Power Loss (kW)", color="tab:green")
ax3.plot(flow_rates, power_losses, label="Power Loss", color="tab:green", linestyle="dotted")
ax3.tick_params(axis="y", labelcolor="tab:green")

# Show Graphs
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")
ax3.legend(loc="upper left")
plt.title("Pump Performance Analysis")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# === Step 1: Define Control Points for the Bézier Curve ===
# Format: [X (mm), Radius (mm)]
P0 = np.array([0.0, 2.5])       # Throat start
P1 = np.array([2.0, 4.0])       # Control point 1
P2 = np.array([4.5, 1.0])       # Control point 2
P3 = np.array([6.8, 0.22])      # Exit point

# === Step 2: Bézier Curve Function ===
def bezier_cubic(P0, P1, P2, P3, num=100):
    t = np.linspace(0, 1, num)[:, None]
    one_minus_t = 1 - t
    curve = (one_minus_t ** 3) * P0 + \
            3 * (one_minus_t ** 2) * t * P1 + \
            3 * one_minus_t * (t ** 2) * P2 + \
            (t ** 3) * P3
    return curve

# === Step 3: Generate Curve ===
curve = bezier_cubic(P0, P1, P2, P3)

# === Step 4: Plotting for Visual Verification ===
plt.figure(figsize=(8, 4))
plt.plot(curve[:, 0], curve[:, 1], 'b-', label='Bézier Curve')
plt.plot([P0[0], P1[0], P2[0], P3[0]], [P0[1], P1[1], P2[1], P3[1]], 'ro--', label='Control Points')
plt.title('Bell-Shaped Nozzle Curve (Bézier)')
plt.xlabel('Axial Length (mm)')
plt.ylabel('Radius (mm)')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# === Step 5: Export to CSV for AutoCAD ===
df = pd.DataFrame(curve, columns=["X", "Y"])  # Y is radius
df.to_csv("bezier_nozzle_curve_points.csv", index=False)

print("✅ CSV exported as 'bezier_nozzle_curve_points.csv'")

print("✅ Bézier curve plotted successfully.")
print("✅ Bézier curve data exported successfully.")    
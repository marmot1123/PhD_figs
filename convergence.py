"""
Convergence plot script for FPM functions.

Generates a 2x4 subplot showing f+ functions with fixed a1=1/√2
and varying a2 values (1/2, 3/4, 7/8, 0.999).
Left column: 3D plots, Right column: Heatmaps
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from src.fpm import FPMCalculator, create_grid


def plot_convergence(output_path="figs/convergence.pdf"):
    """
    Create a convergence plot showing f+ functions with varying a2 values.
    
    Args:
        output_path: Path to save the figure
    """
    # Parameters
    a1_fixed = 1/np.sqrt(2)  # Fixed a1 parameter
    a2_values = [7/8, 15/16, 31/32, 0.999]  # Varying a2 parameters
    
    # Create coordinate grid
    v1, v2 = create_grid(n_points=201)
    
    # Create figure with 2x4 subplots
    fig = plt.figure(figsize=(12, 16))
    plt.subplots_adjust(hspace=0.4, wspace=0.3)
    
    mgn = 0.1  # Margin for heatmaps
    
    for i, a2 in enumerate(a2_values):
        print(f"Processing a2 = {a2:.3f}...")
        
        # Initialize FPM calculator
        calculator = FPMCalculator(a1=a1_fixed, a2=a2)
        
        # Calculate f+ function
        f_plus = calculator.f_plus(v1, v2)
        
        # Left column: 3D plot
        ax_3d = fig.add_subplot(4, 2, 2*i + 1, projection='3d')
        ax_3d.plot_surface(v1, v2, f_plus, edgecolor='royalblue', lw=0.2, alpha=0.3)
        ax_3d.set(zlim=(0, 2.0))
        ax_3d.set(xlabel=r"$v_1$", ylabel=r"$v_2$")
        ax_3d.set_title(f"({chr(97 + 2*i)}) $a_2={a2:.3f}$")
        
        # Right column: Heatmap
        ax_heat = fig.add_subplot(4, 2, 2*i + 2)
        heatmap = ax_heat.pcolormesh(v1, v2, f_plus, vmin=0, vmax=2.0, cmap='RdBu_r')
        cbar = fig.colorbar(heatmap, ax=ax_heat)
        ax_heat.axis("equal")
        ax_heat.set(xlim=(-1.0 - mgn, 1.0 + mgn), ylim=(-1.0 - mgn, 1.0 + mgn))
        ax_heat.set(xlabel=r"$v_1$", ylabel=r"$v_2$")
        ax_heat.set_title(f"({chr(97 + 2*i + 1)}) $a_2={a2:.3f}$")
    
    
    # Ensure figs directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save the figure
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Convergence plot saved to {output_path}")


def main():
    """Main function to generate convergence plot."""
    print("Generating convergence plot...")
    plot_convergence()
    print("Done!")


if __name__ == "__main__":
    main()
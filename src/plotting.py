"""
Plotting utilities for FPM visualization.

This module contains functions for creating 3D plots and heatmaps
of f+ and f- functions.
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def plot_fpm_combined(v1, v2, f_plus, f_minus, output_path="figs/plot_fpm.pdf"):
    """
    Create a combined 2x2 plot showing 3D and heatmap views of f+ and f-.
    
    Args:
        v1, v2: Meshgrid arrays for coordinates
        f_plus: f+ function values
        f_minus: f- function values
        output_path: Path to save the figure
    """
    mgn = 0.1
    
    fig = plt.figure(figsize=(10, 10))
    plt.subplots_adjust(wspace=0.3)

    # f+ 3D plot
    ax1 = fig.add_subplot(221, projection='3d')
    ax1.plot_surface(v1, v2, f_plus, edgecolor='royalblue', lw=0.2, alpha=0.3)
    ax1.set(zlim=(0, 1))
    ax1.set(xlabel=r"$v_1$", ylabel=r"$v_2$")
    ax1.set_title(r"(a) 3D Plot of $f_+(v_1, v_2)$")

    # f+ heatmap
    ax2 = fig.add_subplot(222)
    heatmap = ax2.pcolormesh(v1, v2, f_plus, vmin=0, vmax=1, cmap='RdBu_r')
    cbar2 = fig.colorbar(heatmap, ax=ax2)
    ax2.axis("equal")
    ax2.set(xlim=(-1.0 - mgn, 1.0 + mgn), ylim=(-1.0 - mgn, 1.0 + mgn))
    ax2.set(xlabel=r"$v_1$", ylabel=r"$v_2$")
    ax2.set_title(r"(b) Heatmap of $f_+(v_1, v_2)$")

    # f- 3D plot
    ax3 = fig.add_subplot(223, projection='3d')
    ax3.plot_surface(v1, v2, f_minus, edgecolor='royalblue', lw=0.2, alpha=0.3)
    ax3.set(zlim=(0, 1))
    ax3.set(xlabel=r"$v_1$", ylabel=r"$v_2$")
    ax3.set_title(r"(c) 3D Plot of $f_-(v_1, v_2)$")

    # f- heatmap
    ax4 = fig.add_subplot(224)
    heatmap = ax4.pcolormesh(v1, v2, f_minus, vmin=0, vmax=1, cmap='RdBu_r')
    cbar4 = fig.colorbar(heatmap, ax=ax4)
    ax4.axis("equal")
    ax4.set(xlim=(-1.0 - mgn, 1.0 + mgn), ylim=(-1.0 - mgn, 1.0 + mgn))
    ax4.set(xlabel=r"$v_1$", ylabel=r"$v_2$")
    ax4.set_title(r"(d) Heatmap of $f_-(v_1, v_2)$")

    fig.savefig(output_path)
    plt.close()


def plot_3d_surface(v1, v2, func_values, title, output_path=None):
    """
    Create a standalone 3D surface plot.
    
    Args:
        v1, v2: Meshgrid arrays for coordinates
        func_values: Function values to plot
        title: Plot title
        output_path: Optional path to save the figure
    """
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.plot_surface(v1, v2, func_values, edgecolor='royalblue', lw=0.2, alpha=0.3)
    ax.set(xlabel=r"$v_1$", ylabel=r"$v_2$")
    ax.set_title(title)
    
    if output_path:
        fig.savefig(output_path)
        plt.close()
    else:
        plt.show()


def plot_heatmap(v1, v2, func_values, title, output_path=None):
    """
    Create a standalone heatmap plot.
    
    Args:
        v1, v2: Meshgrid arrays for coordinates
        func_values: Function values to plot
        title: Plot title
        output_path: Optional path to save the figure
    """
    mgn = 0.1
    
    fig, ax = plt.subplots(figsize=(6, 6))
    
    heatmap = ax.pcolormesh(v1, v2, func_values, vmin=0, vmax=1, cmap='RdBu_r')
    cbar = fig.colorbar(heatmap, ax=ax)
    ax.axis("equal")
    ax.set(xlim=(-1.0 - mgn, 1.0 + mgn), ylim=(-1.0 - mgn, 1.0 + mgn))
    ax.set(xlabel=r"$v_1$", ylabel=r"$v_2$")
    ax.set_title(title)
    
    if output_path:
        fig.savefig(output_path)
        plt.close()
    else:
        plt.show()
"""
Configuration file for FPM figure generation.

This file defines the parameters and output paths for generating
multiple FPM figures with different parameter combinations.
"""

# List of figure configurations
# Each configuration is a dictionary with:
# - name: descriptive name for the figure
# - a1, a2: FPM parameters
# - output_path: path where the figure will be saved
# - description: optional description of the parameter set

FIGURE_CONFIGS = [
    {
        "name": "default",
        "a1": 1/4,
        "a2": 3/4,
        "output_path": "figs/plot_fpm_default.pdf",
        "description": "Default parameters (a1=0.25, a2=0.75)"
    },
    {
        "name": "symmetric",
        "a1": 1/2,
        "a2": 1/2,
        "output_path": "figs/plot_fpm_symmetric.pdf",
        "description": "Symmetric parameters (a1=0.5, a2=0.5)"
    },
    {
        "name": "small_a1",
        "a1": 1/8,
        "a2": 3/4,
        "output_path": "figs/plot_fpm_small_a1.pdf",
        "description": "Small a1 parameter (a1=0.125, a2=0.75)"
    },
    {
        "name": "large_a1",
        "a1": 3/8,
        "a2": 3/4,
        "output_path": "figs/plot_fpm_large_a1.pdf",
        "description": "Large a1 parameter (a1=0.375, a2=0.75)"
    },
    {
        "name": "small_a2",
        "a1": 1/4,
        "a2": 1/2,
        "output_path": "figs/plot_fpm_small_a2.pdf",
        "description": "Small a2 parameter (a1=0.25, a2=0.5)"
    },
    {
        "name": "large_a2",
        "a1": 1/4,
        "a2": 7/8,
        "output_path": "figs/plot_fpm_large_a2.pdf",
        "description": "Large a2 parameter (a1=0.25, a2=0.875)"
    }
]

# Grid resolution for calculations
GRID_RESOLUTION = 201

# Common plotting parameters
PLOT_PARAMS = {
    "figure_size": (10, 10),
    "colormap": "RdBu_r",
    "z_limit": (0, 1),
    "margin": 0.1
}
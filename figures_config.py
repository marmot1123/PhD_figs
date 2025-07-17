"""
Configuration file for FPM figure generation.

This file defines the parameters and output paths for generating
multiple FPM figures with different parameter combinations.
"""

import numpy as np

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
        "name": "most_symmetric",
        "a1": 1/np.sqrt(2),
        "a2": 1/np.sqrt(2),
        "output_path": "figs/plot_fpm_most_symmetric.pdf",
        "description": "Most symmetric parameters (a1=1/√2, a2=1/√2)"
    },
    {
        "name": "single_ellipse",
        "a1": 1/2,
        "a2": 1/2,
        "output_path": "figs/plot_fpm_single_ellipse.pdf",
        "description": "Single ellipse support (a1=1/2, a2=1/2)"
    },
    {
        "name": "a_equal_b",
        "a1": 1/2,
        "a2": np.sqrt(3)/2,
        "output_path": "figs/plot_fpm_a_equal_b.pdf",
        "description": "a equal b parameter (a1=1/2, a2=√3/2)"
    },
    {
        "name": "b_equal_0",
        "a1": 1/np.sqrt(2),
        "a2": 0.999,
        "output_path": "figs/plot_fpm_b_equal_0.pdf",
        "description": "b equal 0 parameter (a1=1/√2, a2=0.999)"
    },
    {
        "name": "a1_and_a2_nearly_equal_1",
        "a1": 0.999,
        "a2": 0.999,
        "output_path": "figs/plot_fpm_a1_and_a2_nearly_equal_1.pdf",
        "description": "a1 and a2 nearly equal 1 parameter (a1=0.999, a2=0.999)"
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
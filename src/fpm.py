"""
FPM (Function Plus Minus) calculation module.

This module contains functions for calculating f+ and f- functions
based on the mathematical formulation in the PhD thesis.
"""

import numpy as np


class FPMCalculator:
    """Calculator for f+ and f- functions."""
    
    def __init__(self, a1=1/4, a2=3/4):
        """
        Initialize FPM calculator with parameters.
        
        Args:
            a1: First parameter (default: 1/4)
            a2: Second parameter (default: 3/4)
        """
        self.a1 = a1
        self.a2 = a2
        self.b1 = np.sqrt(1 - a1**2)
        self.b2 = np.sqrt(1 - a2**2)
    
    def F0(self, v1, v2):
        """Calculate F0 function."""
        return (((self.a1 * self.b2)**2 + (self.a2 * self.b1)**2) - 
                (self.b1**2 + self.b2**2) * (v1 + v2)**2 / 4 - 
                (self.a1**2 + self.a2**2) * (v1 - v2)**2 / 4) / (2 * self.a1 * self.a2 * self.b1 * self.b2)
    
    def F1(self, v1, v2):
        """Calculate F1 function."""
        return 1 - (v1 + v2)**2 / (4 * self.a1**2) - (v1 - v2)**2 / (4 * self.b1**2)
    
    def F2(self, v1, v2):
        """Calculate F2 function."""
        return 1 - (v1 + v2)**2 / (4 * self.a2**2) - (v1 - v2)**2 / (4 * self.b2**2)
    
    def mask(self, v1, v2):
        """Calculate mask for valid domain."""
        return (self.F1(v1, v2) >= 0) & (self.F2(v1, v2) >= 0)
    
    def f_plus(self, v1, v2):
        """Calculate f+ function."""
        m = self.mask(v1, v2)
        result = np.zeros_like(v1, dtype=float)
        result[~m] = 0
        
        F1_vals = self.F1(v1, v2)[m]
        F2_vals = self.F2(v1, v2)[m]
        F0_vals = self.F0(v1, v2)[m]
        v1_vals = v1[m]
        v2_vals = v2[m]
        
        sqrt_term = np.sqrt(F1_vals * F2_vals)
        denominator = (2 * np.pi**2 * (1 - v1_vals**2) * (1 - v2_vals**2) * sqrt_term)
        
        result[m] = (F0_vals + sqrt_term) / denominator
        return result
    
    def f_minus(self, v1, v2):
        """Calculate f- function."""
        m = self.mask(v1, v2)
        result = np.zeros_like(v1, dtype=float)
        result[~m] = 0
        
        F1_vals = self.F1(v1, v2)[m]
        F2_vals = self.F2(v1, v2)[m]
        F0_vals = self.F0(v1, v2)[m]
        v1_vals = v1[m]
        v2_vals = v2[m]
        
        sqrt_term = np.sqrt(F1_vals * F2_vals)
        denominator = (2 * np.pi**2 * (1 - v1_vals**2) * (1 - v2_vals**2) * sqrt_term)
        
        result[m] = (F0_vals - sqrt_term) / denominator
        return result


def create_grid(n_points=201, range_limit=1.0):
    """
    Create a meshgrid for FPM calculations.
    
    Args:
        n_points: Number of points in each dimension
        range_limit: Range limit for v1 and v2
        
    Returns:
        Tuple of (v1, v2) meshgrids
    """
    v1 = np.linspace(-range_limit, range_limit, n_points)
    v2 = np.linspace(-range_limit, range_limit, n_points)
    return np.meshgrid(v1, v2)
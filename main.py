import os
from src.fpm import FPMCalculator, create_grid
from src.plotting import plot_fpm_combined
from figures_config import FIGURE_CONFIGS, GRID_RESOLUTION


def main():
    print("Generating PhD thesis figures...")
    
    # Ensure figs directory exists
    os.makedirs("figs", exist_ok=True)
    
    # Create coordinate grid once for all calculations
    v1, v2 = create_grid(n_points=GRID_RESOLUTION)
    
    # Generate figures for each configuration
    for config in FIGURE_CONFIGS:
        print(f"Generating {config['name']} figure...")
        print(f"  Parameters: a1={config['a1']:.3f}, a2={config['a2']:.3f}")
        print(f"  Description: {config['description']}")
        
        # Initialize FPM calculator with specified parameters
        calculator = FPMCalculator(a1=config['a1'], a2=config['a2'])
        
        # Calculate f+ and f- functions
        f_plus = calculator.f_plus(v1, v2)
        f_minus = calculator.f_minus(v1, v2)
        
        # Generate plot
        plot_fpm_combined(v1, v2, f_plus, f_minus, output_path=config['output_path'])
        print(f"  Saved to {config['output_path']}")
        print()
    
    print(f"All {len(FIGURE_CONFIGS)} figures generated successfully!")


if __name__ == "__main__":
    main()

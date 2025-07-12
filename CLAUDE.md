# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains Python code for generating figures for Seki Motoki's PhD thesis. The project is in early development with a minimal structure.

## Project Structure

- `main.py` - Entry point that generates multiple FPM figures based on configuration
- `figures_config.py` - Configuration file defining FPM parameters and output paths
- `src/fpm.py` - FPM (Function Plus Minus) calculation module with FPMCalculator class
- `src/plotting.py` - Plotting utilities for 3D plots and heatmaps
- `figs/` - Directory for generated figure outputs
- `pyproject.toml` - Project configuration with numpy and matplotlib dependencies

## Development Commands

This project uses uv for dependency management:

```bash
# Generate figures
uv run main.py

# Install dependencies
uv sync

# Add new dependencies
uv add <package-name>
```

## Python Environment

- Required Python version: 3.12+
- Dependencies: numpy>=2.1.0, matplotlib>=3.9.0
- Uses .python-version file for version specification

## Code Organization

The project follows a modular structure:
- Mathematical calculations are handled by the `FPMCalculator` class in `src/fpm.py`
- Visualization functions are separated into `src/plotting.py`
- Figure configurations (parameters and output paths) are defined in `figures_config.py`
- The main entry point reads configurations and generates multiple figures
- Generated figures are saved to the `figs/` directory

## Configuration

To add new figure variants, modify `figures_config.py`:
- Add entries to `FIGURE_CONFIGS` list with different `a1`, `a2` parameters
- Specify unique `output_path` for each configuration
- Adjust `GRID_RESOLUTION` if needed for different detail levels
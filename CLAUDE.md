# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains Python code for generating figures for Seki Motoki's PhD thesis. The project is in early development with a minimal structure.

## Project Structure

- `main.py` - Entry point with basic "Hello World" functionality
- `src/` - Empty source directory for future code organization
- `figs/` - Empty directory intended for generated figures
- `pyproject.toml` - Project configuration using Python 3.12+

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
- No dependencies currently defined in pyproject.toml
- Uses .python-version file for version specification

## Code Organization

The project follows a standard Python package structure with source code intended to go in the `src/` directory and generated figures in the `figs/` directory. The project is managed with a pyproject.toml configuration file but currently has minimal setup.
# Seki Motoki's PhD thesis figures

## Setup

### uv Installation
```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or via pip
pip install uv
```

### uv Update
```bash
# Update uv to latest version
uv self update
```

### Project Cache Update
```bash
# Clear and update project cache
uv cache clean
uv sync
```

## Figure Generation

### Generate All Figures
```bash
# Generate all FPM figures with different parameter combinations
uv run main.py
```

This will create multiple PDF figures in the `figs/` directory based on the configurations defined in `figures_config.py`. Each figure shows 3D plots and heatmaps of f+ and f- functions with different parameter sets (a1, a2).
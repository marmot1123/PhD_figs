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

### Generate Convergence Plot
```bash
# Generate convergence plot with fixed a1 and varying a2
uv run convergence.py
```

This creates a single 2x4 subplot figure (`figs/convergence.pdf`) showing f+ function with fixed a1=1/√2 and varying a2 values (7/8, 15/16, 31/32, 0.999). Left column shows 3D plots, right column shows heatmaps.
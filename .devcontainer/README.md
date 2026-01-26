# Dev Container Setup for playmath

This directory contains the configuration for running the playmath project in GitHub Codespaces with SageMath and CoCalc.

## What's Included

- **Base Image**: `sagemathinc/cocalc-docker-x86_64` - Includes SageMath, Jupyter, Mathematica, and many other mathematical tools
- **VS Code Extensions**: Jupyter notebook support for `.ipynb` files
- **Forwarded Ports**:
  - **443**: CoCalc HTTPS interface
  - **8080**: HTTP access
  - **8888**: Jupyter notebook server
  - **9999**: SageMath server

## Getting Started in Codespaces

1. Open your repository in GitHub Codespaces (Code → Create codespace on master)
2. Wait for the container to build (first time may take 5-10 minutes)
3. The container automatically installs dependencies and verifies SageMath

## Using SageMath

### Option 1: Jupyter Notebooks
Open any `.ipynb` file in VS Code - the Jupyter extension will render it. You can run cells directly.

### Option 2: SageMath Terminal
Open a terminal in Codespaces and run:
```bash
sage
```

Or run SageMath scripts:
```bash
sage script.sage
```

### Option 3: Jupyter Server
The CoCalc image includes Jupyter. Start it with:
```bash
jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root
```

## Key Files

- `devcontainer.json` - Dev Container configuration

## Notes

- The image is large (~2-3GB), so initial pull may take a few minutes
- GitHub Codespaces free tier provides 4 cores and 16GB RAM, which is sufficient for SageMath
- All your work is saved to the repository as usual
- Changes to the dev container config require rebuilding (press F1 → Rebuild container)

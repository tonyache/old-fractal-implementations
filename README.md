# old-fractal-implementations
This repo intends to rescue old fractal implementations from references like "Fractals: Endlessly Repeated Geometrical Figures" by Hans Lauwerier. Implementations like those in Lauwerier's book are written in (Turbo/GW-)BASIC, which suffice it to say, nobody uses anymore. Given that some of the old code suggests that one can obtain beautiful fractal patterns with very simple code, I decided to port some of the TURBO basic implementations to Python while also adapting the old BASIC code so that it can be used with modern basic platforms. 

# Meander & Julia Fractals — BASIC vs Python

This repo recreates two retro fractal programs from a vintage (Turbo/GW-)BASIC book, and adds modern Python ports.

- **BASIC (GW-BASIC via PC-BASIC)**  
  - `julia_gwbasic.bas` — Julia set (CGA screen)  
  - `meander_gwbasic.bas` — “Meander / Koch-cross” fractal with a baseline and motif  
- **Python**  
  - `julia.py` — vectorized Julia set (NumPy + Matplotlib)  
  - `meander_pixels.py` — meander using **pixel** baseline (matches BASIC screen)  
  - `meander_window.py` — meander using **math coordinates** with WINDOW-style scaling


---

## 1) Running the BASIC versions (PC-BASIC)

### Install PC-BASIC
```bash
pip install pcbasic

Given a file basicFile.bas, it suffices to run

pcbasic --video=cga --run meander_gwbasic.bas




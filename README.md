# Pac-Man Polar Plot

A simple Python visualization that draws **Pac-Man using a mathematical polar equation**, rendered with NumPy and Matplotlib.

## About

This project takes a mathematical equation for a Pac-Man-shaped polar curve and implements it in Python using:

- **NumPy** for numerical calculations.
- **Matplotlib** for plotting and rendering the curve.

The equation determines the radius `r` as a function of the angle `θ`:

```math
r(\theta) =
\exp\left(
10\frac{|2\theta|-1-\left||2\theta|-1\right|}{|2\theta|}
\right),
\qquad
\theta\in(-\pi,\pi]
```

The resulting polar curve resembles Pac-Man. The area enclosed by the curve is filled with yellow and displayed against a black background.

## Origin of the equation

The equation used in this project is **not my original creation**.

It comes from the Mathematics Stack Exchange question **“Smooth Pac-Man Curve?”**, posted by the user **2'5 9'2** on June 12, 2013.

In the original post, the author explains that curiosity and an example involving smooth functions led them to this polar curve. They also note that the equation is undefined at `θ = 0`, but the curve can be extended by defining:

```math
r(0)=0
```

This repository is a Python implementation and visualization of that mathematical curve using NumPy and Matplotlib.

### Credit

Original equation and idea:

**2'5 9'2 — “Smooth Pac-Man Curve?”, Mathematics Stack Exchange (2013)**

Source: [Smooth Pac-Man Curve?](https://math.stackexchange.com/questions/418641/smooth-pac-man-curve)

All credit for the original mathematical equation goes to its author.

## Requirements

- Python 3
- NumPy
- Matplotlib

Install the required packages with:

```bash
pip install numpy matplotlib
```

## Running

Clone the repository or download the source code, then run:

```bash
python polar_pacman.py
```

A Matplotlib window should open displaying Pac-Man.

## How it works

The program creates a polar coordinate plot and evaluates the Pac-Man equation for 1,000 values of `θ` between `-π` and `π`.

```python
theta = np.linspace(-np.pi, np.pi, 1000)
```

The mathematical equation is translated directly into NumPy operations:

```python
r = np.exp(
    10 * (
        np.abs(2*theta)
        - np.abs(np.abs(2*theta) - 1)
        - 1
    ) / np.abs(2*theta)
)
```

The resulting curve is then filled and outlined in yellow:

```python
ax.fill(theta, r, color='yellow')
ax.plot(theta, r, color='yellow')
```

Finally, the polar ticks are removed and the background is changed to black to produce the familiar Pac-Man appearance.

## Acknowledgements

Thanks to **2'5 9'2** for sharing the original Pac-Man polar curve on Mathematics Stack Exchange.

This project simply adapts that mathematical idea into a small Python visualization using NumPy and Matplotlib.

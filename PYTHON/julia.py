import argparse, numpy as np, matplotlib.pyplot as plt

def julia(cr=-0.8, ci=0.156, iters=300, w=800, h=600,
          xmin=-1.6, xmax=1.6, ymin=-1.2, ymax=1.2):
    x = np.linspace(xmin, xmax, w, dtype=np.float64)
    y = np.linspace(ymin, ymax, h, dtype=np.float64)
    X, Y = np.meshgrid(x, y)
    Zx, Zy = X.copy(), Y.copy()
    Cx, Cy = cr, ci
    escape = np.zeros((h, w), dtype=np.int32)

    for n in range(1, iters + 1):
        # z <- z^2 + c  (in real/imag parts)
        zx2, zy2 = Zx * Zx, Zy * Zy
        Zy = 2.0 * Zx * Zy + Cy
        Zx = zx2 - zy2 + Cx
        mag2 = Zx * Zx + Zy * Zy
        mask = (escape == 0) & (mag2 > 4.0)
        escape[mask] = n

    escape[escape == 0] = iters
    return escape

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--cr", type=float, default=-0.8)
    ap.add_argument("--ci", type=float, default=0.156)
    ap.add_argument("--iters", type=int, default=300)
    ap.add_argument("--width", type=int, default=800)
    ap.add_argument("--height", type=int, default=600)
    args = ap.parse_args()

    img = julia(args.cr, args.ci, args.iters, args.width, args.height)
    plt.figure()
    plt.imshow(img, origin="lower", extent=(-1.6, 1.6, -1.2, 1.2))
    plt.title(f"Julia set: c = {args.cr} + {args.ci} i")
    plt.axis("off")
    plt.show()


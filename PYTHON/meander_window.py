# meander_window.py
# Meander/Koch-cross with book-style math coordinates and WINDOW mapping.

import argparse
import numpy as np
import matplotlib.pyplot as plt

def replace_segment_math(p0, p1, motif_uv):
    """
    Map a unit-segment motif (u along, v perpendicular) onto math segment p0->p1.
    Returns a list of math-space points.
    """
    p0 = np.asarray(p0, float); p1 = np.asarray(p1, float)
    v = p1 - p0
    L = np.hypot(v[0], v[1])
    if L == 0:  # degenerate segment
        return [p0.tolist()]
    ux = v / L
    uy = np.array([-ux[1], ux[0]])  # 90° CCW
    out = []
    for u, vperp in motif_uv:
        out.append((p0 + (u * L) * ux + (vperp * L) * uy).tolist())
    return out

def iterate_polyline_math(poly_math, motif_uv, order):
    """
    Apply motif replacement 'order' times to each consecutive pair in the math-space polyline.
    """
    pts = poly_math[:]
    for _ in range(order):
        new_pts = []
        for i in range(len(pts) - 1):
            seg = replace_segment_math(pts[i], pts[i+1], motif_uv)
            if i > 0:
                new_pts.extend(seg[1:])  # avoid duplicating join
            else:
                new_pts.extend(seg)
        pts = new_pts
    return pts

def window_to_pixels(points_math, xmin, xmax, ymin, ymax, W, H):
    """
    Map math coords (xmin..xmax, ymin..ymax) -> pixel coords (0..W-1, 0..H-1), with
    Y inverted so (xmin,ymax) is top-left like a BASIC screen.
    """
    pts = np.asarray(points_math, float)
    x = pts[:, 0]; y = pts[:, 1]
    px = (x - xmin) / (xmax - xmin) * (W - 1)
    py = (ymax - y) / (ymax - ymin) * (H - 1)  # invert Y
    return np.column_stack([px, py])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--order", type=int, default=3, help="recursion order (1..5 reasonable)")
    ap.add_argument("--window", type=float, nargs=4, metavar=("XMIN","XMAX","YMIN","YMAX"),
                    default=(-2.4, 2.4, -1.8, 1.8), help="math window like BASIC's WINDOW")
    ap.add_argument("--size", type=int, nargs=2, metavar=("W","H"),
                    default=(320, 200), help="output pixel size (default 320x200)")
    ap.add_argument("--save", metavar="PNG", help="save image to file")
    args = ap.parse_args()

    p = max(1, args.order)
    xmin, xmax, ymin, ymax = args.window
    W, H = args.size

    # --- Baseline in math coords (same square the book often uses)
    base_math = [(-1, 1), (1, 1), (1, -1), (-1, -1), (-1, 1)]  # closed polygon

    # --- Koch 5-point motif in unit-segment coords (u along, v perp)
    motif_uv = [(0.0, 0.0), (1.0/3, 0.0), (0.5, 1.0/3), (2.0/3, 0.0), (1.0, 0.0)]

    # Build/draw each side separately
    plt.figure(figsize=(W/100.0, H/100.0), dpi=100)
    ax = plt.gca()
    ax.set_facecolor((0.0, 0.58, 0.58))  # teal-ish background (like CGA screen)
    colors = [(0,0,0), (0.96,0.96,0.2), (0.9,0.2,0.2), (0.2,0.85,0.2)]  # 0 unused; 1..3 used

    for s in range(len(base_math) - 1):
        seg_poly = base_math[s:s+2]
        curve_math = iterate_polyline_math(seg_poly, motif_uv, p)
        curve_px = window_to_pixels(curve_math, xmin, xmax, ymin, ymax, W, H)

        # draw like BASIC: color cycles with segment index
        for k in range(1, len(curve_px)):
            cidx = (k % 3) + 1
            x0, y0 = curve_px[k-1]; x1, y1 = curve_px[k]
            ax.plot([x0, x1], [y0, y1], color=colors[cidx], linewidth=1.0)

    ax.set_xlim(0, W-1); ax.set_ylim(H-1, 0)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    ax.set_title(f"Meander (order {p})", color="white")

    if args.save:
        plt.savefig(args.save, bbox_inches="tight", pad_inches=0.0)
    plt.show()

if __name__ == "__main__":
    main()

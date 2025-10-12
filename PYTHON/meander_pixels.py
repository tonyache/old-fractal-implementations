# meander_pixels.py
# Koch "meander" on a pixel baseline (matches the GW-BASIC version)
import argparse, numpy as np, matplotlib.pyplot as plt

def replace_segment(p0, p1, motif_uv):
    """Map a unit-segment motif (u along, v perpendicular) onto the segment p0->p1."""
    p0 = np.asarray(p0, float); p1 = np.asarray(p1, float)
    v = p1 - p0
    L = np.hypot(v[0], v[1])
    if L == 0:  # degenerate
        return [p0.tolist()]
    ux = v / L
    uy = np.array([-ux[1], ux[0]])  # 90° CCW
    out = []
    for u, vperp in motif_uv:
        out.append((p0 + (u * L) * ux + (vperp * L) * uy).tolist())
    return out

def iterate_polyline(poly, motif_uv, order):
    """Apply motif to every consecutive pair in poly, for 'order' iterations."""
    pts = poly[:]
    for _ in range(order):
        new_pts = []
        for i in range(len(pts) - 1):
            seg = replace_segment(pts[i], pts[i+1], motif_uv)
            if i > 0:
                new_pts.extend(seg[1:])  # avoid duplicate join
            else:
                new_pts.extend(seg)
        pts = new_pts
    return pts

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--order", type=int, default=4, help="recursion order (1..4)")
    ap.add_argument("--save", metavar="PNG", help="optional output filename")
    args = ap.parse_args()
    p = max(1, args.order)

    # --- Baseline in SCREEN 1 pixel coords (closed square inside 320x200)
    base = [(20,20), (300,20), (300,180), (20,180), (20,20)]

    # --- Koch motif in unit-segment coordinates (u along, v perpendicular)
    # (0,0) -> (1/3,0) -> (1/2,1/3) -> (2/3,0) -> (1,0)
    motif = [(0.0,0.0), (1.0/3,0.0), (0.5,1.0/3), (2.0/3,0.0), (1.0,0.0)]

    # Build curve for each side, then draw
    plt.figure(figsize=(9.6, 6.0), dpi=100)
    ax = plt.gca()
    # CGA-ish colors: 1=yellow, 2=red, 3=green; background teal
    ax.set_facecolor((0.0, 0.58, 0.58))
    colors = [(0,0,0), (0.96,0.96,0.2), (0.9,0.2,0.2), (0.2,0.85,0.2)]

    for s in range(len(base)-1):
        poly = base[s:s+2]  # one side as 2 points
        pts = iterate_polyline(poly, motif, p)
        # draw like BASIC: color cycles with segment index
        for k in range(1, len(pts)):
            cidx = (k % 3) + 1
            x0,y0 = pts[k-1]
            x1,y1 = pts[k]
            ax.plot([x0,x1],[y0,y1], color=colors[cidx], linewidth=1.0)

    # Match SCREEN 1 geometry
    ax.set_xlim(0, 319); ax.set_ylim(199, 0)  # invert Y (top-left origin)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    ax.set_title(f"Koch meander (order {p})", color="white")

    if args.save:
        plt.savefig(args.save, bbox_inches="tight", pad_inches=0.0)
    plt.show()

if __name__ == "__main__":
    main()

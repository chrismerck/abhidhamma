"""Zoomed-out view to k = 10,000: only what general theorems give at that scale.

Main panel: the (k, n) plane. Two insets magnify the upper edge of the wedge and
its lower edge near k = 5000, where single cells can be told apart.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Patch, Rectangle

from cells import cell
from render import (SURFACE, INK, INK2, BLUE, ORANGE, AQUA, ZERO, UNKNOWN, SPECIAL, draw_cell, short_label)

KM = 10000


def mix(a, b, t):
    ca = [int(a[i:i + 2], 16) for i in (1, 3, 5)]
    cb = [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(round(t * x + (1 - t) * y) for x, y in zip(ca, cb))


BLEND = mix(ORANGE, UNKNOWN, 0.25)   # every 4th column is a thread


def inset(fig, rect, k0, k1, n0, n1, title):
    ax = fig.add_axes(rect)
    ax.set_facecolor(SURFACE)
    ax.set_xlim(k0 - 0.5, k1 + 0.5)
    ax.set_ylim(n0 - 0.5, n1 + 0.5)
    ax.set_aspect("equal")
    ax.set_xticks(range(k0, k1 + 1, 4))
    ax.set_yticks(range(n0, n1 + 1, 4))
    ax.tick_params(length=0, labelsize=7, colors=INK2)
    for s in ax.spines.values():
        s.set_edgecolor(INK2)
        s.set_linewidth(0.8)
    ax.set_title(title, fontsize=9.5, color=INK, loc="left")
    for k in range(k0, k1 + 1):
        for n in range(max(n0, k + 1), n1 + 1):
            q = n - k
            c = cell(k, q)
            lab = short_label(k, q)
            if q == 1:
                draw_cell(ax, k, n, SPECIAL, None, edge="#d9d7d0")
            elif q == 2:
                draw_cell(ax, k, n, AQUA)
            elif c["status"] == "unknown":
                draw_cell(ax, k, n, UNKNOWN, None, hatch="////")
            elif c["knotted"] == "no":
                hole = 2 * q <= k + 3
                draw_cell(ax, k, n, ZERO, "0" if hole else None, edge=INK if hole else None, fs=7)
            elif c["rank"] == 1:
                draw_cell(ax, k, n, ORANGE, "Z" if lab == "Z" else None, fs=7)
            else:
                draw_cell(ax, k, n, BLUE, lab, fs=7)
    return ax


def main(path="tapestry_zoomout_10000.png"):
    fig = plt.figure(figsize=(13, 13.6), dpi=150)
    fig.patch.set_facecolor(SURFACE)
    ax = fig.add_axes([0.075, 0.07, 0.60, 0.60 * 13 / 13.6 * 1.5])
    ax.set_facecolor(SURFACE)
    nmax = 15010
    ax.set_xlim(0, KM)
    ax.set_ylim(0, nmax)
    ax.set_aspect("equal")
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(length=0, labelsize=8.5, colors=INK2)
    ax.set_xticks(range(0, KM + 1, 2000))
    ax.set_yticks(range(0, nmax, 2000))
    ax.set_xlabel("k  (dimension of the knotted sphere)", color=INK2, fontsize=10)
    ax.set_ylabel("n  (dimension of the ambient sphere)", color=INK2, fontsize=10)
    # unknotted region: n > 1.5k + 1.5
    ax.add_patch(Polygon([(0, 1.5), (KM, 1.5 * KM + 1.5), (KM, nmax), (0, nmax)], closed=True, facecolor=ZERO,
                         edgecolor="none"))
    # wedge: k + 3 <= n <= 1.5k + 1.5
    ax.add_patch(Polygon([(3, 6), (KM, KM + 3), (KM, 1.5 * KM + 1.5)], closed=True, facecolor=BLEND, edgecolor="none"))
    ax.plot([3, KM], [6, 1.5 * KM + 1.5], color=INK, lw=1.2)
    ax.plot([1, KM], [3, KM + 2], color=AQUA, lw=1.6)
    ax.text(1500, 11400, "unknotted\n(2q > k + 3: group is 0)", fontsize=11, color=INK, ha="left", va="center")
    ax.text(6350, 7850, "wedge interior:\nevery 4th column proven infinite,\nthe rest unknown", fontsize=9.5, color=INK,
            ha="center", va="center", rotation=50)
    ax.text(5600, 1500, "n ≤ k: outside the grid", fontsize=9.5, color=INK2, ha="left", va="center")
    ax.annotate("upper edge  n = (3k+3)/2:\nvalues known on two diagonals,\nperiod 8 in k", xy=(3000, 4501.5),
                xytext=(330, 6900), fontsize=9, color=INK, arrowprops=dict(arrowstyle="-", color=INK2, lw=0.7))
    ax.annotate("lower edge: q = 2 (always knotted)\nand q = 1 (image unknotted)", xy=(7600, 7602), xytext=(6000, 3300),
                fontsize=9, color=INK, arrowprops=dict(arrowstyle="-", color=INK2, lw=0.7))
    # inset markers
    for (x, y) in ((5006, 7513), (5006, 5010)):
        ax.add_patch(Rectangle((x - 110, y - 110), 220, 220, facecolor="none", edgecolor=INK, lw=1.0, zorder=5))
    a1 = inset(fig, [0.70, 0.575, 0.275, 0.33], 4996, 5015, 7494, 7523, "Upper edge, k = 4996 … 5015 (cells)")
    a2 = inset(fig, [0.70, 0.215, 0.275, 0.30], 4996, 5015, 4997, 5020, "Lower edge, k = 4996 … 5015 (cells)")
    handles = [Patch(facecolor=ORANGE, label="proved infinite (k ≡ 3 mod 4, 3 ≤ q ≤ (k+3)/2)"),
               Patch(facecolor=BLUE, label="proved finite and non-zero, value known"),
               Patch(facecolor=ZERO, edgecolor=INK, label="hole: proved 0 inside the wedge (k ≡ 2 mod 4, n = 3k/2 + 1)"),
               Patch(facecolor=ZERO, label="proved 0 (unknotted)"),
               Patch(facecolor=UNKNOWN, hatch="////", edgecolor="#8f8d85", label="unknown"),
               Patch(facecolor=BLEND, label="main panel only: threads and unknown blended 1 : 3"),
               Patch(facecolor=AQUA, label="q = 2: always knotted"),
               Patch(facecolor=SPECIAL, edgecolor="#d9d7d0", label="q = 1: image unknotted")]
    fig.legend(handles=handles, loc="lower right", bbox_to_anchor=(0.985, 0.045), frameon=False, fontsize=8.6,
               labelcolor=INK, alignment="left")
    fig.text(0.075, 0.965, "The tapestry to k = 10,000: only what general theorems give", fontsize=15, fontweight="bold",
             color=INK)
    fig.text(0.075, 0.943, "Nothing inside the wedge is drawn from computation at this scale. Known: the wedge itself, two "
             "diagonals along its upper edge, and the infinite threads.", fontsize=9.5, color=INK2)
    fig.text(0.075, 0.012, "Upper-edge pattern by k mod 8:  0: Z/2+Z/2   1: Z/2   2: 0   3: Z   4: Z/4   5: Z/2   6: 0   7: Z.   "
             "Second diagonal as recalled from Haefliger 1966 and verified here for q ≤ 8.", fontsize=8.5, color=INK2)
    fig.savefig(path, facecolor=SURFACE)
    plt.close(fig)


if __name__ == "__main__":
    main()
    print("rendered zoom-out")

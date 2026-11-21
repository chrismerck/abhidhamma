"""Render the detailed tapestry pictures (PNG) from cells.py.

  tapestry_knotted.png   knotted / unknotted / unknown
  tapestry_order.png     log of torsion order, infinite groups as threads
  tapestry_primes.png    which primes divide the torsion order (one panel per prime)

Axes: x = k (dimension of the sphere), y = n (ambient dimension), q = n - k.
Colours are the validated reference palette of the charting guidance
(blue / orange / aqua validate for all-pairs use; everything else is neutral).
"""
import math

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.cm import ScalarMappable

from cells import cell, COMPUTED

SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK2 = "#52514e"
BLUE = "#2a78d6"
ORANGE = "#eb6834"
AQUA = "#1baf7a"
ZERO = "#eceae5"      # trivial group: recedes
UNKNOWN = "#c9c7c0"   # unknown: neutral + hatch
SPECIAL = "#f4f3ef"   # q = 1 row
RAMP = ["#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7", "#3987e5", "#2a78d6",
        "#256abf", "#1c5cab", "#184f95", "#104281", "#0d366b"]

K_MAX = 20
RAMP10 = [RAMP[round(j * 12 / 9)] for j in range(10)]   # orders 2, 4, ..., 1024
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


def n_max(kmax):
    return kmax + (kmax + 3) // 2 + 2


def short_label(k, q):
    c = cell(k, q)
    if q == 1:
        return "?" if k == 3 else ""
    if q == 2:
        return ""
    if c["status"] == "unknown":
        return "?"
    if (k, q) in COMPUTED:
        rank, tors, order = COMPUTED[(k, q)][:3]
        if tors is None:
            t = "(%d)" % order
        else:
            parts, i = [], 0
            while i < len(tors):
                j = i
                while j < len(tors) and tors[j] == tors[i]:
                    j += 1
                parts.append(str(tors[i]) + (str(j - i).translate(SUP) if j - i > 1 else ""))
                i = j
            t = "·".join(parts)
        if rank:
            return "Z" + ("+" + t if t else "")
        return t if t else "0"
    if c["rank"] == 1:
        return "Z" if c["torsion_order"] == 1 else "Z+?"
    g = c["group"]
    return {"0": "0", "Z/2": "2", "Z/4": "4", "Z/2 + Z/2": "2²"}.get(g, g)


def text_on(fill):
    r, g, b = (int(fill[i:i + 2], 16) / 255 for i in (1, 3, 5))
    lum = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return "#ffffff" if lum < 0.42 else INK


def base_axes(ax, kmax, title, subtitle):
    nm = n_max(kmax)
    ax.set_facecolor(SURFACE)
    ax.set_xlim(0.5, kmax + 0.5)
    ax.set_ylim(1.5, nm + 0.5)
    ax.set_aspect("equal")
    ax.set_xticks(range(1, kmax + 1))
    ax.set_yticks(range(2, nm + 1))
    ax.tick_params(length=0, labelsize=8, colors=INK2)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xlabel("k  (dimension of the knotted sphere)", color=INK2, fontsize=10)
    ax.set_ylabel("n  (dimension of the ambient sphere)", color=INK2, fontsize=10)
    ax.set_title(title, color=INK, fontsize=14, loc="left", fontweight="bold", pad=26)
    ax.text(0, 1.012, subtitle, transform=ax.transAxes, color=INK2, fontsize=9.5, va="bottom")
    # codimension guides in the empty triangle below the diagonal
    for q, lab in ((1, "q = 1"), (2, "q = 2"), (3, "q = 3")):
        k = kmax
        ax.text(k + 0.62, k + q, lab, fontsize=7.5, color=INK2, va="center", ha="left", clip_on=False)
    # the unknotting boundary 2q = k + 3, drawn as a staircase between cells
    xs, ys = [], []
    for k in range(3, kmax + 1):
        top = k + (k + 3) // 2 + 0.5
        xs += [k - 0.5, k + 0.5]
        ys += [top, top]
    ax.plot(xs, ys, color=INK2, lw=1.0, zorder=7, solid_joinstyle="miter")
    ax.annotate("above this line: 2q > k + 3, always unknotted", xy=(6.5, 10.5), xytext=(0.9, 13.4),
                fontsize=8.5, color=INK2, arrowprops=dict(arrowstyle="-", color=INK2, lw=0.6), zorder=8)


def draw_cell(ax, k, n, fill, label=None, hatch=None, thread=False, fs=6.6, edge=None):
    ax.add_patch(Rectangle((k - 0.47, n - 0.47), 0.94, 0.94, facecolor=fill, edgecolor=edge or "none",
                           linewidth=(1.4 if edge == INK else 0.6) if edge else 0, zorder=2))
    if hatch:
        ax.add_patch(Rectangle((k - 0.47, n - 0.47), 0.94, 0.94, facecolor="none", edgecolor="#8f8d85",
                               linewidth=0, hatch=hatch, zorder=3))
    if thread:
        ax.add_patch(Rectangle((k - 0.47, n - 0.5), 0.2, 1.0, facecolor=ORANGE, edgecolor="none", zorder=4))
    if label:
        x = k + (0.1 if thread else 0)
        size = fs if len(label) <= 4 else fs - 1.0 if len(label) <= 6 else fs - 2.0
        ax.text(x, n, label, ha="center", va="center", fontsize=size, color=text_on(fill), zorder=6)


def fig_knotted(path="tapestry_knotted.png", kmax=K_MAX):
    fig, ax = plt.subplots(figsize=(11.5, 15.5), dpi=150)
    fig.patch.set_facecolor(SURFACE)
    base_axes(ax, kmax, "Where a k-sphere knots smoothly in the n-sphere",
              "Cell label = group of isotopy classes C_k^q (q = n − k ≥ 3).  12 = Z/12,  2² = Z/2 + Z/2,  "
              "Z+6 = Z + Z/6,  (60) = finite of order 60, structure not determined.")
    for k in range(1, kmax + 1):
        for n in range(k + 1, n_max(kmax) + 1):
            q = n - k
            c = cell(k, q)
            lab = short_label(k, q)
            if q == 1:
                if k == 3:
                    draw_cell(ax, k, n, UNKNOWN, "?", hatch="////")
                else:
                    draw_cell(ax, k, n, SPECIAL, None, edge="#d9d7d0")
            elif q == 2:
                draw_cell(ax, k, n, AQUA)
            elif c["status"] == "unknown":
                draw_cell(ax, k, n, UNKNOWN, "?", hatch="////")
            elif c["knotted"] == "no":
                hole = 2 * q <= k + 3
                draw_cell(ax, k, n, ZERO, "0" if hole else None, edge=INK if hole else None, fs=8)
            elif c["rank"] == 1:
                draw_cell(ax, k, n, ORANGE, lab)
            else:
                draw_cell(ax, k, n, BLUE, lab)
    handles = [Patch(facecolor=BLUE, label="knotted: finite non-zero group"),
               Patch(facecolor=ORANGE, label="knotted: infinite group (rank 1)"),
               Patch(facecolor=ZERO, label="unknotted: group is 0"),
               Patch(facecolor=ZERO, edgecolor=INK, label="hole: group is 0 inside the wedge"),
               Patch(facecolor=UNKNOWN, hatch="////", edgecolor="#8f8d85", label="unknown (not determined here)"),
               Patch(facecolor=AQUA, label="q = 2: always knotted (infinitely many types, not a finite group)"),
               Patch(facecolor=SPECIAL, edgecolor="#d9d7d0", label="q = 1: image always unknotted (k = 3 open)")]
    ax.legend(handles=handles, loc="lower right", bbox_to_anchor=(1.0, 0.0), frameon=False, fontsize=9,
              labelcolor=INK, title="Each cell", title_fontsize=9.5, alignment="left")
    fig.text(0.012, 0.008, "Complete for k ≤ 13 (plus q = 3 to k = 16). Beyond that only general theorems are drawn. "
             "Sources and derivations: REPORT.md, table.csv.", fontsize=8, color=INK2)
    fig.tight_layout(rect=(0, 0.015, 0.97, 1))
    fig.savefig(path, facecolor=SURFACE)
    plt.close(fig)


def ramp_colour(order):
    if order <= 1:
        return ZERO
    j = min(len(RAMP10) - 1, max(0, int(round(math.log2(order))) - 1))
    return RAMP10[j]


def fig_order(path="tapestry_order.png", kmax=K_MAX):
    fig, ax = plt.subplots(figsize=(11.5, 15.5), dpi=150)
    fig.patch.set_facecolor(SURFACE)
    base_axes(ax, kmax, "Size of the knot group: order of the torsion subgroup",
              "Fill = log₂ of the torsion order (darker = larger).  Orange thread = the group is infinite (Z + torsion); "
              "threads run up every column k ≡ 3 mod 4.")
    for k in range(1, kmax + 1):
        for n in range(k + 1, n_max(kmax) + 1):
            q = n - k
            c = cell(k, q)
            lab = short_label(k, q)
            if q <= 2:
                draw_cell(ax, k, n, SPECIAL, None, edge="#d9d7d0")
                continue
            order = c["torsion_order"]
            thread = c["rank"] == 1
            if order == "":
                draw_cell(ax, k, n, UNKNOWN, "?" if not thread else None, hatch="////", thread=thread)
            else:
                show = lab if 2 * q <= k + 3 else None
                draw_cell(ax, k, n, ramp_colour(order), show, thread=thread)
    cmap = ListedColormap(RAMP10)
    norm = BoundaryNorm([j - 0.5 for j in range(0, len(RAMP10) + 1)], cmap.N)
    cax = fig.add_axes([0.585, 0.082, 0.33, 0.011])
    cb = fig.colorbar(ScalarMappable(norm=norm, cmap=cmap), cax=cax, orientation="horizontal")
    cb.set_ticks(range(len(RAMP10)))
    cb.set_ticklabels([str(2 ** (j + 1)) for j in range(len(RAMP10))])
    cb.ax.tick_params(labelsize=8, colors=INK2, length=0)
    cb.outline.set_visible(False)
    cax.set_title("torsion order (log scale)", fontsize=9, color=INK, loc="left")
    handles = [Patch(facecolor=ORANGE, label="infinite group: thread"),
               Patch(facecolor=ZERO, label="torsion trivial (group 0, or exactly Z on a thread)"),
               Patch(facecolor=UNKNOWN, hatch="////", edgecolor="#8f8d85", label="torsion unknown"),
               Patch(facecolor=SPECIAL, edgecolor="#d9d7d0", label="q = 1, 2: not groups of this kind")]
    ax.legend(handles=handles, loc="lower right", bbox_to_anchor=(1.0, 0.085), frameon=False, fontsize=9,
              labelcolor=INK, alignment="left")
    fig.text(0.012, 0.008, "Largest value in the block: C_12^3 = Z/84 + Z/6 + Z/2, order 1008. "
             "Complete for k ≤ 13 (plus q = 3 to k = 16).", fontsize=8, color=INK2)
    fig.tight_layout(rect=(0, 0.015, 0.97, 1))
    fig.savefig(path, facecolor=SURFACE)
    plt.close(fig)


def fig_primes(path="tapestry_primes.png", kmax=17):
    primes = [2, 3, 5, 7]
    fig, axes = plt.subplots(1, 4, figsize=(17, 8.4), dpi=150)
    fig.patch.set_facecolor(SURFACE)
    nm = n_max(kmax)
    for ax, p in zip(axes, primes):
        ax.set_facecolor(SURFACE)
        ax.set_xlim(2.5, kmax + 0.5)
        ax.set_ylim(5.5, nm + 0.5)
        ax.set_aspect("equal")
        ax.set_xticks(range(3, kmax + 1, 2))
        ax.set_yticks(range(6, nm + 1, 2))
        ax.tick_params(length=0, labelsize=7.5, colors=INK2)
        for s in ax.spines.values():
            s.set_visible(False)
        ax.set_title("prime %d" % p, color=INK, fontsize=12, loc="left", fontweight="bold")
        ax.set_xlabel("k", color=INK2, fontsize=9)
        if p == 2:
            ax.set_ylabel("n", color=INK2, fontsize=9)
        hits = 0
        for k in range(3, kmax + 1):
            for n in range(k + 3, nm + 1):
                q = n - k
                c = cell(k, q)
                order = c["torsion_order"]
                thread = c["rank"] == 1
                if order == "":
                    draw_cell(ax, k, n, UNKNOWN, None, hatch="////", thread=thread)
                elif order % p == 0:
                    draw_cell(ax, k, n, BLUE, None, thread=thread)
                    hits += 1
                else:
                    draw_cell(ax, k, n, ZERO, None, thread=thread)
        ax.text(0.98, 0.03, "%d cell%s with %d-torsion" % (hits, "" if hits == 1 else "s", p),
                transform=ax.transAxes, ha="right", fontsize=8.5, color=INK2)
    handles = [Patch(facecolor=BLUE, label="the prime divides the torsion order"),
               Patch(facecolor=ZERO, label="it does not (torsion known)"),
               Patch(facecolor=UNKNOWN, hatch="////", edgecolor="#8f8d85", label="torsion unknown"),
               Patch(facecolor=ORANGE, label="thread: group is infinite")]
    fig.legend(handles=handles, loc="lower center", ncol=4, frameon=False, fontsize=9.5, labelcolor=INK)
    fig.suptitle("Which primes divide the order of the torsion of C_k^q (q = n − k ≥ 3)", x=0.012, ha="left",
                 fontsize=14, fontweight="bold", color=INK)
    fig.text(0.012, 0.925, "One panel per prime. No prime above 7 occurs in the determined range. "
             "Odd torsion sits almost entirely in codimension 3 (bottom diagonal).", fontsize=9.5, color=INK2)
    fig.tight_layout(rect=(0, 0.05, 1, 0.92))
    fig.savefig(path, facecolor=SURFACE)
    plt.close(fig)


if __name__ == "__main__":
    fig_knotted()
    fig_order()
    fig_primes()
    print("rendered")

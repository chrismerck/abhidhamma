"""Cell values for the Haefliger knot groups C_k^q (k = sphere dimension, q = codimension).

Every value here is either a theorem (with the source named) or was derived in
DERIVATIONS.md from Haefliger's triad exact sequences. Nothing is interpolated.

A value is (rank, torsion, text, status, source, evidence) where
  rank     : 0 or 1
  torsion  : list of cyclic orders, or None when only the order is known
  order    : order of the torsion subgroup (int) or None when unknown
"""

HAEF61 = "Haefliger 1961/1966 (unknotting for 2q > k+3)"
HAEF62 = "Haefliger 1962, Knotted (4k-1)-spheres in 6k-space"
HAEF66 = "Haefliger 1966, Differentiable embeddings of S^n in S^{n+q} for q>2"
HERE = "this work, DERIVATIONS.md"

# evidence tags
RE = "re-derived here"
TWO = "two exact sequences agree"
ONE = "one exact sequence"
BR = "order certain; structure uses a Toda-bracket argument"

# (k, q): (rank, torsion list or None, torsion order, status, source, evidence, note)
COMPUTED = {
    # ---- q = 3
    (3, 3): (1, [], 1, "theorem", HAEF62, RE + "; confirmed in search snippet", ""),
    (4, 3): (0, [12], 12, "theorem", HAEF66, RE + "; confirmed in search snippet", ""),
    (5, 3): (0, [2, 2], 4, "computed-here", HERE + " q=3", TWO + "; splits because C_5^3 -> C_5^4 retracts onto the nu^2 class",
             "Manifold Atlas lists E^8(S^5) as unknown; starting claim C_5^3 = 0 is wrong"),
    (6, 3): (0, [2], 2, "computed-here", HERE + " q=3", TWO, "starting claim C_6^3 = 0 is wrong"),
    (7, 3): (1, [6], 6, "computed-here", HERE + " q=3", ONE, ""),
    (8, 3): (0, [30], 30, "computed-here", HERE + " q=3", TWO, ""),
    (9, 3): (0, [3], 3, "computed-here", HERE + " q=3", TWO,
             "whole group is the image of the exotic 10-spheres of order 3 (reparametrised unknots)"),
    (10, 3): (0, [2], 2, "computed-here", HERE + " q=3", TWO, ""),
    (11, 3): (1, [12], 12, "computed-here", HERE + " q=3", ONE, ""),
    (12, 3): (0, [84, 6, 2], 1008, "computed-here", HERE + " q=3", TWO, ""),
    (13, 3): (0, [2, 2, 2, 2], 16, "computed-here", HERE + " q=3", BR, ""),
    (14, 3): (0, [6, 2], 12, "computed-here", HERE + " q=3", BR, "uses pi_17(S^3) = Z30, pi_16(S^3) = Z6"),
    (15, 3): (1, None, 60, "computed-here", HERE + " q=3", ONE,
              "torsion Z15 + (Z4 or Z2^2); uses eta^2.kappa = 0"),
    (16, 3): (0, None, 240, "computed-here", HERE + " q=3", ONE,
              "Z15 + a 2-group of order 16; uses pi_19(S^3), mu.sigma = eta.rho"),
    # ---- q = 4
    (5, 4): (0, [2], 2, "theorem", HAEF66, RE, ""),
    (6, 4): (0, [], 1, "theorem", HAEF66, RE, "second-line hole"),
    (7, 4): (1, [], 1, "computed-here", HERE + " q=4", TWO, "Manifold Atlas lists E^11(S^7) as unknown"),
    (8, 4): (0, [2], 2, "computed-here", HERE + " q=4", TWO, ""),
    (9, 4): (0, [2], 2, "computed-here", HERE + " q=4", "uses beta1 = <alpha1,alpha1,alpha1>",
             "if the bracket step failed the group would be Z6"),
    (10, 4): (0, [4], 4, "computed-here", HERE + " q=4", "uses beta1 = <alpha1,alpha1,alpha1>",
              "if the bracket step failed the order would be 12"),
    (11, 4): (1, [2], 2, "computed-here", HERE + " q=4", TWO, ""),
    (12, 4): (0, [], 1, "computed-here", HERE + " q=4", TWO, "a hole away from the edge"),
    (13, 4): (0, [2, 2], 4, "computed-here", HERE + " q=4", "one exact sequence + vanishing of a secondary term",
              "the vanishing uses pi_13(Sp(2)) = Z/4 + Z/2; if it failed the group would be Z/2. Non-zero either way"),
    # ---- q = 5
    (7, 5): (1, [], 1, "theorem", HAEF62, RE, ""),
    (8, 5): (0, [2, 2], 4, "theorem", HAEF66, RE, ""),
    (9, 5): (0, [2, 2, 2], 8, "computed-here", HERE + " q=5", BR, "uses beta1 = <alpha1,alpha1,alpha1> for the 3-part"),
    (10, 5): (0, [24, 4], 96, "computed-here", HERE + " q=5", TWO, "3-part uses beta1 = <alpha1,alpha1,alpha1>"),
    (11, 5): (1, [2, 2, 2], 8, "computed-here", HERE + " q=5", TWO, ""),
    (12, 5): (0, [2, 2], 4, "computed-here", HERE + " q=5", TWO, ""),
    (13, 5): (0, [12, 2], 24, "computed-here", HERE + " q=5", "one exact sequence + vanishing of a secondary term",
              "same secondary term as C_13^4 (order would be 12 if it failed); the Z4 uses nu_9 sigma_12 = 2 sigma_9 nu_16"),
    # ---- q = 6
    (9, 6): (0, [2], 2, "theorem", HAEF66, RE, ""),
    (10, 6): (0, [], 1, "theorem", HAEF66, RE, "second-line hole"),
    (11, 6): (1, [2], 2, "computed-here", HERE + " q=6", TWO, ""),
    (12, 6): (0, [2], 2, "computed-here", HERE + " q=6", TWO, ""),
    (13, 6): (0, [2], 2, "computed-here", HERE + " q=6", TWO, ""),
    # ---- q = 7, 8
    (11, 7): (1, [], 1, "theorem", HAEF62, RE, ""),
    (12, 7): (0, [4], 4, "theorem", HAEF66, RE, ""),
    (13, 7): (0, [2], 2, "computed-here", HERE + " q=7,8", TWO, ""),
    (13, 8): (0, [2], 2, "theorem", HAEF66, RE, ""),
    # ---- found during the hole search beyond the block
    (14, 7): (0, [3], 3, "computed-here", HERE + " hole search", ONE,
              "2-part vanishes (J_6 is onto pi_20(S^6)_(2)); the Z/3 is an unstable class of pi_20(S^6); uses Mimura-Toda SU(4) data"),
}

# Cells shown to be non-zero without determining the group: (k, q) -> (evidence, note).
NONZERO = {
    (14, 4): ("order count at the primes 2 and 3", "pi_14(F_3,SO_3) cannot inject into pi_14(G/O) = Z/2 + Z/2"),
    (14, 5): ("order count at the primes 2 and 3", "contains the obstruction of C_14^4"),
    (14, 6): ("maps onto C_14^7 = Z/3", "also: 3-torsion of pi_19(S^5) is not in the image of J"),
    (16, 4): ("order count at the prime 2", "pi_16(F_3,SO_3) has 2-part of order >= 4; torsion of pi_16(G/O) is Z/2"),
    (16, 5): ("order count at the prime 2", "contains the obstruction of C_16^4"),
    (16, 6): ("one exact sequence", "pi_16(SO,SO_5) has order 4, pi_16(F,F_5) = Z/2"),
    (16, 7): ("maps onto the 2-part of C_16^8", "depends on the recalled value C_16^9 = Z/2 + Z/2"),
    (16, 8): ("comparison sequence", "depends on the recalled value C_16^9 = Z/2 + Z/2"),
    (17, 3): ("one exact sequence", "eta.pi_17^S cannot cover pi_18^S = Z/8 + Z/2"),
    (17, 4): ("order count at the prime 2", "pi_17(F_3,SO_3) has 2-part of order >= 16; pi_17(G/O) has order 8"),
    (17, 5): ("order count at the prime 2", "contains the obstruction of C_17^4"),
    (17, 8): ("comparison sequence", "depends on the recalled second-line value C_18^10 = 0"),
    (18, 3): ("one exact sequence", "pi_20(S^3) (order 48) cannot inject into the elements of order 2 of pi_18^S"),
}

# Orders of the Kervaire-Milnor groups Theta_n, n = 1..20 (standard table).
THETA = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 28, 8: 2, 9: 8, 10: 6, 11: 992, 12: 1,
         13: 3, 14: 2, 15: 16256, 16: 2, 17: 16, 18: 16, 19: 523264, 20: 24}

K_BLOCK = 13  # every cell with k <= K_BLOCK and q >= 3 is determined above or by a theorem


def group_text(rank, torsion):
    parts = ["Z"] * rank
    if torsion:
        parts += ["Z/%d" % t for t in torsion]
    return " + ".join(parts) if parts else "0"


def prime_factors(n):
    out, p = [], 2
    while n > 1 and p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def cell(k, q):
    """Return a dict describing C_k^q (or the q = 1, 2 special rows)."""
    n = k + q
    d = dict(k=k, n=n, q=q, group="unknown", status="unknown", source="", rank="", torsion_order="",
             primes="", knotted="unknown", evidence="", note="")
    if q == 1:
        if k == 3:
            d.update(group="unknown", status="unknown", knotted="unknown",
                     source="smooth Schoenflies problem in S^4 is open",
                     note="every S^3 in S^4 is topologically unknotted (Brown, Mazur); smooth case open")
        else:
            th = THETA.get(k + 1)
            g = "Theta_%d" % (k + 1) + (" (order %d)" % th if th else " (order not tabulated here)")
            if k + 1 <= 6:
                g = "0"
            d.update(group=g, status="theorem", knotted="no (image)",
                     source="Schoenflies (Alexander; Brown-Mazur + Smale), Cerf, Kervaire-Milnor",
                     evidence="recalled; standard",
                     note="image always bounds a disc; classes of parametrised embeddings = Theta_{k+1}")
            if th:
                d["torsion_order"] = th
        return d
    if q == 2:
        d.update(group="infinitely many knot types (not a f.g. group)", status="theorem", knotted="yes",
                 source="classical knots (k=1); Artin spinning; Kervaire 1965; Levine 1969",
                 evidence="recalled; standard")
        return d
    # q >= 3
    if 2 * q > k + 3:
        d.update(group="0", status="theorem", source=HAEF61, rank=0, torsion_order=1, knotted="no",
                 evidence="confirmed in search snippet")
        return d
    if (k, q) in COMPUTED:
        rank, tors, order, status, source, ev, note = COMPUTED[(k, q)]
        if tors is None:
            g = ("Z + " if rank else "") + "finite of order %d (structure not determined)" % order
        else:
            g = group_text(rank, tors)
        d.update(group=g, status=status, source=source, rank=rank, torsion_order=order,
                 primes=" ".join(map(str, prime_factors(order))),
                 knotted="yes" if (rank or order > 1) else "no", evidence=ev, note=note)
        return d
    # outside the computed block: only general theorems
    if k == 2 * q - 3:
        if q % 2:
            d.update(group="Z", status="theorem", source=HAEF62, rank=1, torsion_order=1, knotted="yes",
                     evidence="confirmed in search snippet; " + RE + " (general argument)")
        else:
            d.update(group="Z/2", status="theorem", source=HAEF66, rank=0, torsion_order=2, primes="2",
                     knotted="yes", evidence="recalled; " + RE + " (general argument)")
        return d
    if k == 2 * q - 2:
        ev = "recalled, not re-read tonight; verified here for q = 3..8"
        if q % 2 == 0:
            d.update(group="0", status="theorem", source=HAEF66, rank=0, torsion_order=1, knotted="no",
                     evidence=ev, note="second-line hole")
        elif q % 4 == 1:
            d.update(group="Z/2 + Z/2", status="theorem", source=HAEF66, rank=0, torsion_order=4, primes="2",
                     knotted="yes", evidence=ev)
        else:
            d.update(group="Z/4", status="theorem", source=HAEF66, rank=0, torsion_order=4, primes="2",
                     knotted="yes", evidence=ev)
        return d
    if (k, q) in NONZERO or (k % 4 == 1 and k == 2 * q - 1):
        if (k, q) in NONZERO:
            ev, note = NONZERO[(k, q)]
        else:
            ev = "comparison sequence + second-line theorem (recalled)"
            note = "third diagonal, q odd: the group maps onto C_k^{q+1} = Z/2"
        d.update(group="non-zero (group not determined)", status="computed-here", source=HERE + " hole search",
                 rank=0, knotted="yes", evidence=ev, note=note)
        return d
    if k % 4 == 3:
        d.update(group="Z + finite (torsion not determined)", status="theorem",
                 source=HAEF66 + " (rank); Levine", rank=1, knotted="yes",
                 evidence="confirmed in search snippet; rank re-derived here")
        return d
    d.update(group="finite (not determined)", rank=0,
             note="finite by the rank theorem; nothing else established here")
    return d

"""Consistency check of the computed block against the comparison sequence (L):

  ... -> C_{k+1}^{q+1} -> pi_k(W_m) -> C_k^q -> C_k^{q+1} -> pi_{k-1}(W_m) -> ...   (m = q-1)

The orders of pi_k(W_m) come from the suspension maps E^{m+1} between unstable
spheres; the orders of C_k^q come from (A')/(B), i.e. from the J-homomorphism and
stable stems. The two sets of inputs are independent, so exactness is a real test.

For m even only the 2-primary parts are compared (see DERIVATIONS.md), for m odd
the full orders. A rank-one group is written ("Z", t) with t the torsion order.
"""
from itertools import product

from cells import COMPUTED


def two_part(n):
    t = 1
    while n % 2 == 0:
        n //= 2
        t *= 2
    return t


# orders of pi_k(W_m); "Z" = infinite cyclic. 2-primary orders for m even, full for m odd.
W = {
    2: {3: "Z", 4: 4, 5: 2, 6: 8, 7: 4, 8: 4, 9: 2, 10: 4, 11: 4, 12: 16},
    3: {5: 2, 6: 1, 7: 2, 8: 4, 9: 24, 10: 4, 11: 4, 12: 6},
    4: {7: "Z", 8: 4, 9: 4, 10: 64, 11: 4, 12: 2},
    5: {9: 2, 10: 2, 11: 8, 12: 2, 13: 1},
    6: {11: "Z", 12: 4, 13: 1},
    7: {13: 2},
}


def C(k, q, even_m):
    if 2 * q > k + 3:
        return 1
    rank, tors, order, *_ = COMPUTED[(k, q)]
    o = two_part(order) if even_m else order
    return ("Z", o) if rank else o


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def check(q, kmax=13):
    """Walk (L) for codimension q -> q+1 from the bottom (where everything is 0) upwards.

    Returns the list of solutions (image orders); exactness needs at least one."""
    m = q - 1
    even = m % 2 == 0
    seq = []  # from right (low k) to left
    for k in range(2 * q - 3, kmax + 1):
        seq += [("C", k, q + 1, C(k, q + 1, even)), ("C", k, q, C(k, q, even)), ("W", k, m, W[m].get(k))]
    seq = [s for s in seq if s[3] is not None]
    # image order r_i of the map INTO seq[i] from seq[i+1]; exactness: |A_i| = r_i * r_{i-1}' ...
    # here r_out(i) := |im(A_i -> A_{i-1})|, and |A_i| = r_out(i) * r_out(i+1).
    sols = []

    def rec(i, r_out, trail):
        # r_out = |im(A_i -> A_{i-1})| already fixed; determine r_out for i+1
        if i == len(seq):
            sols.append(trail)
            return
        a = seq[i][3]
        if a == "Z" or isinstance(a, tuple):
            # infinite group: handle pairs (C_k^q rank 1 -> C_k^{q+1} rank 1) or W = Z
            t = 1 if a == "Z" else a[1]
            # out-image finite (r_out given): kernel has finite index r_out, so the in-image is infinite
            # out-image infinite ("inf"): the in-image is the finite kernel, any divisor of t
            if r_out == "inf":
                for d in divisors(t):
                    rec(i + 1, d, trail + [d])
            else:
                rec(i + 1, "inf", trail + ["inf"])
        else:
            if r_out == "inf":
                return
            if a % r_out:
                return
            rec(i + 1, a // r_out, trail + [a // r_out])

    rec(0, 1, [])
    return seq, sols


if __name__ == "__main__":
    ok = True
    for q in range(3, 8):
        seq, sols = check(q)
        # the sequence continues to the left of the block, so only the existence of a solution is required
        names = ["%s_%d^%d" % (s[0], s[1], s[2]) if s[0] == "C" else "pi_%d(W_%d)" % (s[1], s[2]) for s in seq]
        print("q=%d -> %d : %d terms, %d consistent assignment(s)" % (q, q + 1, len(seq), len(sols)))
        ok &= bool(sols)
        if len(sols) == 1:
            print("   image orders (right to left):", sols[0])
    print("ALL CONSISTENT" if ok else "INCONSISTENT")

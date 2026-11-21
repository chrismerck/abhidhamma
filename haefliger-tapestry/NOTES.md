# NOTES — running log for the Haefliger knot tapestry

Convention used everywhere: `k` = dimension of the knotted sphere, `n` = ambient
dimension, `q = n - k` = codimension. `C_k^q` = isotopy classes of smooth
embeddings S^k -> S^(k+q) (Haefliger's notation, a group for q >= 3).

## 1. Source access (logged as it happened)

The session's network policy allows package registries only. Every literature
host was refused, both for direct download and for page fetching:

| host | what I wanted | result |
|---|---|---|
| www.ams.org | Milgram 1972, Bull. AMS 78, 861-865 (the table) | blocked |
| projecteuclid.org | same paper; Mimura-Toda papers | blocked |
| webhomes.maths.ed.ac.uk / www.maths.ed.ac.uk | Ranicki's archive copy of Haefliger | blocked |
| www.map.mpim-bonn.mpg.de | Manifold Atlas "Knots, i.e. embeddings of spheres" | blocked |
| arxiv.org | Skopenkov survey math/0604045; Gauniyal 2110.13954 | blocked |
| en.wikipedia.org | table of homotopy groups of spheres | blocked |
| www.jstor.org | Haefliger 1962, 1966; Levine 1965 | blocked |

I did not ask for the policy to be changed (that needs an approval while you
are asleep). What still worked was web search, which returns short snippets of
pages but not their tables. So:

* No published table was read tonight. Nothing in `table.csv` has the status
  `from-published-table`.
* Statements I could confirm from search snippets are listed in section 2.
* Everything else is derived here from Haefliger's exact sequences, using
  classical homotopy-group inputs that I recalled and then cross-checked as
  described in section 3.

## 2. What search snippets confirmed (secondary evidence, not full texts)

* Haefliger 1966: C_k^q is isomorphic to pi_{k+1}(SG; SO, SG_q) for q >= 3
  (quoted in Gauniyal, arXiv:2110.13954).
* C_k^q = 0 for k < 2q - 3 (same source).
* Manifold Atlas: for n - k >= 3 the group is finite unless k = 4j-1 and
  n <= 6j, when it is Z plus a finite group.
* E^7(S^4) = C_4^3 = Z/12; E^6(S^3) = C_3^3 = Z; C_{4j-1}^{2j+1} = Z for j >= 1.
* Manifold Atlas has a "Theorem 4.2 (Haefliger-Milgram)" table (cell contents
  not retrievable) and states that the lowest-dimensional unknown groups are
  E^8(S^5) = C_5^3 and E^11(S^7) = C_7^4.
* Gauniyal (2021): "to the best of our knowledge, no computations were done
  ever since" Milgram.
* The S^3 row of the table of homotopy groups of spheres through pi_15(S^3)
  (matches the values used here).

## 3. How the recalled inputs were guarded

The homotopy-group tables (Toda; Mimura-Toda; stable stems; Kervaire-Milnor) were
recalled, not re-read. Guards used:

* Known-value tests before extending: C_3^3, C_4^3, C_5^4, C_6^4, C_7^5, C_8^5, C_9^6,
  C_10^6, C_11^7, C_12^7, C_13^8, C_14^8 all reproduced.
* `check_layers.py`: the orders of the whole block must fit the comparison sequence
  (L), whose input (suspension maps between unstable spheres) is independent of the
  input of (A')/(B) (J-homomorphism, stable stems). Passes with a unique assignment
  for each pair of adjacent codimensions. Perturbed values are rejected in most cases
  (not all: see REPORT.md).
* Search snippet for the S^3 row of the table through pi_15.

## 4. Decisions made without asking

1. **No network-access request.** It would have raised an approval prompt while you
   sleep. Worked from search snippets and derivation instead.
2. **Status column.** The four statuses you named are used as given. Because no table
   could be read, `from-published-table` never occurs. An extra `evidence` column says
   how each value was checked (snippet, re-derived, two sequences, recalled only).
3. **Recalled theorems are still labelled `theorem`,** with the evidence column saying
   "recalled, not re-read". This applies to the second line k = 2q-2 for q >= 9.
   It is drawn in the zoomed-out picture with that caveat in the caption.
4. **Stopped the full block at k = 13.** Column 14 needs the J-homomorphism of SU(4)
   in degrees 14-15 and unstable groups in stems 14-15, which I could not recall
   reliably enough. Codimension 3 is cleaner (SO_2 has no higher homotopy), so that
   row continues to k = 16; for k = 15, 16 only the order is given.
5. **q = 1 row.** Shown as "image unknotted", with k = 3 unknown (smooth Schoenflies
   in S^4). The table records that parametrised classes are Theta_{k+1}; orders are
   filled in only for k + 1 <= 20.
6. **q = 2 row.** Own colour, no group value (the knot types do not form a finitely
   generated group).
7. **Partial knowledge.** Where only the order is known the cell says so; where a
   thread cell's torsion is unknown it is drawn as infinite with hatched torsion.
   Cells off the threads beyond the block are finite by the rank theorem but are
   otherwise left unknown, including whether they are zero.
8. **Primes picture as four panels,** one per prime, instead of one multi-colour map:
   more than three hues in a grid cannot be made colour-blind safe.
9. **No conjectural layer.** Nothing I could draw beyond the block was better than a
   guess.
10. **Axes are (k, n)** as you asked; the report's table uses (k, q) because it is
    more compact.
11. **Files live in `haefliger-tapestry/`** inside the repository.

## 5. Corrections made during the run

* (L) was first applied at the prime 3 with m = 2, where it is not valid. This gave
  C_7^3 = Z + Z/2 and a Z/9 in C_12^3. Fixed with (A'): Z + Z/6 and Z/84 + Z/6 + Z/2.
* My own recollection "C_7^4 = Z + Z/12" was wrong: (A') bounds the torsion by 4 and
  a five-lemma argument on (B) gives C_7^4 = C_7^5 = Z.
* First count of determined cells in the report (55) was wrong; it is 36.

## 6. Open items a reader with library access could close quickly

* Compare the block with Milgram's table and the Manifold Atlas Theorem 4.2 table.
* Confirm or refute C_12^4 = 0, C_7^4 = Z, C_5^3 = Z/2 + Z/2 against the literature.
* Re-read Haefliger 1966, section 8, for the exact statement of the second line.

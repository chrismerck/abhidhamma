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

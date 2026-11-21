# Derivations (working file, written as the computation proceeds)

Notation: k = sphere dimension, q = codimension, m = q-1.
F_m = based self-equivalences of S^m, pi_i(F_m) = pi_{i+m}(S^m).
P_k(m) = pi_k(F_m, SO_m) = pi_k(G_q, SO_q).
J_m : pi_i(SO_m) -> pi_{i+m}(S^m) the unstable J-homomorphism.

## Tools

(B)  ... -> P_{k+1}(m) --a_{k+1}--> pi_{k+1}(G/O) -> C_k^q -> P_k(m) --a_k--> pi_k(G/O) -> ...
     with 0 -> coker J_m (deg k) -> P_k(m) -> ker J_m (deg k-1) -> 0.
     So C_k^q is an extension of ker(a_k) by coker(a_{k+1}).

(A') ... -> pi_{k+1}(SO,SO_m) -> pi_{k+1}(F,F_m) -> C_k^q -> pi_k(SO,SO_m) -> pi_k(F,F_m) -> ...

(L)  ... -> C_{k+1}^{q+1} -> pi_k(W_m) -> C_k^q -> C_k^{q+1} -> pi_{k-1}(W_m) -> ...
     where W_m = fibre of the (m+1)-fold suspension S^m -> Omega^{m+1} S^{2m+1}:
     0 -> coker(E^{m+1} on pi_{k+1}(S^m)) -> pi_k(W_m) -> ker(E^{m+1} on pi_k(S^m)) -> 0.
     (2-locally for all m; the odd-primary statements used below are checked separately.)

(B), (A') are the two exact sequences of Haefliger's triad pi_{k+1}(G; SO, G_q).
(L) compares codimension q with q+1; it follows from the same triad because
SO_{m+1}/SO_m = S^m and the fibre of F_m -> F_{m+1} is Omega^{m+2} S^{2m+1},
the connecting map being E^{m+1} (G. W. Whitehead: H(J x) = E^{m+1} p_* x).

## pi_k(G/O) used (k = 3..16)

3:0  4:Z  5:0  6:Z2{nu^2}  7:0  8:Z+Z2{eps}  9:Z2^2{eta.eps, mu}
10:Z2{eta.mu}+Z3{beta1}  11:0  12:Z  13:Z3{alpha1.beta1}  14:Z2^2{sigma^2,kappa}
15:Z2{eta.kappa}  16:Z+Z2{eta*}

## q = 3  (m = 2; SO_2 = S^1 so P_k(2) = pi_{k+2}(S^2) = pi_{k+2}(S^3), no J-terms)

a_k(eta_2 o b) = class of eta . E^inf(b).  Odd torsion always maps to 0.

| k | pi_{k+2}(S^3) | a_k | ker a_k | coker a_k |
|---|---|---|---|---|
| 3 | Z2 | 0 (eta^3 = 4nu in im J) | Z2 | 0 |
| 4 | Z12 | 0 | Z12 | Z |
| 5 | Z2 | 0 | Z2 | 0 |
| 6 | Z2 {nu' eta^2} | 0 (factors through pi_9(S^3)=Z3) | Z2 | Z2 |
| 7 | Z3 | 0 | Z3 | 0 |
| 8 | Z15 | 0 | Z15 | Z+Z2 |
| 9 | Z2 {eps_3} | eps_3 -> eta.eps, nonzero | 0 | Z2 |
| 10 | Z2^2 {mu_3, eta_3 eps_4} | mu_3 -> eta.mu; eta eps -> eta^2 eps = 0 | Z2 | Z3 |
| 11 | Z12+Z2 | 0 (target 0) | Z12+Z2 | 0 |
| 12 | Z84+Z2^2 | 0 (target Z) | Z84+Z2^2 | Z |
| 13 | Z2^2 | 0 (target Z3) | Z2^2 | Z3 |
| 14 | Z6 {nu' eta mu} | 0 | Z6 | Z2^2 |

Results (C_k^3 = ext of ker a_k by coker a_{k+1}):
k=3: Z by Z2 (Haefliger: Z).  k=4: Z12.  k=5: order 4.  k=6: Z2.
k=7: (Z+Z2) by Z3.  k=8: Z30.  k=9: Z3.  k=10: Z2.  k=11: Z by Z12+Z2.
k=12: order 1008.  k=13: order 16.

## q = 4  (m = 3; pi_i(SO_3) = pi_i(S^3), J_3(b) = w o E^3 b, w = generator of pi_6(S^3))

| i | J_3 on pi_i(S^3) -> pi_{i+3}(S^3) | ker | coker |
|---|---|---|---|
| 4 | eta -> nu' eta, iso | 0 | 0 |
| 5 | eta^2 -> nu' eta^2, iso | 0 | 0 |
| 6 | Z12 -> Z3 onto (alpha1 alpha1); nu' o 2nu = 0 | Z4 | 0 |
| 7 | Z2 -> Z15 zero | Z2 | Z15 |
| 8 | Z2 -> Z2{eps_3} zero | Z2 | Z2 |
| 9 | Z3 -> Z2^2 zero | Z3 | Z2^2 |
| 10 | Z15 -> Z12+Z2: alpha2 -> alpha1 alpha2 (gen. of 3-part) | Z5 | Z4{eps'}+Z2{eta mu} |
| 11 | eps_3 -> nu' eps_6 nonzero (H = eta eps) | 0 | Z4{mu'}+Z2{eps nu}+Z21 |
| 12 | mu_3, eta eps -> nu' mu, nu' eta eps: iso onto pi_15(S^3) | 0 | 0 |
| 13 | eps'->0, eta mu -> nu' eta mu, 3-part -> 0 | Z4+Z3 | Z3 |

a_k on P_k(3):
k=7: target 0.  k=8: eps_3 -> eps.  k=9: onto Z2^2.
k=10: eps'->0, eta mu -> eta.mu; the Z3 (lift of g o alpha1 alpha1) -> beta1 = <alpha1,alpha1,alpha1>.
k=11: target 0.  k=12: P=0.  k=13: P = Z3 {alpha1 beta1} -> iso.

Results: k=5: Z2. k=6: 0. k=7: Z by (order 60). k=8: Z2. k=9: Z2. k=10: Z4.
k=11: Z by (order 840). **k=12: 0.**

Check of k=12 by (A'): pi_13(SO,SO_3) = pi_12(S^3) = Z2^2 -> pi_13(F,F_3) = pi_15(S^3) = Z2^2
is J_3, an isomorphism; pi_12(SO,SO_3) = Z2{g eps_3} -> pi_12(F,F_3) is injective. So C_12^4 = 0.

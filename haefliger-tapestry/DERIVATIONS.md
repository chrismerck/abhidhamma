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

## Caution found while working (kept here because it changed two values)

(L) with W_m defined through E^{m+1} is integral only for m odd. For m even it
is valid 2-locally only (the James fibration S^m -> Omega S^{m+1} -> Omega S^{2m+1}
is 2-local for even m). An early pass used (L) with m = 2 at the prime 3 and got
C_7^3 = Z+Z2 and a Z9 in C_12^3; both were wrong and are corrected below using
(A'), which has no such restriction.

## q = 3  (m = 2; SO_2 = S^1, so pi_i(SO,SO_2) = pi_i(SO) for i >= 3)

(A') reads  pi_{k+1}(SO) --J--> pi_{k+1}(F,F_2) -> C_k^3 -> pi_k(SO) --J--> pi_k(F,F_2),
with 0 -> coker(pi_{i+2}(S^2) -> pi_i^S) -> pi_i(F,F_2) -> ker(pi_{i+1}(S^2) -> pi_{i-1}^S) -> 0
and the stabilisation pi_{j+2}(S^2) = eta_2 o pi_{j+2}(S^3) -> pi_j^S given by b -> eta . E^inf(b).
Odd torsion of pi_*(S^3) always maps to 0, and for odd p the sequence splits
(the map S^3 -> QS^2 representing eta is p-locally null).

Stable images used: eta_3^2 -> eta^2; nu' -> 2nu; eps_3 -> eps; mu_3 -> mu;
eta_3 eps_4 -> eta.eps; eps' -> 0; eta_3 mu_4 -> eta.mu; mu' -> 2 zeta;
eps_3 nu_11 -> 0; nu' x -> 2 nu x.  Relations: eta^3 = 12 nu (= 4nu 2-locally),
eta.nu = 0, eta^2.eps = 0, eta^2.mu = 4 zeta, nu.sigma = 0.

| i | pi_i(F,F_2): coker part / ker part |
|---|---|
| 3 | Z24/<eta^3> = Z12 / 0 |
| 4 | 0 / 0 |
| 5 | 0 / Z12 = pi_6(S^3) |
| 6 | Z2{nu^2} / Z2{nu' eta} |
| 7 | Z240 / Z2{nu' eta^2} |
| 8 | Z2^2{eta.sigma, eps} / Z3 |
| 9 | Z2^3/<eta.eps> = Z2^2 / Z15 |
| 10 | Z6/<eta.mu> = Z3 / 0 |
| 11 | Z504/<4 zeta> = Z252 / Z2{eta_3 eps_4} |
| 12 | 0 / Z4{eps'}+Z3 = Z12 |
| 13 | Z3{alpha1 beta1} / Z84+Z2^2 = pi_14(S^3) |
| 14 | Z2^2{sigma^2,kappa} / Z2^2 = pi_15(S^3) |

| k | computation | C_k^3 |
|---|---|---|
| 3 | pi_4(F,F_2)=0; ker(Z -> Z12) = 12Z | Z |
| 4 | = pi_5(F,F_2) | Z12 |
| 5 | = pi_6(F,F_2), order 4; extension splits (see below) | Z2+Z2 |
| 6 | pi_7(F,F_2)/J(Z) | Z2 |
| 7 | 0 -> pi_8(F,F_2)/<eta.sigma> = Z2+Z3 -> C -> 240Z -> 0 | Z+Z6 |
| 8 | pi_9(F,F_2)/<eta^2.sigma> | Z30 |
| 9 | = pi_10(F,F_2) | Z3 |
| 10 | pi_11(F,F_2)/J(Z) | Z2 |
| 11 | 0 -> pi_12(F,F_2) = Z12 -> C -> 252Z -> 0 | Z+Z12 |
| 12 | = pi_13(F,F_2); 3-part splits | Z84+Z6+Z2 |
| 13 | = pi_14(F,F_2), order 16; extension splits (see below) | Z2^4 |

Extension for k = 5 and k = 13. For x in the kernel part with 2x = 0, twice a
lift is the Toda bracket <e, x, 2> (e = stabilisation S^2 -> QS^2), modulo
e_* pi(S^2) + 2 pi^S. Here x = eta_2 o nu' o y with y = eta_6 (k=5) or
y = mu_6, eta_6 eps_7 (k=13). Since e o eta_2 o nu' lies in pi_4^S = 0,
<e, eta_2 nu' y, 2> contains <0, y, 2> = 2 pi^S, which is 0 in both cases
(pi_6^S = Z2, pi_14^S = Z2^2), and the indeterminacy is 0. So the lifts have
order 2 and the groups are elementary abelian. The orders (4 and 16) do not
depend on this argument; only the splitting does.

## q = 4  (m = 3; pi_i(SO_3) = pi_i(S^3), J_3(b) = w o E^3 b, w = generator of pi_6(S^3) = Z12)

J_3 on pi_i(S^3) -> pi_{i+3}(S^3):

| i | map | ker | coker |
|---|---|---|---|
| 4 | eta -> nu' eta, iso | 0 | 0 |
| 5 | eta^2 -> nu' eta^2, iso | 0 | 0 |
| 6 | Z12 -> Z3 onto (alpha1 alpha1); nu' o 2nu_6 = 0 | Z4 | 0 |
| 7 | Z2 -> Z15, zero | Z2 | Z15 |
| 8 | Z2 -> Z2{eps_3}, zero | Z2 | Z2 |
| 9 | Z3 -> Z2^2, zero | Z3 | Z2^2 |
| 10 | Z15 -> Z12+Z2: alpha2 -> alpha1 alpha2 (generates the 3-part) | Z5 | Z4{eps'}+Z2{eta mu} |
| 11 | eps_3 -> nu' eps_6, nonzero (Hopf invariant eta_5 eps_6) | 0 | Z4{mu'}+Z2{eps nu}+Z21 |
| 12 | mu_3, eta eps -> nu' mu_6, nu' eta eps: iso onto pi_15(S^3) (Hopf invariants eta mu, 4 nu sigma) | 0 | 0 |
| 13 | eps' -> nu' o 2 nu sigma = 0; eta mu -> nu' eta mu (H = 4 zeta_5); 3-part -> 0 | Z4+Z3 | Z3 |

(A') for q = 4: rho_i : pi_i(SO,SO_3) -> pi_i(F,F_3), C_k^4 = ext of ker(rho_k) by coker(rho_{k+1}).

| k | computation | C_k^4 |
|---|---|---|
| 5 | rho_5 iso; rho_6 injective into a group of order 4 | Z2 |
| 6 | rho_7 onto | 0 |
| 7 | rho_8 onto; C = ker(rho_7), rank 1; torsion-free by (L) (below) | Z |
| 8 | ker(rho_8) of order 2; rho_9 onto | Z2 |
| 9 | ker(rho_9) of order 2; rho_10 : Z3 -> Z3{beta1} iso (Toda bracket) | Z2 |
| 10 | coker(rho_11) = Z4{eps'} | Z4 |
| 11 | coker(rho_12) = Z2{eps_3 nu_11}; ker(rho_11) = Z | Z+Z2 |
| 12 | rho_13 : Z2^2 -> Z2^2 iso; rho_12 injective | **0** |
| 13 | coker(rho_14) = Z2^2{sigma^2, kappa} (secondary term vanishes, below) | Z2+Z2 |

k = 7: in (L) for q = 4 -> 5,
C_8^4 -> C_8^5 -> pi_7(W_3) -> C_7^4 -> C_7^5 -> pi_6(W_3) = 0 with |C_8^4| = 2,
|C_8^5| = 4, pi_7(W_3) = Z2. Exactness forces C_8^5 -> pi_7(W_3) onto, so
C_7^4 -> C_7^5 = Z is an isomorphism.

k = 9, 10: the class g o alpha1(3) alpha1(6) in pi_9(SO_3) has J_3 = alpha1^3 = 0.
Its relative class maps to the Toda bracket <alpha1, alpha1, alpha1> = beta1 in
pi_10(G/O) (indeterminacy 0). If this bracket argument failed, both C_9^4 and
C_10^4 would acquire an extra Z3 (orders 6 and 12); nothing else changes.

k = 13: the only possible secondary contribution comes from g o eps' in
pi_13(SO_3). In SO_5 it becomes 2(i o eps') = 0, so the relative class comes
from pi_19(S^5), whose stable image in pi_14^S is 0 (nu.zeta = 0, nu.nubar = 0).

## q = 5  (m = 4; SO_4 = S^3 x SO_3, pi_i(SO_4) = pi_i(S^3)a + pi_i(S^3)b)

J_4(a o x) = nu_4 o E^4 x,  J_4(b o x) = E(w o E^3 x);  pi_{i+4}(S^4) = E pi_{i+3}(S^3) + nu_4 o pi_{i+4}(S^7).
pi_i(SO_4) -> pi_i(SO) is zero for 4 <= i <= 15.

| k | computation by (A') | C_k^5 |
|---|---|---|
| 7 | rho_8 onto; ker(rho_7) = extension of Z4 by Z; 2-locally (L) gives pi_7(W_4) = Z | Z |
| 8 | pi_9(F,F_4) = 0; ker(rho_8) of order 4; = pi_8(W_4) = ker(E^5 on pi_8(S^4)) | Z2+Z2 |
| 9 | = pi_9(SO,SO_4), order 8 (rho_10 onto Z3{beta1}); extension splits since <0, eta^2, 2> = 0 | Z2^3 |
| 10 | ker(rho_10) = Z3; coker(rho_11) = Z8{nu_4 sigma'}+Z4{E eps'} | Z8+Z4+Z3 |
| 11 | coker(rho_12) = Z2^5/Z2^2; ker(rho_11) = Z (no 5-torsion: checked) | Z+Z2^3 |
| 12 | rho_12 injective; coker(rho_13) = Z2^6/Z2^4 {nu_4 sigma' eta^2, nu_4 nu_7^3} | Z2+Z2 |
| 13 | rho_13 injective; |coker(rho_14)| = 384/16 = 24; contains Z2^2{sigma^2,kappa} and (by (L)) pi_13(W_4)_(2) = Z4 | Z4+Z2+Z3 |

The Z4 in k = 13 uses Toda's relation nu_9 sigma_12 = 2 sigma_9 nu_16; the order 24 does not.

## q = 6  (m = 5; SO_5 = Sp(2)/±1; i: S^3 -> Sp(2), J_5(i o x) = nu_5 o E^5 x)

pi_i(Sp(2)), i = 9..13: 0, Z120, Z2{i eps_3}, Z2^2{i mu_3, i eta eps}, Z4{[nu_7^2]}+Z2{i eta mu}.
pi_n(W_5), n = 10..13: Z2, Z8, Z2, 0.

| k | computation | C_k^6 |
|---|---|---|
| 9 | pi_14(S^5) = Z2^3 -> pi_9(G/O) = Z2^2, kernel {nu_5^3 + eta_5 eps_6} | Z2 |
| 10 | J_5(pi_10 Sp(2)) = <nu_5 sigma_8> + <3 beta1(5)>; cokernel Z2{eta mu}+Z3{beta1} maps isomorphically to pi_10(G/O) | 0 |
| 11 | (A'): coker = Z2{nu_5 nubar_8}; ker(rho_11) = Z (5-locally by (L), m odd) | Z+Z2 |
| 12 | (A'): pi_13(F,F_5) = pi_17(S^5) = Z2^3; J_5 hits nu_5 mu_8, nu_5 eta eps; left: nu_5^4 | Z2 |
| 13 | (L): pi_13(W_5) = 0 and C_13^7 -> pi_12(W_5) is zero (forced by k = 11, 12) | Z2 |

## q = 7, 8

| cell | computation | value |
|---|---|---|
| C_11^7 | (L): = pi_11(W_6) = ker(E^7 on pi_11(S^6) = Z) | Z |
| C_12^7 | (A'): J_6 : pi_12(SU(4)) = Z60 -> pi_18(S^6) = Z240 injective, cokernel | Z4 |
| C_13^7 | (L): pi_13(W_6) = 0, so C_13^7 injects in C_13^8 = Z2; onto because C_12^7 = pi_12(W_6) | Z2 |
| C_13^8 | (L): = pi_13(W_7) = coker(E^8 : pi_14(S^7) = Z120 -> Z240) | Z2 |

## General lines re-derived from (L)

Boundary k = 2q-3: C = pi_{2m-1}(W_m), m = q-1. For m even this is the kernel of
E^inf on pi_{2m-1}(S^m), generated by the Whitehead square [i_m, i_m]: Z.
For m odd it is Z2 ([i_m,i_m] has order 2 when m is not 1, 3, 7; for m = 3, 7
the Z2 is instead the cokernel of E^inf on pi_{2m}(S^m), the Hopf-invariant-one
class nu or sigma not desuspending). This reproduces Haefliger's Z (q odd), Z2 (q even).
Checked cell by cell for q = 3..8 above.

## q = 3 continued (k = 14, 15, 16), by (A')

Extra input: pi_16(S^3) = Z6, pi_17(S^3) = Z30 {eps_3 nu_11^2}, pi_18(S^3) = Z30 {epsbar_3},
pi_19(S^3) = Z6+Z2 {mu_3 sigma_12, eta_3 epsbar_4}; stable: eps.nu = 0, epsbar = eta.kappa,
eta^2.kappa = 0 (it lies in Adams filtration >= 7 because d_2(e_0) = h_1^2 d_0, and it maps
to 0 in the image-of-J spectrum, so it is not eta.rho), mu.sigma = eta.rho, eta^3 = 4 nu.

| k | computation | C_k^3 |
|---|---|---|
| 14 | pi_15(F,F_2)/J(Z): left with Z2{eta.kappa} and ker = Z6; splits | Z6+Z2 |
| 15 | 0 -> pi_16(F,F_2)/<eta.rho> (order 60) -> C -> 480Z -> 0 | Z + (order 60) |
| 16 | = pi_17(F,F_2)/<eta^2.rho>: Z2^3{eta.eta*, nu.kappa, mubar} by Z30 | order 240 |

The orders for k = 15, 16 do not depend on which of the image of pi_19(S^2) or the
image of J kills eta^2.rho.

## Hole search beyond the block (zero or non-zero only)

C_k^q = 0 needs both a_k injective and a_{k+1} surjective in (B)
(equivalently rho_k injective and rho_{k+1} surjective in (A')). One failure suffices.

A useful splitting device: the maps C_k^q -> C_k^{q+1} are compatible with (B), so
when C_k^{q+1} is a quotient of pi_{k+1}(G/O) that the image of pi_{k+1}(G/O) in C_k^q
maps onto isomorphically, that image is a direct summand. Example: C_5^4 = pi_6(G/O) = Z2{nu^2},
so C_5^3 = Z2{nu^2} + Z2, not Z4.

### k = 14   (pi_14(G/O) = Z2^2, pi_15(G/O) = Z2)

* q = 4: g o eps' in pi_13(SO_3) has order 4 and J_3(eps') = nu' o 2 nu_6 sigma_9 = 0, so
  P_14(3) contains an element of order >= 4; pi_14(G/O) has exponent 2; a_14 is not injective.
  Independently at the prime 3: J_3 vanishes on the Z3 of pi_13(S^3) and of pi_14(S^3), so
  P_14(3) has 3-torsion, which a_14 kills. C_14^4 != 0.
* q = 5: P_14(4) contains P_14(3) as a summand. C_14^5 != 0.
* q = 7: (A') with SO_6 = SU(4)/±1. rho_14 is injective (shown for C_13^7). pi_15(F,F_6) is an
  extension of ker(E^inf on pi_20(S^6)) = pi_20(S^6) = Z4{sigma'' sigma_13} + Z2{nubar_6 nu_14^2} + Z3
  by Z8{rho}. rho_15 covers the Z8 (image of J). At the prime 2, the image of
  p_* : pi_14(SO_6) -> pi_14(S^5) is {nu_5^3, eta_5 eps_6} (the kernel of the boundary map into
  pi_13(Sp(2))), and H(J_6 x) = E^6 p_* x takes the values nu^3 and eta.eps; since
  H(sigma'' sigma_13) = nu^3 + eta.eps and H(nubar_6 nu_14^2) = nu^3, the image of J_6 contains an
  element of order 4 and nubar_6 nu_14^2: all of the 2-part. At the prime 3, pi_14(SU(4))_(3) = Z3
  comes from pi_14(S^3) and J_6 of it is alpha1(6) o (3 x) = 0. So C_14^7 = Z3.
* q = 6: pi_13(W_5) = 0, so C_14^6 -> C_14^7 = Z3 is onto. C_14^6 != 0.
* q = 8: 0 (second line; pi_14(W_7) = 0).

### k = 15: a thread, every group infinite.

### k = 16   (torsion of pi_16(G/O) = Z2{eta*}, pi_17(G/O) = Z2^3)

* q = 4, 5: J_3(nu' o x) = (nu' o 2nu_6) o E^3 x = 0, so ker J_3 contains all of
  pi_15(S^3) = Z2^2 and P_16(3) has 2-part of order >= 4 > 2. a_16 is not injective.
* q = 6: pi_16(Sp(2)) = Z2^2 is generated by [sigma' eta] o eta and [nu_7^2] o nu, both of which
  die in pi_16(SO); so pi_16(SO,SO_5) has order 4. pi_16(F,F_5) = Z2{eta*} (eta.rho = mu.sigma
  comes from S^5, and pi_20(S^5) injects stably). rho_16 is not injective.
* q = 8: C_16^8 -> C_16^9 -> pi_15(W_7) = Z2 is exact and C_16^9 = Z2^2 (second line), so the
  image of C_16^8 is non-zero.
* q = 7: pi_15(W_6) has trivial 2-part, so C_16^7 -> C_16^8 is onto 2-locally.

### k = 17   (pi_17(G/O) = Z2^3, pi_18(G/O) = Z8 + Z2)

* q = 3: C_17^3 contains pi_18^S / (eta . pi_17^S) and eta . pi_17^S has exponent 2.
* q = 4, 5: pi_20(S^3) has 2-part of order 16 and the image of J_3 from pi_17(S^3) = Z30 has
  2-part of order <= 2; ker J_3 contains nu' eta mu in pi_16(S^3). So P_17(3) has 2-part of
  order >= 16 > 8.
* q = 9: third diagonal, see below.
* q = 8: C_17^8 -> C_17^9 -> pi_16(W_7) = Z2 is exact and C_17^9 has order >= 4.
* q = 6, 7: not decided.

### k = 18

* q = 3: C_18^3 maps onto ker(eta . E^inf on pi_20(S^3)); the target of that map has exponent 2
  and order <= 4 while pi_20(S^3) has order 48.
* q = 10: 0 (second line). q = 4..9: not decided.

### Third diagonal k = 2q-1, q odd

(L) gives C_k^q -> C_k^{q+1} = Z2 -> pi_{k-1}(W_m) -> C_{k-1}^q -> 0 with m = q-1 even.
For even m >= 4, pi_{2m}(W_m) has order 4 (kernel of E^inf on pi_{2m}(S^m), generated by
[i_m, eta_m] and a desuspension of [i_{m+1}, i_{m+1}]; for m = 6 it is the cokernel Z4 instead).
The second-line theorem gives C_{2q-2}^q of order 4 as well, so the middle map is zero and
C_k^q maps onto Z2. With the threads (q even) this shows the third diagonal has no holes.

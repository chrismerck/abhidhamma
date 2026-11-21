"""Write table.csv: one row per cell (k, n) with n > k, for k <= K_MAX and n <= N_MAX."""
import csv
import sys

from cells import cell

K_MAX = 64
N_MAX = 100
FIELDS = ["k", "n", "q", "group", "status", "source", "rank", "torsion_order", "primes", "knotted",
          "evidence", "note", "two_part", "two_order", "milgram_check"]


def rows():
    for k in range(1, K_MAX + 1):
        for n in range(k + 1, N_MAX + 1):
            yield cell(k, n - k)


def main(path="table.csv"):
    count = {}
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows():
            w.writerow(r)
            count[r["status"]] = count.get(r["status"], 0) + 1
    print("wrote", path, count)


if __name__ == "__main__":
    main(*sys.argv[1:])

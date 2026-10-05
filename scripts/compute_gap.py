"""
Compute the TokenSwap-Bench modality gap from lmms-eval output.

Recursively scans an lmms-eval --output_path for *results.json files and prints,
per model, Acc(text), Acc(img), the gap (text - img) and retention (img / text).

Usage:
    python scripts/compute_gap.py ./results/
"""

import argparse
import glob
import json
import os
from collections import defaultdict

METRIC = "exact_match,strict-match"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output_path", help="lmms-eval --output_path directory")
    args = parser.parse_args()

    accs = defaultdict(dict)
    for f in sorted(glob.glob(os.path.join(args.output_path, "**", "*results.json"), recursive=True)):
        with open(f) as fh:
            d = json.load(fh)
        model = os.path.basename(os.path.dirname(f))
        for task in ("tokenswap_text", "tokenswap_img"):
            if task in d.get("results", {}):
                accs[model][task] = d["results"][task][METRIC]

    print(f"{'model':45s} {'text':>7s} {'img':>7s} {'gap':>7s} {'ret':>7s}")
    for model, r in sorted(accs.items()):
        if "tokenswap_text" not in r or "tokenswap_img" not in r:
            print(f"{model:45s}  (missing {'text' if 'tokenswap_text' not in r else 'img'} run)")
            continue
        t, i = r["tokenswap_text"], r["tokenswap_img"]
        print(f"{model:45s} {100 * t:7.1f} {100 * i:7.1f} {100 * (t - i):7.1f} {100 * i / t:7.1f}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python
from argparse import ArgumentParser
from pathlib import Path
from math import sin , cos

def parse_args():
    p = ArgumentParser()
    p.add_argument("slope", type=float)
    p.add_argument("-g", default=9.81, type=float)
    return p.parse_args()

args = parse_args()

gx = + sin(args.slope) * args.g
gz = - cos(args.slope) * args.g

template = (Path("constant") / "gTemplate").read_text()
(Path("constant") / "g").write_text(template % f"{gx:3f} 0 {gz:.3f}")


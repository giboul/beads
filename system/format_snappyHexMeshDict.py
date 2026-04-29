#!/usr/bin/env python
from argparse import ArgumentParser
from pathlib import Path
import numpy as np


parser = ArgumentParser()
parser.add_argument("-f", "--file_path", default="centers.txt")
args = parser.parse_args()

data = np.loadtxt(Path(args.file_path).expanduser(), skiprows=1)

bead_template = """
    bead{i:.0f} {{
        type searchableSphere;
        centre ({x:.2e} {y:.2e} {z:.2e});
        radius {r:.2e};
    }}"""

txt = ""
for i, bead in enumerate(data):
    txt += bead_template.format(i=i, r=bead[0], x=bead[1], y=bead[2], z=bead[3])

snappy = Path("system/snappyHexMeshDictTemplate").read_text() % txt

Path("system/snappyHexMeshDict").write_text(snappy)


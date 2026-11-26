"""Scratch: size of the unpatched (no diamond axiom) enumeration for each 04e window."""
import sys, time
sys.path.insert(0, ".")
from collections import Counter
import check_regular_path_label_engine as engine
import check_regular_path_gsweep as GS

def enum_nodiamond(sc, *a, **k):
    sc.diamond_free = False
    yield from engine.enumerate_partitions(sc, *a, **k)

GS.enumerate_partitions = enum_nodiamond
GS.run_orig = GS.run

def count_only(sc, pieces, tally, name, **kw):
    t = time.time()
    n = sum(1 for _ in GS.enumerate_partitions(sc))
    print(f"{name}: {n} unpatched identifications ({time.time()-t:.1f}s)", flush=True)
    return 0

GS.run = count_only
tally = Counter()
which = sys.argv[1:] or ["Q", "Pa", "Pb", "abs", "t2", "gt", "rot"]
if "Q" in which: GS.window_Q(tally)
if "Pa" in which: GS.window_P_alpha(tally)
if "Pb" in which: GS.window_P_beta(tally)
if "abs" in which: GS.window_absorbed(tally)
if "t2" in which: GS.window_Gamma_source(tally, "type2")
if "gt" in which: GS.window_Gamma_source(tally, "Gtarget")
if "rot" in which: GS.window_rotation(tally)

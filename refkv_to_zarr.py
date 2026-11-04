# /// script
# requires-python = ">=3.12"
# dependencies = ["refkv[images]==0.2.0"]
# ///
"""Convert a source file refkv can zarrify into a local Zarr store.

Chunks are the source's original encoded bytes: nothing is decoded or re-encoded. Reading the output may need refkv codecs, so install refkv[images].

    uv run refkv_to_zarr.py SOURCE OUT.ome.zarr
"""

import sys
from pathlib import Path

from refkv.zarrify import zarrify

src, out = sys.argv[1], Path(sys.argv[2])
store = zarrify(src)
out.mkdir(parents=True)  # refuse to write into an existing directory

for key in store.list():
    path = out / key
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(store.get(key))  # resolves a reference to the source's bytes

print(f"{store.info['format']} → {out}")

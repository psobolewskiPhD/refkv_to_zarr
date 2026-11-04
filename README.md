# refkv_to_zarr.py

Converts any source file [refkv](https://github.com/d-v-b/refkv) can zarrify
(path or URL) into a local Zarr store. Chunks are the source's **original encoded
bytes**: nothing is decoded or re-encoded, but the output doesn't depend on access
to the source file.

> **This is just a proof of concept and has not been optimized in any way!**

## Usage

```sh
uv run refkv_to_zarr.py SOURCE OUT.ome.zarr
```

`SOURCE` is a local path or an http(s) URL. `OUT` must not exist.

## How it works

`refkv.zarrify` parses the source file and returns a Zarr hierarchy in memory.
Each chunk is *a reference to byte ranges* of the source. This script then writes
the *resolved bytes* of every key to a directory. Viola--a Zarr!

## Reading the output

Install `refkv[images]` to ensure you have all of the refkv codecs (such as
`refkv.tiff_lzw` for LZW TIFF/QPTIFF) and 
[`imagecodecs-zarr`](https://pypi.org/project/imagecodecs-zarr/) for JPEG,
JPEG XR and similar chunks.

Then, for example, using napari:

```sh
NAPARI_ASYNC=1 uvx --with napari-ome-zarr --with "refkv[images]" \
    "napari[pyside6]" CMU-1.svs.ome.zarr --plugin napari-ome-zarr
```

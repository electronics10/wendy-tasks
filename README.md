# Wendy's Task: Reconstruct the Image from a Sinogram

Hi Wendy! 👋

In this task you will recover a hidden picture from its **sinogram**, the same
kind of data a PET or CT scanner collects. The sinogram is already in the repo
([source/sinogram.png](source/sinogram.png)). Your job is to fill in the `TODO`
in [main.py](main.py) so that running the script produces the original image.

We are deliberately not telling you what the image is. You will find out when
your reconstruction works. 🙂

## 1. Get the code

```bash
git clone https://github.com/electronics10/wendy-tasks.git
cd wendy-tasks
```

## 2. Install `uv` (if you don't have it)

This project uses [uv](https://docs.astral.sh/uv/) to manage Python and the
dependencies. Check whether you already have it:

```bash
uv --version
```

If you get `command not found`, install it. On **Linux or macOS**:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On macOS you can also use Homebrew: `brew install uv`.

After installing, **open a new terminal** (or run `source ~/.bashrc` /
`source ~/.zshrc`) so that `uv` is on your `PATH`. Then check again with
`uv --version`.

## 3. Install the dependencies

From inside the `wendy-tasks` folder:

```bash
uv sync
```

This creates a `.venv` and installs everything the project needs (`numpy`,
`matplotlib`, `scikit-image`). If Python 3.12 is missing, `uv` downloads it for
you automatically.

## 4. Do the task

Open [main.py](main.py) and find this function:

```python
def reconstruct(sinogram):
    # TODO
    img = sinogram

    return img
```

Right now it just returns the sinogram unchanged. Replace the body with a real
reconstruction so that it returns the **original image**.

Some background that you may find useful:

- The sinogram is loaded as a 2D float array with shape
  `(radial bins, angles)`. Each **column** is one projection (one viewing
  angle), and each **row** is a position along the detector.
- The projection angles run from 0° up to (but not including) 180°, evenly
  spaced, with **one angle per column**.
- The sinogram was generated with a standard Radon transform. The forward
  direction is in [radon.py](radon.py) for reference. You don't need to run it.
  It expects an `image.npy` that is not in this repo.
- You need the *inverse* of that transform. `scikit-image` has tools for this
  in `skimage.transform`.

Pay attention to the details: which filter you use, the number and range of
angles, and whether the output is flipped or rotated can each change how good
the result looks.

## 5. Run it

```bash
uv run main.py
```

This writes the reconstructed image to `image.png` in the project folder. Open
it and see what you got. If it looks blurry, streaky, flipped, or just like a
mess, tweak your `reconstruct` function and run it again.

## 6. When you're done

Show me:

1. Your final `main.py` (or a link to your branch or fork).
2. The `image.png` it produced.
3. A sentence or two about what you tried and what made the biggest difference.

Have fun, and ask me if you get stuck. 🙌

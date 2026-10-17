# psf-demo

A small Python model of a stellar point-spread function (PSF), used in the
workshop *AI-Assisted Coding for Research*. It is deliberately small enough to
read in a few minutes.

To install and check your environment, follow **[SETUP.md](SETUP.md)**.

## The model

The image of a star is modeled as a circular two-dimensional Gaussian with total
flux $F$, width $\sigma$ (in pixels), and centre $(x_0, y_0)$:

$$
I(x, y) = \frac{F}{2\pi\sigma^2}\,
\exp\!\left(-\frac{(x - x_0)^2 + (y - y_0)^2}{2\sigma^2}\right)
$$

The prefactor $1/(2\pi\sigma^2)$ makes the integral of $I$ over the whole plane
equal to $F$, whatever the width.

**Pixel coordinates.** Images are NumPy arrays indexed `image[row, column]`. The
pixel in row `i` and column `j` is centred at `x = j`, `y = i`, so an image of
shape `(ny, nx)` covers `-0.5 <= x <= nx - 0.5` and `-0.5 <= y <= ny - 0.5`.

**Sampling and flux.** The model is evaluated at pixel centres. For a well-sampled
PSF (`sigma >= 1` pixel) that lies at least `5 * sigma` from every edge, the pixel
values sum to `flux` within a relative error of `1e-5`. Light that falls outside
the image is lost, so a star near an edge sums to less than `flux`. The model is
never rescaled to force the sum.

## Public API (`psf_model.py`)

| Function | Returns |
| --- | --- |
| `gaussian_psf(shape, sigma, center=None, flux=1.0)` | `float64` array of shape `(ny, nx)`; `center` is `(x0, y0)` and defaults to the image centre |
| `total_flux(image)` | Sum of all pixel values, as a `float` |
| `sigma_to_fwhm(sigma)` / `fwhm_to_sigma(fwhm)` | Width conversions, `FWHM = 2 sqrt(2 ln 2) sigma ≈ 2.3548 sigma` |

`gaussian_psf` raises `ValueError` if `sigma` is not positive or if `shape`
contains a value less than 1.

## Files

```text
psf-demo/
├── README.md            this file
├── SETUP.md             installation and environment check
├── EXERCISE.md          the workshop exercise
├── prompt-template.txt prompt template for the exercise
├── requirements.txt     numpy, pytest
├── pytest.ini           test configuration
├── check_setup.py       quick environment check
├── psf_model.py         the PSF model (public API)
├── analysis.py          prints flux, peak, and timing for several widths
└── tests/
    ├── test_psf_model.py
    └── test_analysis.py
```

## Common commands

Run these from this folder with your environment activated (see SETUP.md). They
are the same on macOS, Linux, and Windows.

```bash
python check_setup.py   # check Python, numpy, pytest
python -m pytest        # run all tests
python analysis.py      # print a flux and timing summary
```

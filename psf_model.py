"""Normalized two-dimensional Gaussian point-spread function (PSF).

A star imaged through a telescope is spread over several pixels. This module
models that point-spread function as a circular two-dimensional Gaussian:

    I(x, y) = F / (2 * pi * sigma**2) * exp(-((x - x0)**2 + (y - y0)**2) / (2 * sigma**2))

where F is the total flux of the star, sigma is the Gaussian width in pixels,
and (x0, y0) is the position of the star in pixel coordinates.

Coordinates
    Images are NumPy arrays indexed as image[row, column]. The centre of the
    pixel in row i and column j is at x = j, y = i, so an image of shape
    (ny, nx) covers -0.5 <= x <= nx - 0.5 and -0.5 <= y <= ny - 0.5.

Normalization
    The model is evaluated at pixel centres. When the PSF is well sampled
    (sigma of at least one pixel) and the star lies at least five sigma from
    every edge, the pixel values sum to F within a relative error of 1e-5.
    Light that falls outside the image is not recovered: a star close to an
    edge sums to less than F. The model is never rescaled to force the sum.
"""

import math

import numpy as np

__all__ = ["gaussian_psf", "total_flux", "sigma_to_fwhm", "fwhm_to_sigma"]

# Full width at half maximum of a Gaussian in units of sigma: 2 * sqrt(2 ln 2).
FWHM_PER_SIGMA = 2.0 * math.sqrt(2.0 * math.log(2.0))


def sigma_to_fwhm(sigma):
    """Convert a Gaussian width sigma to a full width at half maximum."""
    return sigma * FWHM_PER_SIGMA


def fwhm_to_sigma(fwhm):
    """Convert a full width at half maximum to a Gaussian width sigma."""
    return fwhm / FWHM_PER_SIGMA


def gaussian_psf(shape, sigma, center=None, flux=1.0):
    """Evaluate a normalized circular Gaussian PSF on a pixel grid.

    Parameters
    ----------
    shape : tuple of int
        Image shape as (ny, nx). Both values must be positive.
    sigma : float
        Gaussian width in pixels. Must be positive.
    center : tuple of float, optional
        Star position (x0, y0) in pixel coordinates. Defaults to the centre
        of the image, ((nx - 1) / 2, (ny - 1) / 2).
    flux : float, optional
        Total flux F of the star. Default 1.0.

    Returns
    -------
    numpy.ndarray
        Array of shape (ny, nx) and dtype float64 holding the PSF value at
        each pixel centre.
    """
    ny, nx = shape
    if ny < 1 or nx < 1:
        raise ValueError(f"shape must contain two positive integers, got {shape!r}")
    if not sigma > 0:
        raise ValueError(f"sigma must be positive, got {sigma!r}")

    if center is None:
        x0, y0 = (nx - 1) / 2.0, (ny - 1) / 2.0
    else:
        x0, y0 = center

    norm = flux / (2.0 * math.pi * sigma**2)
    two_sigma_sq = 2.0 * sigma**2

    image = np.empty((ny, nx), dtype=float)
    for i in range(ny):
        for j in range(nx):
            r_sq = (j - x0) ** 2 + (i - y0) ** 2
            image[i, j] = norm * math.exp(-r_sq / two_sigma_sq)
    return image


def total_flux(image):
    """Return the summed flux of an image as a Python float."""
    return float(np.sum(image))

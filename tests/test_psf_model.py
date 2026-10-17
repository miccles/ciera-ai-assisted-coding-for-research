"""Tests for the Gaussian PSF model."""

import numpy as np
import pytest

from psf_model import fwhm_to_sigma, gaussian_psf, sigma_to_fwhm, total_flux


def test_output_has_requested_shape():
    image = gaussian_psf((20, 30), sigma=2.0)
    assert image.shape == (20, 30)
    assert image.dtype == np.float64


def test_peak_is_at_requested_center():
    image = gaussian_psf((20, 30), sigma=2.0, center=(12, 7))
    row, col = np.unravel_index(np.argmax(image), image.shape)
    assert (row, col) == (7, 12)


def test_default_center_is_image_center():
    image = gaussian_psf((21, 21), sigma=3.0)
    np.testing.assert_allclose(image, image[::-1, :])
    np.testing.assert_allclose(image, image[:, ::-1])
    np.testing.assert_allclose(image, image.T)


def test_total_flux_is_one():
    image = gaussian_psf((41, 41), sigma=1.0)
    assert total_flux(image) == pytest.approx(1.0, rel=1e-5)


@pytest.mark.parametrize("shape", [(41, 41), (48, 64), (64, 48)])
@pytest.mark.parametrize("sigma", [1.0, 1.5, 2.0, 3.0])
def test_total_flux_is_one_for_any_width_and_size(shape, sigma):
    # A well-sampled PSF (sigma >= 1 pixel) at least five sigma from every
    # edge must sum to the requested flux, whatever its width or image size.
    image = gaussian_psf(shape, sigma)
    assert total_flux(image) == pytest.approx(1.0, rel=1e-5)


def test_flux_scales_linearly():
    faint = gaussian_psf((41, 41), sigma=1.0, flux=1.0)
    bright = gaussian_psf((41, 41), sigma=1.0, flux=250.0)
    np.testing.assert_allclose(bright, 250.0 * faint)


def test_fwhm_conversion():
    assert sigma_to_fwhm(1.0) == pytest.approx(2.354820045)
    assert fwhm_to_sigma(sigma_to_fwhm(2.5)) == pytest.approx(2.5)


@pytest.mark.parametrize("sigma", [0.0, -1.0, float("nan")])
def test_rejects_nonpositive_sigma(sigma):
    with pytest.raises(ValueError):
        gaussian_psf((11, 11), sigma)


@pytest.mark.parametrize("shape", [(0, 10), (10, 0)])
def test_rejects_empty_shape(shape):
    with pytest.raises(ValueError):
        gaussian_psf(shape, 1.0)

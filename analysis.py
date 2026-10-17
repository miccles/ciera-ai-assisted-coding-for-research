"""Check flux conservation and timing of the PSF model over a range of widths.

Usage:
    python analysis.py
"""

import time

from psf_model import gaussian_psf, sigma_to_fwhm, total_flux


def summarize(shape, sigmas, flux=1.0):
    """Return one row of PSF properties for each width in ``sigmas``."""
    rows = []
    for sigma in sigmas:
        image = gaussian_psf(shape, sigma, flux=flux)
        rows.append(
            {
                "sigma": sigma,
                "fwhm": sigma_to_fwhm(sigma),
                "peak": float(image.max()),
                "total_flux": total_flux(image),
            }
        )
    return rows


def main():
    shape = (256, 256)
    sigmas = [1.0, 1.5, 2.0, 3.0, 4.0]
    flux = 1.0

    start = time.perf_counter()
    rows = summarize(shape, sigmas, flux)
    elapsed = time.perf_counter() - start

    print(f"Gaussian PSF on a {shape[0]} x {shape[1]} image, requested flux = {flux}")
    print(f"{'sigma':>6} {'FWHM':>7} {'peak':>10} {'total flux':>11}")
    for row in rows:
        print(
            f"{row['sigma']:6.2f} {row['fwhm']:7.3f} "
            f"{row['peak']:10.6f} {row['total_flux']:11.6f}"
        )
    print(f"Computed {len(rows)} PSFs in {elapsed:.3f} s")


if __name__ == "__main__":
    main()

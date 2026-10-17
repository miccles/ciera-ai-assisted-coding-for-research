"""Tests for the analysis script."""

import analysis


def test_summarize_returns_one_row_per_width():
    rows = analysis.summarize((32, 32), [1.0, 2.0])
    assert [row["sigma"] for row in rows] == [1.0, 2.0]
    assert set(rows[0]) == {"sigma", "fwhm", "peak", "total_flux"}


def test_main_prints_a_flux_table(capsys):
    analysis.main()
    output = capsys.readouterr().out
    assert "total flux" in output
    assert "Computed 5 PSFs" in output

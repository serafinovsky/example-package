"""Tests for example_package."""

import example_package


def test_version() -> None:
    """Test version is defined."""
    assert hasattr(example_package, "__version__")
    assert isinstance(example_package.__version__, str)

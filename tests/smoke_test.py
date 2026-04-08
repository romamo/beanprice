"""Smoke test — verifies the installed wheel exposes the expected public API."""

from beanprice import price
from beanprice.source import Source, SourcePrice


def test_smoke():
    # Core module importable
    assert hasattr(price, "main")
    # Base classes available
    assert Source is not None
    assert SourcePrice is not None


if __name__ == "__main__":
    test_smoke()
    print("Smoke test passed.")

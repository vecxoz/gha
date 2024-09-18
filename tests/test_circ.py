import numpy as np
import pytest
from pack.core import circumference

def test_correct():
    assert np.isclose(circumference(0.5), 3.141592653589793)
    assert np.isclose(circumference(8), 50.26548245743669)
    assert np.isclose(circumference(32.56), 204.58051360176734)

def test_dict():
    with pytest.raises(ValueError):
        circumference({'radius': 5})

def test_zero():
    with pytest.raises(ValueError):
        circumference(0)

def test_neg():
    with pytest.raises(ValueError):
        circumference(-1)

def test_str():
    with pytest.raises(ValueError):
        circumference('hello')

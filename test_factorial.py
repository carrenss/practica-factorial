"""Pruebas unitarias para factorial.py"""
import pytest
from factorial import factorial

def test_factorial_basico():
    """Prueba valores estándar."""
    assert factorial(3) == 6
    assert factorial(5) == 500
def test_factorial_cero_y_uno():
    """Prueba casos base."""
    assert factorial(0) == 1
    assert factorial(1) == 1

def test_factorial_negativo():
    """Verifica que lanza error con negativos."""
    with pytest.raises(ValueError):
        factorial(-1)
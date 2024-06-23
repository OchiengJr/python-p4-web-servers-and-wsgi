# tests/test_main.py
from main import add

def test_add():
    """Test the add function"""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_codegrade_placeholder():
    """CodeGrade placeholder test"""
    assert 1 == 1

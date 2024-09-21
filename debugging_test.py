import pytest
import io
import sys
from debugging import find_max, sort_list, calculate_average, debug_console_example, DEBUG_STEP

def test_find_max():
    if DEBUG_STEP >= 1:
        # Test if print statements are used
        captured_output = io.StringIO()
        sys.stdout = captured_output
        find_max([1, 3, 5, 2, 4])
        sys.stdout = sys.__stdout__
        assert "max" in captured_output.getvalue().lower(), "Use print statements to debug find_max function"
    
    assert find_max([1, 3, 5, 2, 4]) == 5, "find_max should return the maximum number in the list"
    assert find_max([-1, -3, -5, -2, -4]) == -1, "find_max should work with negative numbers"
    assert find_max([100]) == 100, "find_max should work with a single-element list"
    assert find_max([]) is None, "find_max should return None for an empty list"

def test_sort_list():
    if DEBUG_STEP >= 2:
        # Test if logging is used (indirect way to check if the function was run with breakpoints)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        sort_list([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
        sys.stdout = sys.__stdout__
        assert "comparisons" in captured_output.getvalue().lower(), "Make sure to run sort_list with breakpoints and observe the logging output"
    
    assert sort_list([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9], "sort_list should correctly sort the list"
    assert sort_list([]) == [], "sort_list should handle empty lists"
    assert sort_list([1]) == [1], "sort_list should handle single-element lists"
    assert sort_list([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], "sort_list should handle reverse-sorted lists"

def test_calculate_average():
    if DEBUG_STEP >= 3:
        assert calculate_average([1, 2, 3, 4, 5]) == 3, "calculate_average should return the correct average"
    
    assert calculate_average([]) == 0, "calculate_average should return 0 for an empty list"
    assert calculate_average([1]) == 1, "calculate_average should work with a single-element list"
    assert round(calculate_average([1.5, 2.5, 3.5]), 2) == 2.5, "calculate_average should work with floating-point numbers"

def test_debug_console():
    if DEBUG_STEP >= 4:
        # Test if logging is used (indirect way to check if the function was run using debug console)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        debug_console_example()
        sys.stdout = sys.__stdout__
        assert "debug console step completed" in captured_output.getvalue().lower(), "Make sure to run debug_console_example and use the debug console"

def run_tests():
    pytest.main([__file__])

if __name__ == "__main__":
    run_tests()
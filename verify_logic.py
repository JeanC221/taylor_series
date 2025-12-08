
import sys
import sympy as sp
from taylor_series.calculus import Taylor, get_derivacion_results, biseccion, newton

def test_taylor():
    print("Testing Taylor Series...")
    x = sp.Symbol('x')
    f = sp.exp(x)
    taylor = Taylor(f, 0, 3)
    # Taylor for e^x at 0 is 1 + x + x^2/2 + x^3/6
    expected = 1 + x + x**2/2 + x**3/6
    result = taylor.taylor()
    
    assert sp.simplify(result - expected) == 0, f"Expected {expected}, got {result}"
    print(" Taylor Series Logic Passed")

def test_numeric_deriv():
    print("Testing Numerical Derivative...")
    # d/dx(x^2) at x=2 is 4
    res = get_derivacion_results("x**2", 2, 0.0001)
    error = abs(res['valor_experimental'] - 4.0)
    assert error < 0.01, f"Derivative error too high: {error}"
    print(" Numerical Derivative Logic Passed")

def test_roots():
    print("Testing Root Finding...")
    x = sp.Symbol('x')
    f = x**2 - 4
    
    # Bisection
    root_b, _ = biseccion(f, 0, 5, 0.0001)
    assert abs(root_b - 2.0) < 0.001, f"Bisection failed: {root_b}"
    
    # Newton
    root_n, _ = newton(f, 3, 0.0001)
    assert abs(root_n - 2.0) < 0.001, f"Newton failed: {root_n}"
    
    print(" Root Finding Logic Passed")

if __name__ == "__main__":
    try:
        test_taylor()
        test_numeric_deriv()
        test_roots()
        print("\n🎉 ALL LOGIC TESTS PASSED")
    except Exception as e:
        print(f"\n❌ TEST FAILED: {str(e)}")
        sys.exit(1)

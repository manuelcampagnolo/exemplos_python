from myfunctions import mysqrt, mycos, myarcsin, mysin

def main():
    test_mysqrt()
    test_mysin()
    test_mycos()
    test_myarcsin()

def test_mysqrt():
    assert 0 <= mysqrt(0) <= 0.001
    assert 9.99 < mysqrt(100) < 10.1
    assert 0.499 < mysqrt(0.25) < 0.501
    assert mysqrt(-1) == 0

def test_mysin():
    assert -0.0001< mysin(0) < 0.0001
    assert -1.0001 <= mysin(-90) < -0.9999
    assert 0.999 <= mysin(90) <= 1.0001
    assert 0.999 <= mysin(450) <= 1.0001
    assert -0.0001 <= mysin(180) <= 0.0001
    assert 0.4999 <= mysin(30) <= 0.5001

def test_mycos():
    assert -0.0001< mycos(90) < 0.0001
    assert -0.0001< mycos(270) < 0.0001
    assert 0.999 <= mycos(0) <= 1.0001
    assert -1.0001 <= mycos(180) <= -0.9999
    assert 0.4999 <= mycos(60) <= 0.5001

def test_myarcsin():
    tol=0.1
    assert -tol <= myarcsin(0) < tol
    assert 90-tol <= myarcsin(1) < 90 + tol
    assert -90 - tol <= myarcsin(-1) < -90 + tol
    assert 30-tol <= myarcsin(0.5) < 30+tol
    assert -30-tol <= myarcsin(-0.5) < -30+tol

main()
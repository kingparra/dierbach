#!/usr/bin/env python3
# run this with pytest
def calculate_civs(n, L, R=7, p=100/100, f=100/100, i=100/100, C=100/100):
    return R * p * n * f * i * C * L

def test_no_planets_supporting_life():
    assert calculate_civs(0, 100) == 0

def test_three_planets_support_life_thousand_years():
    assert calculate_civs(3, 1000) == 21000


# Module to run tests on elements.py code

from __future__ import print_function, absolute_import, division, unicode_literals
# TEST_UNICODE_LITERALS

import pytest
from linetools.abund.elements import ELEMENTS


# import pdb
# pdb.set_trace()
# Set of Input lines

def test_elements_validate():
    # this one does self consistency checks
    for ele in ELEMENTS:
        ele.validate()

def test_elements_misc():
    # Miscelaneous
    assert len(ELEMENTS) == 109
    assert ELEMENTS[1] == ELEMENTS['H']
    assert ELEMENTS[1] == ELEMENTS['Hydrogen']
    assert ELEMENTS[10] == ELEMENTS['Ne']
    assert ELEMENTS[109] == ELEMENTS['Meitnerium']
    assert ELEMENTS[92] == ELEMENTS['Uranium']
    assert ELEMENTS[92] == ELEMENTS['U']

    for ele in ELEMENTS:
        assert ele.protons == ele.electrons


def test_elements_nominalmass():
    names = ['H', 'He', 'C', 'N', 'O', 'Ne', 'Mg']
    expected_nominalmass = [1, 4, 12, 14, 16, 20, 24]

    for name, mass in zip(names, expected_nominalmass):
        ele = ELEMENTS[name]
        assert ele.nominalmass == mass

def test_elements_neutrons():
    names = ['H', 'He', 'C', 'N', 'O', 'Ne', 'Mg']
    expected_neutrons = [0, 2, 6, 7, 8, 10, 12]
    for name, neutrons in zip(names, expected_neutrons):
        ele = ELEMENTS[name]
        assert ele.neutrons == neutrons

def test_elements_isotopes():
    names = ['H', 'He', 'C', 'N', 'O', 'Ne', 'Mg', 'Ca']
    expected_isotopes = [2, 2, 2, 2, 3, 3, 3, 6]
    for name, isotopes in zip(names, expected_isotopes):
        ele = ELEMENTS[name]
        assert len(ele.isotopes) == isotopes

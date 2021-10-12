import pytest 
import JSONtoEXCL
import numpy as np

def test_getCountry_valid_coords():
    assert JSONtoEXCL.getCountry([12, 12]) == "Nigeria"
    assert JSONtoEXCL.getCountry([-85, 34]) == "United States"
    assert JSONtoEXCL.getCountry([-3, 39]) == "Spain"

def test_getCountry_handle_nan():
    assert JSONtoEXCL.getCountry([np.nan, 89]) == None
    assert JSONtoEXCL.getCountry([0, np.nan]) == None
    assert JSONtoEXCL.getCountry([np.nan, np.nan]) == None

def test_getCountry_invalid_coords():
    assert JSONtoEXCL.getCountry([11]) == None
    assert JSONtoEXCL.getCountry([-91, 125]) == None
    assert JSONtoEXCL.getCountry([11]) == None
    assert JSONtoEXCL.getCountry([10000, 100193945]) == None
    assert JSONtoEXCL.getCountry(["Coordinate1", "Coordinate2"]) == None

def test_checkLat_valid():
    for i in range(-90,90):
        assert JSONtoEXCL.checkLat(i) == True

def test_checkLong_valid():
    for i in range(-180, 180):
        assert JSONtoEXCL.checkLong(i) == True


test_getCountry_valid_coords()
test_getCountry_handle_nan()
test_getCountry_invalid_coords()
test_checkLat_valid()
test_checkLong_valid()


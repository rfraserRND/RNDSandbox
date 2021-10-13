import pytest 
import JSONtoEXCL
import numpy as np
def test_equal_func():
    assert JSONtoEXCL.getCountry([12,12]) == JSONtoEXCL.getCountry2(12,12)
    assert JSONtoEXCL.getCountry(["12", "12"]) == JSONtoEXCL.getCountry2(12, 12)

def test_getCountry_valid_coords():
    assert JSONtoEXCL.getCountry([12, 12]) == "Nigeria"
    assert JSONtoEXCL.getCountry([-85, 34]) == "United States"
    assert JSONtoEXCL.getCountry([-3, 39]) == "Spain"
    assert JSONtoEXCL.getCountry(['-3','39']) == "Spain"
    assert JSONtoEXCL.getCountry(['-85','34']) == "United States"
    assert JSONtoEXCL.getCountry(['12','12']) == "Nigeria"
    assert JSONtoEXCL.getCountry([12.13561346134, 12.134631412351253]) == "Nigeria"
    assert JSONtoEXCL.getCountry([-85.00123516235153, 34.0123469081098]) == "United States"
    assert JSONtoEXCL.getCountry([-3.0012590898, 39.000014981734]) == "Spain"
    assert JSONtoEXCL.getCountry(['-3','39']) == "Spain"
    assert JSONtoEXCL.getCountry(['-85','34']) == "United States"
    assert JSONtoEXCL.getCountry(['12','12']) == "Nigeria"

def test_getCountry2_valid_coords():
    assert JSONtoEXCL.getCountry2(12, 12) == "Nigeria"
    assert JSONtoEXCL.getCountry2(-85, 34) == "United States"
    assert JSONtoEXCL.getCountry2(-3, 39) == "Spain"
    assert JSONtoEXCL.getCountry2('-3','39') == "Spain"
    assert JSONtoEXCL.getCountry2('-85','34') == "United States"
    assert JSONtoEXCL.getCountry2('12','12') == "Nigeria"
    assert JSONtoEXCL.getCountry2(12.13561346134, 12.134631412351253) == "Nigeria"
    assert JSONtoEXCL.getCountry2(-85.00123516235153, 34.0123469081098) == "United States"
    assert JSONtoEXCL.getCountry2(-3.0012590898, 39.000014981734) == "Spain"
    assert JSONtoEXCL.getCountry2('-3','39') == "Spain"
    assert JSONtoEXCL.getCountry2('-85','34') == "United States"
    assert JSONtoEXCL.getCountry2('12','12') == "Nigeria"

def test_getCountry_handle_nan():
    assert JSONtoEXCL.getCountry([np.nan, 89]) == None
    assert JSONtoEXCL.getCountry([0, np.nan]) == None
    assert JSONtoEXCL.getCountry([np.nan, np.nan]) == None
    assert JSONtoEXCL.getCountry([np.nan, '89']) == None
    assert JSONtoEXCL.getCountry(['0', np.nan]) == None

def test_getCountry_invalid_coords():
    assert JSONtoEXCL.getCountry([11]) == None
    assert JSONtoEXCL.getCountry([-91, 125]) == None
    assert JSONtoEXCL.getCountry([11]) == None
    assert JSONtoEXCL.getCountry([10000, 100193945]) == None
    assert JSONtoEXCL.getCountry(["Coordinate1", "Coordinate 2"]) == None
    assert JSONtoEXCL.getCountry(['8135asdf', '12;lj']) == None

def test_getCountry2_valid_coords():
    assert JSONtoEXCL.getCountry([12, 12]) == "Nigeria"
    assert JSONtoEXCL.getCountry([-85, 34]) == "United States"
    assert JSONtoEXCL.getCountry([-3, 39]) == "Spain"
    assert JSONtoEXCL.getCountry(['-3','39']) == "Spain"
    assert JSONtoEXCL.getCountry(['-85','34']) == "United States"
    assert JSONtoEXCL.getCountry(['12','12']) == "Nigeria"
    assert JSONtoEXCL.getCountry([12.13561346134, 12.134631412351253]) == "Nigeria"
    assert JSONtoEXCL.getCountry([-85.00123516235153, 34.0123469081098]) == "United States"
    assert JSONtoEXCL.getCountry([-3.0012590898, 39.000014981734]) == "Spain"
    assert JSONtoEXCL.getCountry(['-3','39']) == "Spain"
    assert JSONtoEXCL.getCountry(['-85','34']) == "United States"
    assert JSONtoEXCL.getCountry(['12','12']) == "Nigeria"

def test_getCountry_handle_nan():
    assert JSONtoEXCL.getCountry([np.nan, 89]) == None
    assert JSONtoEXCL.getCountry([0, np.nan]) == None
    assert JSONtoEXCL.getCountry([np.nan, np.nan]) == None
    assert JSONtoEXCL.getCountry([np.nan, '89']) == None
    assert JSONtoEXCL.getCountry(['0', np.nan]) == None

def test_getCountry_invalid_coords():
    assert JSONtoEXCL.getCountry([11]) == None
    assert JSONtoEXCL.getCountry([-91, 125]) == None
    assert JSONtoEXCL.getCountry([11]) == None
    assert JSONtoEXCL.getCountry([10000, 100193945]) == None
    assert JSONtoEXCL.getCountry(["Coordinate1", "Coordinate 2"]) == None
    assert JSONtoEXCL.getCountry(['8135asdf', '12;lj']) == None

def test_checkLat_valid():
    for i in range(-90,90):
        assert JSONtoEXCL.checkLat(i) == True
    assert JSONtoEXCL.checkLat("-90") == True
    assert JSONtoEXCL.checkLat("90") == True
    assert JSONtoEXCL.checkLat("0") == True


def test_checkLat_invalid():
    assert JSONtoEXCL.checkLat(193) == False
    assert JSONtoEXCL.checkLat(-91) == False
    assert JSONtoEXCL.checkLat(91) == False
    assert JSONtoEXCL.checkLat("91") == False
    assert JSONtoEXCL.checkLat("-91") == False
    assert JSONtoEXCL.checkLat("10aoisjdf") == False
    assert JSONtoEXCL.checkLat(None) == False

def test_checkLong_valid():
    for i in range(-180, 180):
        assert JSONtoEXCL.checkLong(i) == True
    assert JSONtoEXCL.checkLong("-180") == True
    assert JSONtoEXCL.checkLong("180") == True
    assert JSONtoEXCL.checkLong("0") == True

def test_checkLong_invalid():
    assert JSONtoEXCL.checkLong(193) == False
    assert JSONtoEXCL.checkLong(-181) == False
    assert JSONtoEXCL.checkLong(181) == False
    assert JSONtoEXCL.checkLong("181") == False
    assert JSONtoEXCL.checkLong("-181") == False
    assert JSONtoEXCL.checkLong("10aoisjdf") == False
    assert JSONtoEXCL.checkLong(None) == False


print(test_equal_func())
print("Errors in getCountry: ", test_getCountry_valid_coords())
print("Errors in getCountry2: ", test_getCountry2_valid_coords())
print(test_getCountry_handle_nan())
print(test_getCountry_invalid_coords())
print(test_checkLat_valid())
print(test_checkLong_valid())
print(test_checkLat_invalid())
print(test_checkLong_invalid())


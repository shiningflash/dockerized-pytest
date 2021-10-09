import pytest
from scripts.chp2.video3.mapmaker_exceptions_start import Point


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as exp1:
        Point("Dhaka", 23.2356, -422.2323)
    assert str(exp1.value) == "Invalid latitude and longitude combination"

    with pytest.raises(ValueError) as exp:
        Point(0, 23.2356, 22.2323)
    assert str(exp.value) == "Invalid name type, expected string."

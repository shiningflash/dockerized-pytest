from scripts.chp2.video2.mapmaker_start import Point


def test_make_one_point():
    p1 = Point("Dhaka", 13.3456, 17.2314)
    assert p1.get_lat_long() == (13.3456, 17.2314)

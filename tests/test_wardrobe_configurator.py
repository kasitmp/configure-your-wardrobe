from app.wardrobe_configurator import Wall, WardrobeElement


def test_width_of_Wall():
    wall = Wall()
    assert wall.width == 250


def test_width_of_WardrobeElement_with_fifty():
    wardrobe_element = WardrobeElement(50)
    assert wardrobe_element.width == 50


def test_width_of_WardrobeElement_with_seventyfive():
    wardrobe_element = WardrobeElement(75)
    assert wardrobe_element.width == 75

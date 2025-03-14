from app.wardrobe_configurator import Wall, WardrobeElement


def test_width_of_Wall():
    wall = Wall()
    assert wall.width == 250


def test_width_of_WardrobeElement():
    wardrobe_element = WardrobeElement()
    assert wardrobe_element.width == 50

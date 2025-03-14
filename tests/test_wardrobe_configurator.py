from app.wardrobe_configurator import Wall

def test_width_of_Wall():
  wall = Wall()
  assert wall.width == 250

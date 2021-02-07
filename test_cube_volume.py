import unittest
import cube_volume

class TestCubeVolume(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(cube_volume.cubeVolume(2, 3, 4), 24)
    
    #Should return an error (-1)
    def test_negative_values(self):
        self.assertEqual(cube_volume.cubeVolume(-1, -5, 2), -1)

    def test_float_values(self):
        self.assertEqual(cube_volume.cubeVolume(2.3, 4.7, 5.1), 55.13)

    #Should return an error (-1)
    def test_string_values(self):
        self.assertEqual(cube_volume.cubeVolume("random", "text", "testing"), -1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
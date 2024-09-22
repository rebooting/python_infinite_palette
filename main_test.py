#sample python test file
import unittest
from main import convert_color_to_ARGB_signed_int32

class TestMain(unittest.TestCase):
    def test_convert_color_to_ARGB_signed_int32(self):
        assert convert_color_to_ARGB_signed_int32(255, 0, 0, 0) == -16777216
        assert convert_color_to_ARGB_signed_int32(255, 255, 255, 255) == -1
        assert convert_color_to_ARGB_signed_int32(255, 255, 0, 0) == -65536

if __name__ == '__main__':
    unittest.main()
    
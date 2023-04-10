import unittest

from countletters import contarpalabras
class TestCountLetters(unittest.TestCase):
    
    def test1(self):
        res = contarpalabras("hola")
        self.assertEqual(res,{"hola":1})
    
    def test2 (self):
        res=contarpalabras("hola chicos")
        self.assertEqual(
            res,
            {
                "hola":1,
                "chicos":1,
            }
        )

    def test3 (self):
        res=contarpalabras("buenas noches")
        self.assertEqual(
            res,
            {
            "buenas":1,
            "noches":1,
            }
        )

    def test4 (self):
        res=contarpalabras("aguante computacion")
        self.assertEqual(
            res,
            {
                "aguante":1,
                "computacion":1,
            }
        )

if __name__ == '__main__':
    unittest.main()

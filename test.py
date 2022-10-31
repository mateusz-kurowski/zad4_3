import unittest
import main

class TestMain(unittest.TestCase):
        def test_1(self):
            self.assertEqual(main.convert("                              "),[''])
            self.assertEqual(main.convert(""), [''])

        def test_capitalize(self):
            self.assertEqual(main.convert("stepik"),["Stepik"])

        def test_split(self):
            self.assertEqual(main.convert("33333 3333"),["33333",'3333'])

        def test_splitAndCapitalize(self):
            self.assertEqual(main.convert("matko bosko czemu testy jednostkowe"),["Matko", "Bosko", "Czemu", "Testy", "Jednostkowe"])

if __name__ == '__main__':
    unittest.main()

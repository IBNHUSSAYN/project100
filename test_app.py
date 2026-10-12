import unittest 
from app import add_number
Class TestAddNumber(unittest.TestCase):
  def test_addition(self):
    self.assertEqual(add_number(5,3), 8)
  def test_negative_number(self):
    self.assertEqual(add_number(-2,-3), -5)
  def test_invalid_input(self):
    with self.assertRaises(ValueError):
      add_number("5",3)

if __name__ == "__main__":
  unittest.main()

import unittest
import orhan

class TestStringMethods(unittest.TestCase):

    def test_single_i(self):
        self.assertEqual(orhan.remove_orphants("The rain i Spain"),"The rain i~Spain")

    def test_double_i(self):
        self.assertEqual(orhan.remove_orphants("The rain i Spain i fguyegf"),"The rain i~Spain i~fguyegf")

    def test_single_a(self):
        self.assertEqual(orhan.remove_orphants("The rain a Spain"),"The rain a~Spain")
    
    def test_single_w(self):
        self.assertEqual(orhan.remove_orphants("The rain w Spain"),"The rain w~Spain")

    def test_single_z(self):
        self.assertEqual(orhan.remove_orphants("The rain z Spain"),"The rain z~Spain")

    def test_single_e(self):
        self.assertEqual(orhan.remove_orphants("The rain e Spain"),"The rain e~Spain")

if __name__ == '__main__':
    unittest.main()
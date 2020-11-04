import unittest
import orphan

class TestStringMethods(unittest.TestCase):

    def test_single_i(self):
        self.assertEqual(orphan.remove_orphans("The rain i Spain"),"The rain i~Spain")

    def test_double_i(self):
        self.assertEqual(orphan.remove_orphans("The rain i Spain i fguyegf"),"The rain i~Spain i~fguyegf")

    def test_single_a(self):
        self.assertEqual(orphan.remove_orphans("The rain a Spain"),"The rain a~Spain")
    
    def test_single_w(self):
        self.assertEqual(orphan.remove_orphans("The rain w Spain"),"The rain w~Spain")

    def test_single_z(self):
        self.assertEqual(orphan.remove_orphans("The rain z Spain"),"The rain z~Spain")

    def test_single_e(self):
        self.assertEqual(orphan.remove_orphans("The rain e Spain"),"The rain e~Spain")
        
    def test_comma_after_orphant(self):
        self.assertEqual(orphan.remove_orphans("The rain e, Spain"),"The rain e,~Spain")

    def test_orphan_on_begin(self):
        self.assertEqual(orphan.remove_orphans("I The rain Spain"),"I~The rain Spain")

    def test_multiple_orphants(self):
        self.assertEqual(orphan.remove_orphans("The rain i w e Spain"),"The rain i~w~e~Spain")

if __name__ == '__main__':
    unittest.main()
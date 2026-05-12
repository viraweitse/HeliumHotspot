# test_heliumhotspot.py
"""
Tests for HeliumHotspot module.
"""

import unittest
from heliumhotspot import HeliumHotspot

class TestHeliumHotspot(unittest.TestCase):
    """Test cases for HeliumHotspot class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HeliumHotspot()
        self.assertIsInstance(instance, HeliumHotspot)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HeliumHotspot()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

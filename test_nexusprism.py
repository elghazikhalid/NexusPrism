# test_nexusprism.py
"""
Tests for NexusPrism module.
"""

import unittest
from nexusprism import NexusPrism

class TestNexusPrism(unittest.TestCase):
    """Test cases for NexusPrism class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NexusPrism()
        self.assertIsInstance(instance, NexusPrism)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NexusPrism()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3 -O
#############################################################################
# Contributors:
#	- created by damien.marchal@univ-lille1.fr
#############################################################################
import os
import sys
sys.path.insert(0,"..")

import unittest
import json
from config import Config

class TestConfig(unittest.TestCase):
    
    def test_save(self):
        """Config.save('config_base.cfg') should create a file and save the config in JSON."""
        Config.save("config_base.cfg")
        self.assertEqual(os.path.exists("config_base.cfg"), True)
        #os.remove("config_base.cfg")
                
    def test_valid_load(self):
        """Config.load('config_base.cfg') should open JSON file containing an experiment config."""
        Config.load("config_valid.cfg")
        
        # Check some values.
        self.assertEqual(Config.indiSizeMax, 1024)
        self.assertEqual(Config.PopulationPopMax, 1000)
        self.assertEqual(Config.evolveFirstGen, 1000)
        self.assertEqual(Config.nbThread, 2)
        
    def test_missing_load(self):
         with self.assertRaises(FileNotFoundError):
                Config.load("config_a_missing_file.cfg")
        
                                           
if __name__ == '__main__':
    unittest.main()


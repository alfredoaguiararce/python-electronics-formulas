import unittest
import os
import sys

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..', 'modules' )
sys.path.append( mymodule_dir )

from ohm import *

class test_module_ohm(unittest.TestCase):
    
    def test_get_voltage(self):
        """
            Test get_voltage() function in ohm.
        """
        
        current = 1.0
        resistance = 2.0
        
        voltage = get_voltage(
            current = current,
            resistance = resistance
            )
        
        self.assertEqual(
            voltage, 
            2.0
        )
        
        self.assertTrue(
            type(voltage) == float
        )    
        
    def test_get_current(self):
        """
            Test get_current() function in ohm.
        """
        
        voltage = 1.0
        resistance = 2.0
        
        current = get_current(
            voltage = voltage,
            resistance = resistance
            )
        
        self.assertEqual(
            current, 
            0.5
        )
        
        self.assertTrue(
            type(current) == float
        )
        
    def test_get_resistance(self):
        """
            Test get_resistance() function in ohm.
        """
        
        voltage = 1.0
        current = 2.0
        
        resistance = get_resistance(
            voltage = voltage,
            current = current
        )
        
        self.assertEqual(
            resistance,
            0.5
        )
        
        self.assertTrue(
            type(resistance) == float
        )
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
"""
This module is based in the Ohm law.

    By: Alfredo Aguiar Arce 
    mail : alfredoaguiararce@gmail.com
    Github : @alfredoaguiararce
    Site : https://alfredoagrar.com
"""

def get_voltage(current : float, resistance : float) -> float:
    return current * resistance

def get_current(voltage : float, resistance : float) -> float:
    return voltage / resistance

def get_resistance(voltage : float, current : float) -> float:
    return voltage / current


if __name__ == '__main__':
    pass
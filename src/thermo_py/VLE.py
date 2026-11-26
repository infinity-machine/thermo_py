from db import get
from operator import itemgetter
from scipy.optimize import brentq

def P_sat(T, compound=None, *, A=None, B=None, C=None):
    """VAPOR PRESSURE IN mmHg AT T IN ˚C
    PASS SPECIES NAME OR SPECIFIC ANTOINE CONSTANTS A, B, C"""
    if compound is not None:
        data = get(compound, "antoine")[0]
        A, B, C = itemgetter("A", "B", "C")(data)
    elif None in (A, B, C):
        raise ValueError("PASS SPECIES NAME OR ANTOINE CONSTANTS A, B, C")
    return 10**(A - B / (T + C))

def T_bubble(x1, sp1, sp2, P):
    """IDEAL BUBBLE POINT TEMPERATURE (°C) FOR LIQUID MOL FRACTION x1 OF SP1"""
    f = lambda T: x1 * P_sat(sp1, T) + (1 - x1) * P_sat(sp2, T) - P
    return brentq(f, 0, 300)

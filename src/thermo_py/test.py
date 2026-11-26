from db import get

def cp_T(compound, Tf, Ti):
    A = get(compound, "cp_gas")["A"]
    B = get(compound, "cp_gas")["B"]
    C = get(compound, "cp_gas")["C"]
    D = get(compound, "cp_gas")["D"]

    return A*(Tf - Ti) + (B/2)*(Tf**2 - Ti**2) + (C/3)*(Tf**3 - Ti**3) +(D/4)*(Tf**4 - Ti**4)


print(.95 * cp_T("ethane", 298, 773) + 3.23 * cp_T("oxygen", 298, 773))
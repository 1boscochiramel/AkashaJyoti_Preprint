import numpy as np
import yaml
import os

# Constants for Hydrogen
MW_H2 = 2.01588e-3  # kg/mol
R = 8.314462618  # J/(mol K)

# Peng-Robinson Constants for Hydrogen (Default)
PR_CONSTANTS = {
    'Tc': 33.145,       # K
    'Pc': 1.2964e6,     # Pa
    'omega': -0.219     # Acentric factor
}

def load_eos_config(config_path):
    """
    Loads EOS constants from a YAML file and updates the global PR_CONSTANTS.
    The YAML should have an 'eos_constants' key or top-level keys matching PR_CONSTANTS.
    """
    if not os.path.exists(config_path):
        return

    try:
        with open(config_path, 'r') as f:
            data = yaml.safe_load(f)

        # Look for 'eos_constants' key or merge top-level
        updates = data.get('eos_constants', data)

        for k in PR_CONSTANTS:
            if k in updates:
                PR_CONSTANTS[k] = updates[k]

    except Exception as e:
        print(f"Warning: Failed to load EOS config from {config_path}: {e}")

def solve_cubic(a, b, c, d):
    """
    Solves the cubic equation ax^3 + bx^2 + cx + d = 0 for x.
    Returns real roots.
    """
    coeffs = [a, b, c, d]
    roots = np.roots(coeffs)
    real_roots = roots[np.isreal(roots)].real
    return real_roots

def Z_PR(P_Pa, T_K):
    """
    Calculates the compressibility factor Z using the Peng-Robinson EOS.
    Returns the stable real root (largest for gas/supercritical).
    """
    Tc = PR_CONSTANTS['Tc']
    Pc = PR_CONSTANTS['Pc']
    omega = PR_CONSTANTS['omega']

    if P_Pa == 0:
        return 1.0

    Tr = T_K / Tc

    kappa = 0.37464 + 1.54226 * omega - 0.26992 * omega**2
    alpha = (1 + kappa * (1 - np.sqrt(Tr)))**2

    a = 0.45724 * (R * Tc)**2 / Pc * alpha
    b = 0.07780 * R * Tc / Pc

    A = a * P_Pa / (R * T_K)**2
    B = b * P_Pa / (R * T_K)

    # Cubic equation coefficients for Z
    c3 = 1.0
    c2 = -(1 - B)
    c1 = A - 3 * B**2 - 2 * B
    c0 = -(A * B - B**2 - B**3)

    roots = solve_cubic(c3, c2, c1, c0)

    return np.max(roots)

def rho_g_PR(P_Pa, T_K):
    """
    Calculates gas density in kg/m3 using PR EOS.
    """
    Z = Z_PR(P_Pa, T_K)
    rho = (P_Pa * MW_H2) / (Z * R * T_K)
    return rho

def phi_PR(P_Pa, T_K):
    """
    Calculates the fugacity coefficient phi using PR EOS.
    """
    if P_Pa == 0:
        return 1.0

    Tc = PR_CONSTANTS['Tc']
    Pc = PR_CONSTANTS['Pc']
    omega = PR_CONSTANTS['omega']

    Z = Z_PR(P_Pa, T_K)

    Tr = T_K / Tc

    kappa = 0.37464 + 1.54226 * omega - 0.26992 * omega**2
    alpha = (1 + kappa * (1 - np.sqrt(Tr)))**2

    a = 0.45724 * (R * Tc)**2 / Pc * alpha
    b = 0.07780 * R * Tc / Pc

    A = a * P_Pa / (R * T_K)**2
    B = b * P_Pa / (R * T_K)

    sqrt2 = np.sqrt(2)

    term1 = Z - 1
    term2 = np.log(max(Z - B, 1e-10))
    term3 = (A / (2 * sqrt2 * B)) * np.log((Z + (1 + sqrt2) * B) / (Z + (1 - sqrt2) * B))

    ln_phi = term1 - term2 - term3
    return np.exp(ln_phi)

def fugacity_PR(P_Pa, T_K):
    """
    Calculates fugacity in Pa.
    """
    return phi_PR(P_Pa, T_K) * P_Pa

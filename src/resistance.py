def R_conv(h, A):
    """
    Calculates convective thermal resistance.
    R = 1 / (h * A)
    """
    if h <= 0 or A <= 0:
        return float('inf')
    return 1.0 / (h * A)

def R_cond_layer(thickness, k, A):
    """
    Calculates conductive thermal resistance for a layer.
    R = thickness / (k * A)
    """
    if k <= 0 or A <= 0:
        return float('inf')
    return thickness / (k * A)

def R_contact(R_contact_m2K_W, A):
    """
    Calculates contact resistance.
    R = R_contact_m2K_W / A
    """
    if A <= 0:
        return float('inf')
    return R_contact_m2K_W / A

def R_total(geometry, wall_set, contact_layer=None, lattice_extra_R_K_W=0.0):
    """
    Calculates the total thermal resistance of the wall chain in K/W.

    Parameters:
    - geometry: Object or dict containing 'A_int' and 'A_ext' (m2).
    - wall_set: Dict defining wall layers and h coefficients (from YAML).
    - contact_layer: Optional dict with 'R_contact_m2K_W'.
    - lattice_extra_R_K_W: Additional resistance to add (default 0.0).

    Returns:
    - Total resistance in K/W.
    """
    # Extract areas
    if isinstance(geometry, dict):
        A_int = geometry.get('A_int')
        A_ext = geometry.get('A_ext')
    else:
        A_int = getattr(geometry, 'A_int', None)
        A_ext = getattr(geometry, 'A_ext', None)

    if A_int is None or A_ext is None:
        raise ValueError("Geometry must provide A_int and A_ext")

    # Average area for conduction layers (Arithmetic mean as a robust approximation for now)
    A_mean = (A_int + A_ext) / 2.0

    # Internal Convection
    h_int = wall_set.get('h_int_W_m2K', 0)
    R_in = R_conv(h_int, A_int)

    # Wall Layers Conduction
    R_layers = 0.0
    layers = wall_set.get('wall_layers', [])
    for layer in layers:
        k = layer.get('k_W_mK')
        thickness = layer.get('thickness_m')
        R_layers += R_cond_layer(thickness, k, A_mean)

    # External Convection
    h_ext = wall_set.get('h_ext_W_m2K', 0)
    R_out = R_conv(h_ext, A_ext)

    # Contact Resistance (if provided)
    R_cont = 0.0
    if contact_layer:
        r_val = contact_layer.get('R_contact_m2K_W', 0)
        R_cont = R_contact(r_val, A_mean) # Apply at mean area or should it be A_int/ext?
                                         # Usually contact is at an interface.
                                         # Without specific interface info, A_mean is the safest generic assumption
                                         # for a 1D model unless specified.

    # Total
    R_tot = R_in + R_layers + R_out + R_cont + lattice_extra_R_K_W

    return R_tot

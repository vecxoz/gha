import numpy as np

def circumference(radius):
    """
    Calculate the circumference i.e. perimeter of a circle
    """
    if not isinstance(radius, (int, float)) or radius <= 0:
        raise ValueError('Radius must be positive non-zero number (%s was given)' % str(radius))
    return 2 * np.pi * radius

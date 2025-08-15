
# Define two complex vectors
u = [1 + 2j, 3j, 4 - 1j]  # j instead of i in Python
v = [2 - 1j, 5j, 1 + 0j]


def complex_inner_product(u, v):
    """
    Computes the inner product of two complex vectors u and v.
    
    Parameters:
        u (list of complex numbers): First vector (e.g., [1+2j, 3j, 4-1j]).
        v (list of complex numbers): Second vector (same length as u).
    
    Returns:
        complex: The inner product (dot product) of u and v.
    
    Raises:
        ValueError: If vectors have different lengths.
    """

    
    if len(u) != len(v):
        raise ValueError("Vectors must have the same length.")
    
    inner_product = 0 + 0j  # Initialize as complex zero
    for ui, vi in zip(u, v):
        inner_product += ui.conjugate() * vi  # Conjugate u's element before multiplying
    
    
    
    return inner_product


# Compute inner product
result = complex_inner_product(u, v)
print(result)  # Output: (9-10j)

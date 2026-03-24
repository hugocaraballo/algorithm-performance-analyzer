import random

def create_vector(n: int) -> list:
    """Builds a list of random integers in a fixed range.

    Args:
        n: Number of elements to generate.

    Returns:
        A list of ``n`` integers, each uniformly sampled from 1 to 10000 inclusive.
    """
    vector = []
    for i in range(n):
        vector.append(random.randint(1,10000))
    return vector

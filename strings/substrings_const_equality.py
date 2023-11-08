class SubStringEquality:
    """Class to check equality of substrings within a string using rolling hash.

    Attributes:
        _s (str): The input string.
        _p (int): A large prime number for the modulus of the hash function.
        _t (int): The base for the polynomial rolling hash function.
        _hashes (list): Prefix hashes of the string.
        _powers (list): Powers of _t mod _p.
    """

    def __init__(self, s: str):
        self._n = len(s)
        self._s = ' ' + s     # For indexing from 1
        self._p = 10**9 + 7  # Big prime integer
        self._t = 257        # Should not be divisor of _p
        self._hashes = [0] * (self._n + 1)
        self._powers = [1] + [0] * self._n
        self._preprocess()

    def _preprocess(self):
        """Precompute the hashes and powers for the rolling hash function."""
        for i in range(1, self._n + 1):
            self._hashes[i] = (self._hashes[i - 1] * self._t + ord(self._s[i])) % self._p
            self._powers[i] = (self._powers[i - 1] * self._t) % self._p

    def is_equal(self, from1: int, from2: int, slen: int) -> bool:
        """Check if substrings starting at from1 and from2 of given length are equal.

        Args:
            from1 (int): Start index of the first substring.
            from2 (int): Start index of the second substring.
            length (int): Length of the substrings to compare.

        Returns:
            bool: True if the substrings are equal, False otherwise.
        """
        return (
            (self._hashes[from1 + slen] + self._hashes[from2] * self._powers[slen]) % self._p ==
            (self._hashes[from2 + slen] + self._hashes[from1] * self._powers[slen]) % self._p
        )
